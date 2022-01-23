from django import forms

class ArtistasForm(forms.Form):
    artista=forms.CharField(max_length=60)
    galeria=forms.CharField(max_length=60)