# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    iso_code = models.TextField(primary_key=True, null=False)  # This field type is a guess.
    country_name = models.TextField(blank=True, null=True, max_length=30)  # This field type is a guess.

    class Meta:
        db_table = 'country'
        
    def __str__(self):
        return self.country_name

class Mortality(models.Model):
    iso_code = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='iso_code')
    median = models.TextField(blank=True, null=True)  # This field type is a guess.
    year = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'mortality'
