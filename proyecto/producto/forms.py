from django import forms
from django.core.exceptions import ValidationError
from .models import Producto



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ['nombre','descripcion']
        fields = '__all__'

  








