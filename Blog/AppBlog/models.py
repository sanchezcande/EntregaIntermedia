from django.forms import IntegerField
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=40,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    experiencia = models.IntegerField(null=True, blank=True)
    trabajosRealizados = models.CharField(max_length=100,null=True, blank=True)
    galeria=models.CharField(max_length=60,null=True, blank=True)
    
    def __str__(self):
        return f'Artista {self.nombre} ({self.galeria})'


class Galeria(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    artistasQueExponen = models.CharField(max_length=100)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    artistaAlQueLeCompro = models.CharField(max_length=40)
    galeriaALaQueLeCompro = models.CharField(max_length=40)
    
