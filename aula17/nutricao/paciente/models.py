from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200) 
    data_nascimento = models.DateTimeField()
    telefone = models.CharField(max_length=15)
    profissao = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    sexo = models.CharField(max_length=20, choices=[('M','Masculino'),('F','Feminino')])

    def __str__(self):
        return self.nome

class Dieta(models.Model):
    plano_alimentar = models.CharField(max_length=200)
    periodo = models.CharField(max_length=20, choices=[('1','Manhã'),('2','Tarde'),('3','Noite')])

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=20, choices=[('1','Consulta'),('2','Retorno')])
    local = models.CharField(max_length=200)

class Avaliacao(models.Model):
    peso = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    altura = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    local = models.CharField(max_length=200)

class Nutricionista(models.Model):
    nome = models.CharField(max_length=200) 
    especialidades = models.CharField(max_length=20, choices=[('1','Funcional'),('2','Esportivo'),('3','Pediatria')])
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=15)
    crn = models.CharField(max_length=30)


# AVALIACAO
 # peso
 # altura

# NUTRICIONISTA
 # nome
 # especialidade
 # email
 # telefone
 # crn