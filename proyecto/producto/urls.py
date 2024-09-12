from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'producto'


urlpatterns = [
    path('', views.index, name='index'),
    path('producto/list', login_required(views.producto_list), name='producto_list'),
    path('producto/create', login_required(views.producto_create), name='producto_create'), 
    path('producto/update/<int:pk>',login_required(views.producto_update),name='producto_update'),

    path('producto/detalle/<int:pk>',login_required(views.ProductoDetail.as_view()),name='producto_detalle'),
    path('producto/beneficio/<int:pk>',login_required(views.ProductoBeneficio.as_view()),name='producto_beneficio'),
    path('producto/delete/<int:pk>',login_required(views.ProductoDelete.as_view()),name='producto_delete'),
]


