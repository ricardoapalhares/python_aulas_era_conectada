from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path

from appUnicef.api.views import * 
from mortalidade_infantil import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'mortalities', MortalityViewSet, basename='mortalities')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('form-country/', views.country_view),
    path('form-mortality/', views.mortality_view),
    #path('form-mortality-o/', views.mortality_o_view),
    path('admin/', admin.site.urls),
]
