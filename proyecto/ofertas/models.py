from django.db import models
from django.db import models


class Ofertas(models.Model):
    """
    El modelo Ofertas representa ofertas especiales en la verdulería.

    Atributos:
        nombre_ofertas (CharField): El nombre de la oferta, debe ser único para evitar duplicados.
        kilo_ofertas (IntegerField): La cantidad de kilos de la oferta.
        monto_ofertas (DecimalField): El precio de la oferta en pesos.
    """




    nombre_ofertas = models.CharField(max_length=50, unique=True)
    kilo_ofertas=models.IntegerField()
    monto_ofetas= models.DecimalField(max_digits=10, decimal_places=2)


                  
    def __str__(self):
        return f'{self.nombre_ofertas}, {self.kilo_ofertas} kilos,{self.monto_ofetas} pesos'

