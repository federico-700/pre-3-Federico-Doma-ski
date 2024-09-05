from django.db import models

class Producto(models.Model):
    class Tipo_producto(models.TextChoices):
        Fruta = "FRUTA", "Fruta"
        VERDURA = "VERDURA", "verdura"
        OFERTA = "OFERTA", "Oferta"
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    kilo_producto = models.DecimalField(max_digits=10, decimal_places=2)
    stock_producto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_producto = models.CharField(max_length=20, choices=Tipo_producto.choices)


    
    def __str__(self):
        return f'{self.nombre_producto}, {self.kilo_producto} kilo,{self.precio_producto} pesos, stock disponible {self.stock_producto} kilos {self.tipo_producto}'
