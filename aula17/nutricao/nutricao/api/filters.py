import django_filters

from paciente.models import Paciente, Dieta

class PacienteFilter(django_filters.FilterSet):
    class Meta:
        model = Paciente
        fields = {'nome': ['exact', 'in', 'startswith']}

