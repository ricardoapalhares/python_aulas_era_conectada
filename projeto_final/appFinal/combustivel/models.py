from django.db import models

class Combustivel(models.Model):
    id = models.CharField(primary_key=True, max_length=200) 
    cnpj = models.CharField(max_length=200) 
    nome = models.CharField(max_length=200) 
    endereco = models.CharField(max_length=200) 
    numero = models.CharField(max_length=200) 
    complemento = models.CharField(max_length=200) 
    bairro = models.CharField(max_length=200) 
    municipio = models.CharField(max_length=200) 
    uf = models.CharField(max_length=200) 
    produto = models.CharField(max_length=200) 
    #valor_venda = models.CharField(max_length=200)
    valor_venda = models.DecimalField(default=0, max_digits=3, decimal_places=2) 
    #data_cadastro = models.CharField(max_length=200) 
    data_cadastro = models.DateTimeField(null=True)
    latitude = models.CharField(max_length=200) 
    longitude = models.CharField(max_length=200) 
    #sexo = models.CharField(max_length=20, blank='True', choices=[('1','masculino'),('2','feminino')])

    class Meta:
       managed = False
       db_table = 'combustivel'

    def __str__(self):
        return self.nome


