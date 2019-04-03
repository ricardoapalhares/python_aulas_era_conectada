from rest_framework import serializers

from paciente.models import Paciente, Dieta, Especialidade, Nutricionista, Consulta, Avaliacao

# Serializers define the API representation.
#class PacienteSerializer(serializers.HyperlinkedModelSerializer):
class DietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = ('plano_alimentar', 'periodo')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('nome', 'data_nascimento', 'telefone', 'profissao', 'email', 'sexo')
    
class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('nome', 'descricao')

class NutricionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricionista
        fields = ('nome', 'especialidades', 'email', 'telefone', 'crn')

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('data_hora', 'tipo', 'local', 'dieta', 'paciente', 'nutricionista', 'avaliacao')

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('peso', 'altura')
