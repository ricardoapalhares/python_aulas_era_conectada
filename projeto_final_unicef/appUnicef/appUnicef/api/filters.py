import django_filters

from mortalidade_infantil.models import Country, Mortality

class CountryFilter(django_filters.FilterSet):
    class Meta:
        model = Country
        fields = {'iso_code': ['exact', 'in', 'startswith'], 
                  'country_name': ['exact', 'in', 'startswith'] 
                 }

class MortalityFilter(django_filters.FilterSet):
    class Meta:
        model = Mortality
        fields = {'median': ['exact', 'in', 'startswith'],
                  'year': ['exact', 'in', 'startswith'] 
                 }
