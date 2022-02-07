from multiprocessing.connection import Client
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from .forms import ArtistasForm, ClientesForm, GaleriasForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from AppBlog.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def crear_artista(request, camada):
    artista = Artista(nombre='Van Gogh', galeria=galeria)
    artista.save()

    return HttpResponse(f'Artista creado! {artista}')

def inicio(request):
    return render(request, "AppBlog/inicio.html",{})

def not_pages_yet(request):
    return render(request, "AppBlog/not_pages_yet.html",{})

def about_us(request):
    return render(request, "AppBlog/about_us.html",{})

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
    

def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return redirect(request, 'AppBlog/login.html', 
                            {'form': form,
                             'error': 'No es válido el usuario y contraseña' })  #Este código se podría ignorar

        else:
            return render(request, 'AppBlog/login.html', {'form': form})
        
    else:
        form=AuthenticationForm()
        return render(request, 'AppBlog/login.html', {'form': form})
    

class UserCreateView(CreateView):
    model=User
    success_url = reverse_lazy('login')
    template_name = 'AppBlog/register.html'
    form_class = UserRegisterForm
    
@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == "POST":
        formulario= UserEditForm(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            usuario.email=data['email']
            usuario.set_password(data['password1'])
            usuario.first_name=data['first_name']
            usuario.last_name=data['last_name']
            usuario.save()
            return redirect('inicio')

            
    else:
        formulario = UserEditForm ({'email': usuario.email})
        
    return render(request, 'AppBlog/register.html', {'form': formulario})