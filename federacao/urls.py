from django.urls import path

from .views import *
from federacao.utils.obter_municipio import obter_municipio
from federacao.utils.obter_bairro import obter_bairro


urlpatterns = [
    path('index/', formulario, name='formulario'),
    path('ajax/obter/municipio/', obter_municipio, name='obter_municipio'),
    path('ajax/obter/bairro/', obter_bairro, name='obter_bairro'),
]