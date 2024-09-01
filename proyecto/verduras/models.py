from django.db import models

class Verduras(models.Model):
    nombre_verduras = models.CharField(max_length=50, unique=True)
    kilo_verduras=models.IntegerField()
    monto_verduras= models.DecimalField(max_digits=10, decimal_places=2)


                  
    def __str__(self):
        return f'{self.nombre_verduras}, {self.kilo_verduras} kilo,{self.monto_verduras} pesos'





