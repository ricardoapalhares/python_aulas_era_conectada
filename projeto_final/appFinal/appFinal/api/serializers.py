from rest_framework import serializers

from combustivel.models import Combustivel

# Serializers define the API representation.
class CombustivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combustivel
        fields = ('id','cnpj','nome','endereco','numero','complemento','bairro','municipio','uf','produto','valor_venda','data_cadastro','latitude','longitude')

