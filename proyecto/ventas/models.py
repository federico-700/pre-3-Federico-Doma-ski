from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from decimal import Decimal

class Vendedor(models.Model):
    """
    Modelo que representa a un vendedor en la plataforma.
    Cada vendedor está asociado a un usuario de Django (OneToOneField).
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendedor')
    celular = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


###########################


class Comprador(models.Model):
    """
    Modelo que representa a un comprador en la plataforma.
    Cada comprador está asociado a un usuario de Django (OneToOneField).
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='comprador')
    celular = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)


    class Meta:
        verbose_name = 'Comprador'
        verbose_name_plural = 'Compradores'


    def __str__(self):
        return self.usuario.username

###############################


class Venta(models.Model):
    id: int
    """
    Modelo que representa una venta realizada en la plataforma.
    Una venta está asociada a un comprador, un vendedor y un producto.
    
    Atributos:
    - comprador: El comprador que realizó la compra (ForeignKey a Comprador).
    - vendedor: El vendedor que vendió el producto (ForeignKey a Vendedor).
    - producto: El producto que se vendió (ForeignKey a Producto).
    - cantidad: La cantidad de producto vendida.
    - precio_total: El precio total de la venta calculado automáticamente( si compra 10 o mas kilos obtiene un descuento del 20%)
    - fecha_venta: Fecha en la que se realizó la venta (se asigna automáticamente).
    """

    comprador = models.ForeignKey(Comprador, on_delete=models.DO_NOTHING, blank=True, null=True )
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey('producto.Producto', on_delete=models.DO_NOTHING)
    cantidad = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'Venta {self.id} - {self.producto.nombre_producto} x {self.cantidad}'

    class Meta:
        ordering = ['-fecha_venta']

    def clean(self):
        if not self.producto:
            raise ValidationError('El producto no existe')
        if self.producto.stock_producto == 0:
            raise ValidationError('No hay stock disponible para este producto')
        if self.cantidad > self.producto.stock_producto:
            raise ValidationError(
                f'No hay suficiente stock disponible para vender {self.cantidad} unidades.'
                f'Solo hay {self.producto.stock_producto} unidades disponibles.'
            )

    def save(self, *args, **kwargs):
        if self.cantidad >= 10:
            self.precio_total = self.producto.precio_producto *Decimal('0.8')* self.cantidad
        else:
            self.precio_total = self.producto.precio_producto*self.cantidad

        self.producto.disminuir_stock(self.cantidad)
        super().save(*args, **kwargs)



