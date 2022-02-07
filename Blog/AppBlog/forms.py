from django.forms import Form, CharField, BooleanField, EmailField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    

class UserRegisterForm(UserCreationForm):
    
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
        
        
class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)
    last_name = CharField()
    first_name = CharField()
    is_staff = BooleanField()
    
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

    
    
    