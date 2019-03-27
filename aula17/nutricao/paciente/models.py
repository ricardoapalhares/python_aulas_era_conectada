from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200) 
    idade = models.DateTimeField()
    telefone = models.CharField(max_length=15)
    profissao = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.nome

class Dieta(models.Model):
    PERIODO = (('1','Manhã'),('2','Tarde'),('3','Noite'))
    
    #paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    paciente = models.ManyToManyField(Paciente, related_name='dieta')
    plano_alimentar = models.CharField(max_length=200)
    periodo = models.CharField(max_length=20, choices=PERIODO)

    