import django_filters

from combustivel.models import Combustivel

class CombustivelFilter(django_filters.FilterSet):
    class Meta:
        model = Combustivel
        fields = {'cnpj': ['exact', 'in', 'startswith'], 
                  'nome': ['exact', 'in', 'startswith'], 
                  'uf': ['exact', 'in', 'startswith'], 
                  'valor_venda': ['exact', 'in', 'startswith'],
                  'data_cadastro': ['exact', 'range'] 
                 }

