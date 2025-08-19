from django.db import models

class Vaga(models.Model):

  titulo = models.CharField(max_length=100)
  setor = models.CharField(max_length=100)
  data_abertura = models.DateField(auto_now_add=True)
  
  STATUS_CHOICES = (
    ('aberta', 'Aberta'),
    ('fechada', 'Fechada'),
  )

  status = models.CharField(max_length=20, choices=STATUS_CHOICES)

  def __str__(self):
    return self.titulo

class Candidato(models.Model):

  nome = models.CharField(max_length=100)
  e_mail = models.EmailField(unique=True)
  data_nascimento = models.DateField()
  experiencia = models.TextField()

  vagas = models.ManyToManyField(Vaga, through='Candidatura')

  def __str__(self):
    return self.nome

class Candidatura(models.Model):

  candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
  data = models.DateField(auto_now_add=True)

  STATUS_CANDIDATURA_CHOICES = (
    ('pendente', 'Pendente'),
    ('aprovada', 'Aprovada'),
    ('rejeitada', 'Rejeitada'),
  )

  status_candidatura = models.CharField(max_length=20, choices=STATUS_CANDIDATURA_CHOICES, default='pendente')