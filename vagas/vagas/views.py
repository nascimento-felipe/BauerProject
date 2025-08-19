from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Candidatura, Candidato, Vaga

def listagem(request):
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
    