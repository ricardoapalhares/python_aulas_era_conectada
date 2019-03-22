from django import forms
from django.forms import ModelForm

from .models import Paciente, Dieta

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome','idade','telefone','profissao','email')
    
    #nome = forms.CharField(label='nome', max_length=200)
    #idade = forms.DateTimeField()
    #telefone = forms.CharField(max_length=15)
    #profissao = forms.CharField(max_length=50)
    #email = forms.EmailField(max_length=254)

class DietaForm(ModelForm):
    class Meta:    
        model = Dieta
        fields = ('paciente','plano_alimentar','periodo')
    
    #paciente = forms.ModelChoiceField(queryset=Paciente.objects.all())
    #plano_alimentar = forms.CharField(max_length=200)
    #periodo = forms.ChoiceField(choices=[('1','Manhã'),('2','Tarde'),('3','Noite')])