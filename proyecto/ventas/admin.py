from django.contrib import admin

# Register your models here.
from .models import Vendedor, Venta

admin.site.register(Vendedor)


#@admin.register(Venta)
#class VentaAdmin(admin.ModelAdmin):
##    list_display = ('vendedor', 'producto', 'cantidad', 'precio_total',)
#    list_display_links = ('producto',)
#    search_fields = ("producto__nombre_producto")
#    list_filter = ('vendedor',)
    



@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'producto', 'cantidad', 'precio_total', 'fecha_venta')
    list_display_links = ('producto',)
    search_fields = ["producto__nombre_producto", "vendedor__usuario__username", "vendedor__usuario__first_name", "vendedor__usuario__last_name"]  # Cambiar a lista
    list_filter = ("vendedor",)
    date_hierarchy = 'fecha_venta'

