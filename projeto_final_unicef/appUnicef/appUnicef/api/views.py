from rest_framework import viewsets

from mortalidade_infantil.models import Country, Mortality
from appUnicef.api.serializers import *
from appUnicef.api.filters import CountryFilter, MortalityFilter

# ViewSets define the view behavior.
class CountryViewSet(viewsets.ModelViewSet):
    #queryset = Combustivel.objects.all()
    #queryset = Combustivel.objects.filter(uf = 'SC')
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_class = CountryFilter

class MortalityViewSet(viewsets.ModelViewSet):
    queryset = Mortality.objects.all()
    serializer_class = MortalitySerializer
    filter_class = MortalityFilter