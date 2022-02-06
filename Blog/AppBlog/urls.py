from django.urls import path
from .views import artistas, artistas_formulario, inicio, galeria, clientes, buscar, busqueda_artista, galerias_formulario, clientes_formulario
from AppBlog import views 
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('artistasFormulario/', artistas_formulario, name = 'artistas_formulario'),
    path('', inicio, name='inicio'),
    path('galerias/', galeria, name='galerias'),
    path('artistas/', artistas, name='artistas'),
    path('buscar/', buscar, name='buscar'),
    path('busquedaArtistas/', busqueda_artista, name='busqueda_artista'),
    path('galeriasFormulario/', galerias_formulario, name = 'galerias_formulario'),
    path('clientes/', views.ClienteListView.as_view(), name="clientes"),
    path('clientes/add', views.ClienteCreateView.as_view(), name="cliente_add"),
    path('clientes/update/<pk>', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/delete/<pk>', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/view/<pk>', views.ClienteDetailView.as_view(), name='cliente_view'),
]