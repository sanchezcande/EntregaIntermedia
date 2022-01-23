from django.shortcuts import render, redirect
from django.template import loader
from .forms import ArtistasForm
from .models import *
from django.http import HttpResponse


def inicio(request):
    return render(request, "AppBlog/inicio.html",{})

def galeria(request):
    return render(request, "AppBlog/galeria.html",{})

def clientes(request):
    return render(request, "AppBlog/clientes.html",{})

def artistas(request):
    return render(request, "AppBlog/artistas.html")

def artistas_formulario(request):
    if request.method == 'POST':
       formulario = ArtistasForm(request.POST)
       
       if formulario.is_valid():
           data=formulario.cleaned_data
           Artista.objects.create(artistas=data['artistas'], galeria=data['artistas'])
           return redirect('artistas')
    else:
        formulario = ArtistasForm()
    return render (request, 'AppBlog/artistasFormulario.html', {'formulario': formulario})

def buscar(request):
    artista= request.GET.get("artista")
    
    if artista: 
        galeria= Artista.objects.filter(artista=artista)
        return render(request, 'AppCoder/buscar.html',
        {'artistas': artistas, 'galeria': galeria})
    else:
        return HttpResponse('No se envió un artista válido') 