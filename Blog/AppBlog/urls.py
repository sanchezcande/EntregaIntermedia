from django.urls import path
# from AppBlog import views
# from django.urls import path
from .views import inicio, galeria, artista, clientes


urlpatterns = [
    path('', inicio, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('artista/', artista, name='artistas'),
    path('clientes/', clientes, name='clientes'),
    # path('entregables', views.entregables, name = "entregables"),
]