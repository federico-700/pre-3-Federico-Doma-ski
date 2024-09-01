from django.db import models

# Create your models here.


from django.db import models


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

