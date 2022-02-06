from multiprocessing.connection import Client
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from .forms import ArtistasForm, ClientesForm, GaleriasForm
from .models import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def crear_artista(request, camada):
    artista = Artista(nombre='Van Gogh', galeria=galeria)
    artista.save()

    return HttpResponse(f'Artista creado! {artista}')

def inicio(request):
    return render(request, "AppBlog/inicio.html",{})

def galeria(request):
    return render(request, "AppBlog/galerias.html",{})

def clientes(request):
    return render(request, "AppBlog/clientes.html",{})

def artistas(request):
    artistas= Artista.objects.all()
    return render(request, "AppBlog/artistas.html",{'artistas': artistas})



def busqueda_artista(request):
    return render(request, 'AppBlog/busquedaArtistas.html')

def artistas_formulario(request):
    if request.method == 'POST':
        formulario = ArtistasForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Artista.objects.create(nombre=data['artista'], galeria=data['galeria'] )
            return redirect('artistas')
    else:
        formulario = ArtistasForm()
    return render(request, 'AppBlog/artistasFormulario.html', {'formulario': formulario})

def buscar(request):
    galeria = request.GET.get("galeria")
    
    if galeria:
        artistas = Artista.objects.filter(galeria=galeria)

        return render(request, 'AppBlog/buscar.html',
            {'artistas': artistas, 'galeria': galeria})
    else:
        return HttpResponse('No se envió una galería válida')
    
def clientes_formulario(request):
    if request.method == 'POST':
        formulario = ClientesForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Cliente.objects.create(nombre=data['nombre'], artistaAlQueLeCompro=data['artistaAlQueLeCompro'], galeriaALaQueLeCompro=data['galeriaALaQueLeCompro'])
            return redirect('clientes')
    else:
        formulario = ClientesForm()
    return render(request, 'AppBlog/clientesFormulario.html', {'formulario': formulario})

def galerias_formulario(request):
    if request.method == 'POST':
        formulario = GaleriasForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Galeria.objects.create(nombre=data['nombre'], direccion=data['direccion'], artistasQueExponen=data['artistasQueExponen'])
            return redirect('galerias')
    else:
        formulario = GaleriasForm()
    return render(request, 'AppBlog/galeriasFormulario.html', {'formulario': formulario})


class ClienteListView(ListView):
    model = Cliente
    template_name = 'AppBlog/clientes.html' 
    context_object_name = 'clientes'   

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'AppBlog/ver_cliente.html' 

class ClienteCreateView(CreateView):
    model = Cliente
    success_url =  reverse_lazy ('clientes')
    fields = ['nombre', 'artistaAlQueLeCompro','galeriaEnQueCompro' ]
    template_name = 'AppBlog/cliente_form.html' 

class ClienteUpdateView(UpdateView):
    model = Cliente
    success_url =  reverse_lazy ('clientes')
    fields = ['nombre', 'artistaAlQueLeCompro','galeriaEnQueCompro' ]
    template_name = 'AppBlog/cliente_form.html' 
 
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')
    template_name = 'AppBlog/cliente_delete.html' 