from django.shortcuts import render, redirect
from django.template import loader
from forms import ArtistasForm


def inicio(request):
    return render(request, "AppBlog/inicio.html",{})

def galeria(request):
    return render(request, "AppBlog/galeria.html",{})

def clientes(request):
    return render(request, "AppBlog/clientes.html",{})

def artista(request):
    return render(request, "AppBlog/artista.html")

def artistas_formulario(request):
    if request.method == 'POST':
       formulario = ArtistasForm(request.POST)
       if formulario.is_valid():
           data=formulario.cleaned_data
           artista.objects.create(artista=data['artista'], galeria=data['artista'])
           return redirect('artistas')
    else:
        formulario = ArtistasForm()
        return render (request, 'AppBlog/artistasFormulario.html')
    return render(request, "AppBlog/artista.html",{})
