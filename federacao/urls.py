from django.urls import path

from .views import *
from federacao.utils.obter_municipio import obter_municipio

urlpatterns = [
    path('index/', formulario, name='formulario'),
    path('ajax/obter/municipio/', obter_municipio, name='obter_municipio'),
]