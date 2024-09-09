from django.urls import path

from . import views

app_name = 'producto'


urlpatterns = [
    path('', views.index, name='index'),
    path('producto/list', views.producto_list, name='producto_list'),
    path('producto/create', views.producto_create, name='producto_create'),
    path('producto/detalle/<int:pk>',views.producto_detalle,name='producto_detalle'),
]


