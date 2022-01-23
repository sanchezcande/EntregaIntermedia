from django.forms import IntegerField
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    experiencia = models.IntegerField()
    trabajosRealizados = models.CharField(max_length=100)

class Galeria(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    artistasQueExponen = models.CharField(max_length=100)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    artistaAlQueLeCompro = models.CharField(max_length=40)
    galeriaALaQueLeCompro = models.CharField(max_length=40)
    
