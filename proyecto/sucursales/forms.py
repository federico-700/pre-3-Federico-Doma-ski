from django import forms
from django.core.exceptions import ValidationError
from .models import Sucursales



class SucursalesForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        #fields = ['nombre','descripcion']
        fields = '__all__'

  








