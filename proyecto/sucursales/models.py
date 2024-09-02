from django.db import models


class Sucursales(models.Model):
    """
    El modelo Sucursales representa las distintas sucursales de la verdulería.

    Atributos:
        nombre_sucursales (CharField): El nombre de la sucursal.
        direccion_sucursales (CharField): La dirección física de la sucursal.
    """

    nombre_sucursales = models.CharField(max_length=100)
    direccion_sucursales = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre_sucursales}, {self.direccion_sucursales}'
 



