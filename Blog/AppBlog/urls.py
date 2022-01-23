from django.urls import path
from .views import artistas_formulario, inicio, galeria, artista, clientes


urlpatterns = [
    path('artistasFormulario/', artistas_formulario, name = 'artistas_formulario'),
    path('', inicio, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('artista/', artista, name='artista'),
    path('clientes/', clientes, name='clientes'),
]