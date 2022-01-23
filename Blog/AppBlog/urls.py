from django.urls import path
from AppBlog import views


urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('galeria', views.galeria, name = "galeria"),
    path('artista', views.artista, name = "artista"),
    path('clientes', views.clientes, name = "clientes"),
    path('artistasFormulario', views.artistas_formulario, name = "artistas_formulario"),
]