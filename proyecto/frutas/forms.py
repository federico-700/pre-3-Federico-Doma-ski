from django import forms
from django.core.exceptions import ValidationError
from .models import Frutas


class FrutasForm(forms.ModelForm):
    class Meta:
        model = Frutas
        #fields = ['nombre','descripcion']
        fields = '__all__'

  








