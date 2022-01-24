from django.shortcuts import render, redirect
from django.template import loader
from .forms import ArtistasForm, ClientesForm, GaleriasForm
from .models import *
from django.http import HttpResponse

def crear_artista(request, camada):
    artista = Artista(nombre='Van Gogh', galeria=galeria)
    artista.save()

    return HttpResponse(f'Artista creado! {artista}')

def inicio(request):
    return render(request, "AppBlog/inicio.html",{})

def galeria(request):
    return render(request, "AppBlog/galeria.html",{})

def clientes(request):
    return render(request, "AppBlog/clientes.html",{})

def artistas(request):
    return render(request, "AppBlog/artistas.html")

def busqueda_artista(request):
    return render(request, 'AppBlog/busquedaArtistas.html')

def artistas_formulario(request):
    if request.method == 'POST':
        formulario = ArtistasForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Artista.objects.create(nombre=data['artista'], galeria=data['galeria'])
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