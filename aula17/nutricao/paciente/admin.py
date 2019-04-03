from django.contrib import admin
from .models import *

admin.site.register(Paciente)
admin.site.register(Dieta)
admin.site.register(Especialidade)
admin.site.register(Nutricionista)
admin.site.register(Consulta)
admin.site.register(Avaliacao)