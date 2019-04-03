from rest_framework import viewsets

from paciente.models import Paciente, Dieta
from nutricao.api.serializers import *
from nutricao.api.filters import PacienteFilter

# ViewSets define the view behavior.
class PacienteViewSet(viewsets.ModelViewSet):
    #queryset = Paciente.objects.all()
    #queryset = Paciente.objects.filter(profissao = 'Analista')
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_class = PacienteFilter

class DietaViewSet(viewsets.ModelViewSet):
    #queryset = Paciente.objects.all()
    queryset = Dieta.objects.all()
    serializer_class = DietaSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class NutricionistaViewSet(viewsets.ModelViewSet):
    queryset = Nutricionista.objects.all()
    serializer_class = NutricionistaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
