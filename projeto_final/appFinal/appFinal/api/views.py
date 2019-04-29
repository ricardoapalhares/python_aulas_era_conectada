from rest_framework import viewsets

from combustivel.models import Combustivel
from appFinal.api.serializers import *
from appFinal.api.filters import CombustivelFilter

# ViewSets define the view behavior.
class CombustivelViewSet(viewsets.ModelViewSet):
    #queryset = Combustivel.objects.all()
    #queryset = Combustivel.objects.filter(uf = 'SC')
    queryset = Combustivel.objects.all()
    serializer_class = CombustivelSerializer
    filter_class = CombustivelFilter

