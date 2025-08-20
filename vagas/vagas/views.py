from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Candidatura, Candidato, Vaga
import pandas as pd

def listagem(request: HttpRequest):
    candidaturas_list = Candidatura.objects.select_related('candidato', 'vaga').all()
    return render(request, 'vagas/listagem.html', {'candidaturas_list': candidaturas_list})

def associacao_vagas(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        candidato_id = request.POST.get('candidato')
        vaga_id = request.POST.get('vaga')

        if candidato_id and vaga_id:
          Candidatura.objects.create(candidato_id=candidato_id, vaga_id=vaga_id)
          return redirect('/')

    candidatos = Candidato.objects.all()
    vagas = Vaga.objects.all()
    return render(request, 'vagas/candidatos-vagas.html', {'candidatos': candidatos, 'vagas': vagas})
    
def dashboard(request: HttpRequest):
    import datetime
    import math
    from collections import Counter

    # Total de vagas total, vagas abertas e vagas fechadas
    vagas_query = Vaga.objects.all().values('id', 'titulo', 'status')
    df_vagas = pd.DataFrame(list(vagas_query))
    
    abertas = fechadas = 0
    
    if not df_vagas.empty:
        abertas = (df_vagas['status'] == 'aberta').sum()
        fechadas = (df_vagas['status'] == 'fechada').sum()

    # Número de candidatos por vaga
    candidatura_query = Candidatura.objects.values('vaga_id')
    df_candidaturas = pd.DataFrame(list(candidatura_query))
    
    candidatos_por_vaga = {}

    if not df_candidaturas.empty:
        # relaciona o id da vaga com o titulo
        id_to_titulo = {vaga['id']: vaga['titulo'] for vaga in vagas_query}
        
        # conta a quantidade de candidatos por vaga
        counts = df_candidaturas['vaga_id'].value_counts().to_dict()

        # formata o nome da vaga como chave e a quantidade de candidatos como valor
        candidatos_por_vaga = {id_to_titulo.get(vaga_id, str(vaga_id)): count for vaga_id, count in counts.items()}

    # Média da idade dos candidatos
    candidatos_query = Candidato.objects.values('data_nascimento')
    
    idades = []
    
    for candidato in candidatos_query:
        idade = (datetime.date.today() - candidato['data_nascimento']).days // 365
        idades.append(idade)

    media_idade = None
    df_idades = pd.DataFrame(idades, columns=['idade'])

    if not df_idades.empty:
        media_idade = math.floor(df_idades['idade'].mean())

    
    # Setor com mais vagas abertas
    vagas_banco = Vaga.objects.values_list('setor', flat=True)
    setor_counts = Counter(vagas_banco)
    setores_ordenados = [{'setor': setor, 'contagem': count} for setor, count in sorted(setor_counts.items(), reverse=True)]

    return render(request, 'vagas/dashboard.html', {
        'total_vagas': len(df_vagas),
        'total_abertas': abertas,
        'total_fechadas': fechadas,
        'candidatos_por_vaga': candidatos_por_vaga,
        'media_idade': media_idade,
        'setores_ordenados': setores_ordenados,
    })