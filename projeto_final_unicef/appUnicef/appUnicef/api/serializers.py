from rest_framework import serializers

from mortalidade_infantil.models import Country, Mortality

# Serializers define the API representation.
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('iso_code','country_name')

# Serializers define the API representation.
class MortalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortality
        fields = ('iso_code','median','year')
