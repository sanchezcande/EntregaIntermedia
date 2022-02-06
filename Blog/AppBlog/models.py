from django.forms import IntegerField
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=40,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    experiencia = models.IntegerField(null=True, blank=True)
    trabajosRealizados = models.CharField(max_length=100,null=True, blank=True)
    galeria=models.CharField(max_length=60,null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre} ({self.galeria})'


class Galeria(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    artistasQueExponen = models.CharField(max_length=100)
    
    def __str__(self):
        return f'La galería {self.nombre} queda en la dirección {self.direccion}.'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='nombre y apellido')
    artistaAlQueLeCompro = models.CharField(max_length=40, verbose_name='Autor de la obra', blank=True, null=True)
    galeriaEnQueCompro = models.CharField(max_length=40, verbose_name='Galería en la adquirió la obra', blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre} le compró al artista {self.artistaAlQueLeCompro} en la galería {self.galeriaEnQueCompro}.'
    
