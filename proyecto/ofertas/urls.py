from django.urls import path

from . import views

app_name = 'ofertas'


urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas/list', views.ofertas_list, name='ofertas_list'),
    path('ofertas/create', views.ofertas_create, name='ofertas_create'),
]


