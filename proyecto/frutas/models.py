from django.db import models


class Frutas(models.Model):
    nombre_frutas = models.CharField(max_length=50, unique=True)
    kilo_frutas=models.IntegerField()
    monto_frutas= models.DecimalField(max_digits=10, decimal_places=2)


                  
    def __str__(self):
        return f'{self.nombre_frutas}, {self.kilo_frutas} kilo,{self.monto_frutas} pesos'