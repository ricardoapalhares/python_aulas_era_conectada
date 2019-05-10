from django import forms
from django.forms import ModelForm

from .models import *

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ('iso_code','country_name')

class MortalityForm(ModelForm):
    class Meta:
        model = Mortality
        fields = ('iso_code','median','year')
