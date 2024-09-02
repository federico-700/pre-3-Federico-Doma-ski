from django import forms
from django.core.exceptions import ValidationError
from .models import Ofertas



class OfertasForm(forms.ModelForm):
    class Meta:
        model = Ofertas
        #fields = ['nombre','descripcion']
        fields = '__all__'

  








