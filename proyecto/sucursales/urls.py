from django.urls import path

from . import views

app_name = 'sucursales'


urlpatterns = [
    path('', views.index, name='index'),
    path('sucursales/list', views.sucursales_list, name='sucursales_list'),
    path('sucursales/create', views.sucursales_create, name='sucursales_create'),
]
