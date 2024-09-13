from django.contrib import admin
from .models import Producto

#admin.site.register(Producto)


# personalizar panel de control
from . import models


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre_producto","kilo_producto","precio_producto","stock_producto")
    search_fields = ("nombre_producto",)







    