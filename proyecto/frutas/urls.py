from django.urls import path

from . import views

app_name = 'frutas'


urlpatterns = [
    path('', views.index, name='index'),
    path('frutas/list', views.frutas_list, name='frutas_list'),
    path('frutas/create', views.frutas_create, name='frutas_create'),
]

