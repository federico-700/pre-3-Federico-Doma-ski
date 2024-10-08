from django.db import models

class Producto(models.Model):
    """
    Modelo que representa un producto en la verdulería.
    Los productos pueden ser frutas, verduras o estar en oferta.
    Cada producto tiene un nombre, precio, stock y detalles opcionales.
    """
    class Tipo_producto(models.TextChoices):
        FRUTA = "FRUTA", "Fruta"
        VERDURA = "VERDURA", "Verdura"
        OFERTA = "OFERTA", "Oferta"
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    kilo_producto = models.DecimalField(max_digits=10, decimal_places=2)
    stock_producto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_producto = models.CharField(max_length=20, choices=Tipo_producto.choices)
    detalle_producto = models.TextField(blank=True, null=True)
    beneficio_producto = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.nombre_producto}, {self.kilo_producto} kilo,{self.precio_producto} pesos, stock disponible {self.stock_producto} kilos {self.tipo_producto}'

    

    def disminuir_stock(self, cantidad):
        """cantidad es enviado desde el modelo Venta"""
        if self.stock_producto >= cantidad:
            self.stock_producto -= cantidad
            self.save()
        else:
            raise ValueError('No hay suficiente stock disponible')

    def aumentar_stock(self, cantidad):
        self.stock_producto += cantidad
        self.save()



    
