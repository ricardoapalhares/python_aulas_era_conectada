from paciente.models import Paciente, Dieta
from rest_framework import viewsets

from nutricao.api.serializers import PacienteSerializer, DietaSerializer
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
