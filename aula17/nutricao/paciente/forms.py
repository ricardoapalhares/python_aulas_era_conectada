from django import forms
from django.forms import ModelForm

from .models import *

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome','data_nascimento','telefone','profissao','email','sexo')
    
    #nome = forms.CharField(label='nome', max_length=200)
    #idade = forms.DateTimeField()
    #telefone = forms.CharField(max_length=15)
    #profissao = forms.CharField(max_length=50)
    #email = forms.EmailField(max_length=254)

class DietaForm(ModelForm):
    class Meta:    
        model = Dieta
        fields = ('plano_alimentar','periodo')
    
    #paciente = forms.ModelChoiceField(queryset=Paciente.objects.all())
    #plano_alimentar = forms.CharField(max_length=200)
    #periodo = forms.ChoiceField(choices=[('1','Manhã'),('2','Tarde'),('3','Noite')])

class EspecialidadeForm(ModelForm):
    class Meta:    
        model = Especialidade
        fields = ('nome','descricao')

class NutricionistaForm(ModelForm):
    class Meta:    
        model = Nutricionista
        fields = ('nome', 'especialidades', 'email', 'telefone', 'crn')

class ConsultaForm(ModelForm):
    class Meta:    
        model = Consulta
        fields = ('data_hora', 'tipo', 'local', 'dieta', 'paciente', 'nutricionista','avaliacao')

class AvaliacaoForm(ModelForm):
    class Meta:    
        model = Avaliacao
        fields = ('peso', 'altura')
