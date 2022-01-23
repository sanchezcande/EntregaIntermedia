from django.urls import path
from .views import artistas, artistas_formulario, inicio, galeria, clientes, buscar


urlpatterns = [
    path('artistasFormulario/', artistas_formulario, name = 'artistas_formulario'),
    path('', inicio, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('artistas/', artistas, name='artistas'),
    path('clientes/', clientes, name='clientes'),
    path('buscar/', buscar, name='buscar')
]