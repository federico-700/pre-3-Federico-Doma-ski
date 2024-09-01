from django.db import models

# Create your models here.


##############################33
#from django.db import models
# Create your models here.



#cliente modelo tomo como ejemplo
#from django.db import models
#
#class Pais(models.Model):
#    nombre = models.CharField(max_length=50)
#
#    def __str__(self):
#        return self.nombre
#
#
#class Cliente(models.Model):
#    nombre = models.CharField(max_length=50)
#    apellido = models.CharField(max_length=50)
#    nacimiento = models.DateField(null=True, blank=True)
#    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
#
#    def __str__(self):
#        return f'{self.apellido}, {self.nombre}'
#############
from django.db import models


class Ofertas(models.Model):
    nombre_ofertas = models.CharField(max_length=50, unique=True)
    kilo_ofertas=models.IntegerField()
    monto_ofetas= models.DecimalField(max_digits=10, decimal_places=2)


                  
    def __str__(self):
        return f'{self.nombre_ofertas}, {self.kilo_ofertas} kilos,{self.monto_ofetas} pesos'

