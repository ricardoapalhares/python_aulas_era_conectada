from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200) 
    idade = models.DateTimeField()
    telefone = models.CharField(max_length=15)
    profissao = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)





