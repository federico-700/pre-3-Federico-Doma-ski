from django.db import models


class Sucursales(models.Model):
    nombre_sucursales = models.CharField(max_length=100)
    direccion_sucursales = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre_sucursales}, {self.direccion_sucursales}'
 



