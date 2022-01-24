from django.urls import path
from .views import artistas, artistas_formulario, inicio, galeria, clientes, buscar, busqueda_artista, galerias_formulario, clientes_formulario


urlpatterns = [
    path('artistasFormulario/', artistas_formulario, name = 'artistas_formulario'),
    path('', inicio, name='inicio'),
    path('galerias/', galeria, name='galerias'),
    path('artistas/', artistas, name='artistas'),
    path('clientes/', clientes, name='clientes'),
    path('buscar/', buscar, name='buscar'),
    path('busquedaArtistas/', busqueda_artista, name='busqueda_artista'),
    path('galeriasFormulario/', galerias_formulario, name = 'galerias_formulario'),
    path('clientesFormulario/', clientes_formulario, name = 'clientes_formulario'),

]