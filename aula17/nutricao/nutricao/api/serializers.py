from rest_framework import serializers

from paciente.models import Paciente, Dieta

# Serializers define the API representation.
#class PacienteSerializer(serializers.HyperlinkedModelSerializer):
class DietaSerializer(serializers.ModelSerializer):
    PERIODO = [('1','Manhã'),('2','Tarde'),('3','Noite')]
    
    paciente = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Dieta
        #fields = ('paciente', 'plano_alimentar', 'periodo', 'paciente')
        fields = ('paciente', 'plano_alimentar', 'periodo', 'paciente')

class PacienteSerializer(serializers.ModelSerializer):
    dieta = DietaSerializer(many=True, read_only=True)
    class Meta:
        model = Paciente
        #fields = ('nome', 'idade')
        fields = ('nome', 'idade', 'telefone', 'profissao', 'email', 'dieta')

