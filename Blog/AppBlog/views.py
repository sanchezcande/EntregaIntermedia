from django.shortcuts import render
from django.template import loader


def inicio(request):
    return render(request, "AppBlog/inicio.html",{})

def galeria(request):
    return render(request, "AppBlog/galeria.html",{})

def clientes(request):
    return render(request, "AppBlog/clientes.html",{})

def artista(request):
    return render(request, "AppBlog/artista.html",{})