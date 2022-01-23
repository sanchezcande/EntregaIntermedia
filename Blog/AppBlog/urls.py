from django.urls import path
from AppBlog import views


urlpatterns = [
<<<<<<< HEAD
    path('', views.inicio, name = "inicio"),
    path('galeria', views.galeria, name = "galeria"),
    path('artista', views.artista, name = "artista"),
    path('clientes', views.clientes, name = "clientes"),
    path('artistasFormulario', views.artistas_formulario, name = "artistas_formulario"),
=======
    path('', inicio, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('artista/', artista, name='artista'),
    path('clientes/', clientes, name='clientes'),
    # path('entregables', views.entregables, name = "entregables"),
>>>>>>> ccde5510124406a330969b16e5a7f4cae331160e
]