from django.urls import path

from . import views

app_name = 'verduras'


urlpatterns = [
    path('', views.index, name='index'),
    path('verduras/list', views.verduras_list, name='verduras_list'),
    path('verduras/create', views.verduras_create, name='verduras_create'),

]