from django.db import models


class Frutas(models.Model):
    """
    El modelo Frutas representa un tipo de fruta que se vende en la verdulería.

    Atributos:
        nombre_frutas (CharField): El nombre de la fruta, debe ser único.
        kilo_frutas (IntegerField): La cantidad de kilos de esta fruta.
        monto_frutas (DecimalField): El precio por kilo de la fruta en pesos.
    """
    nombre_frutas = models.CharField(max_length=50, unique=True)
    kilo_frutas=models.IntegerField()
    monto_frutas= models.DecimalField(max_digits=10, decimal_places=2)


                  
    def __str__(self):
        return f'{self.nombre_frutas}, {self.kilo_frutas} kilo,{self.monto_frutas} pesos'