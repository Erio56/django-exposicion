from django.forms import ModelForm, fields
from django import forms

from .models import Pelicula


class peliculaForm(forms.ModelForm):
   class Meta:
      model= Pelicula
      fields = ['nombre_pelicula', 'calificacion']
      