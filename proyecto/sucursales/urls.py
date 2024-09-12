from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'sucursales'


urlpatterns = [
    path('', views.index, name='index'),
    path('sucursales/list', login_required(views.sucursales_list), name='sucursales_list'),
    path('sucursales/create', login_required(views.sucursales_create), name='sucursales_create'),
]
