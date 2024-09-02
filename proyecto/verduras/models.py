from django.db import models

class Verduras(models.Model):
    """
    El modelo Verduras representa diferentes tipos de verduras disponibles en la verdulería.

    Atributos:
        nombre_verduras (CharField): El nombre de la verdura, debe ser único para evitar duplicados.
        kilo_verduras (IntegerField): La cantidad de kilos de esta verdura.
        monto_verduras (DecimalField): El precio por kilo de la verdura en pesos.
    """




    nombre_verduras = models.CharField(max_length=50, unique=True)
    kilo_verduras=models.IntegerField()
    monto_verduras= models.DecimalField(max_digits=10, decimal_places=2)


                  
    def __str__(self):
        return f'{self.nombre_verduras}, {self.kilo_verduras} kilo,{self.monto_verduras} pesos'





