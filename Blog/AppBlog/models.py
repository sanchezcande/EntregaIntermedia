from tabnanny import verbose
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User

class Artista(Model):
    nombre = CharField(max_length=40,null=True, blank=True)
    edad = IntegerField(null=True, blank=True)
    experiencia = IntegerField(null=True, blank=True)
    trabajosRealizados = CharField(max_length=100,null=True, blank=True)
    galeria=CharField(max_length=60,null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre} ({self.galeria})'


class Galeria(Model):
    nombre = CharField(max_length=40)
    direccion = CharField(max_length=40)
    artistasQueExponen = CharField(max_length=100)
    
    def __str__(self):
        return f'La galería {self.nombre} queda en la dirección {self.direccion}.'
    
class Cliente(Model):
    nombre = CharField(max_length=40, verbose_name='nombre y apellido')
    artistaAlQueLeCompro = CharField(max_length=40, verbose_name='Autor de la obra', blank=True, null=True)
    galeriaEnQueCompro = CharField(max_length=40, verbose_name='Galería en la adquirió la obra', blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre} le compró al artista {self.artistaAlQueLeCompro} en la galería {self.galeriaEnQueCompro}.'
    
class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', null=True, blank=True)
    
