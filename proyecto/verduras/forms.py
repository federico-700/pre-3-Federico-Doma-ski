from django import forms
from django.core.exceptions import ValidationError
from .models import Verduras




class VerdurasForm(forms.ModelForm):
    class Meta:
        model = Verduras
        #fields = ['nombre','descripcion']
        fields = '__all__'

  








