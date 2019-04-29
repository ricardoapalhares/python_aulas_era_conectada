from django import forms
from django.forms import ModelForm

from .models import *

class CombustivelForm(ModelForm):
    class Meta:
        model = Combustivel
        fields = ('id','cnpj','nome','endereco','numero','complemento','bairro','municipio','uf','produto','valor_venda','data_cadastro','latitude','longitude')
