"""nutricao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from paciente.models import Paciente, Dieta

# Serializers define the API representation.
class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ('nome', 'idade')
        #fields = ('nome', 'idade', 'telefone', 'profissao', 'email')

class DietaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dieta
        fields = '__all__'

# ViewSets define the view behavior.
class PacienteViewSet(viewsets.ModelViewSet):
    #queryset = Paciente.objects.all()
    queryset = Paciente.objects.filter(profissao = 'Analista')
    serializer_class = PacienteSerializer

class DietaViewSet(viewsets.ModelViewSet):
    #queryset = Paciente.objects.all()
    queryset = Dieta.objects.all()
    serializer_class = DietaSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'dietas', DietaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]