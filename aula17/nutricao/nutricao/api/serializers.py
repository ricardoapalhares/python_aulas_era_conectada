from paciente.models import Paciente, Dieta
from rest_framework import serializers

# Serializers define the API representation.
class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        #fields = ('nome', 'idade')
        fields = ('nome', 'idade', 'telefone', 'profissao', 'email')

class DietaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dieta
        fields = '__all__'

