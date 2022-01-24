from django.forms import Form, CharField

class ArtistasForm(Form):
    artista=CharField(max_length=60)
    galeria=CharField(max_length=60)

class ClientesForm(Form):
    nombre=CharField(max_length=60)
    artistaAlQueLeCompro = CharField(max_length=40,label="Artista a quien le compró")
    galeriaALaQueLeCompro = CharField(max_length=40,label="Galería a la que le compró la obra")
    
class GaleriasForm(Form):
    nombre = CharField(max_length=40)
    direccion = CharField(max_length=40)
    artistasQueExponen = CharField(max_length=100,label="Artistas que exponen")
    
    