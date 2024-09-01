from django import forms
from django.core.exceptions import ValidationError
from .models import Ofertas




#class ProductoCategoriaForm(forms.ModelForm):
#    class Meta:
#        model = ProductoCategoria
#        #fields = ['nombre','descripcion']
#        fields = '__all__'
#
#    def clean_nombre(self):
#        nombre: str = self.cleaned_data.get('nombre','')
#
#        #validar que solo tenga letras
#
#        if not nombre.isalpha():
#            raise ValidationError('El nombre solo puede contener letras')
#        
#        if len(nombre) < 3 or len(nombre) > 50:
#           raise ValidationError ("El nombre debe tener una longitud minima de 3 letras o maxima de 50")
#        
#        return nombre





class OfertasForm(forms.ModelForm):
    class Meta:
        model = Ofertas
        #fields = ['nombre','descripcion']
        fields = '__all__'

  








