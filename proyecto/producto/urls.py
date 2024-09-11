from django.urls import path

from . import views

app_name = 'producto'


urlpatterns = [
    path('', views.index, name='index'),
    path('producto/list', views.producto_list, name='producto_list'),
    path('producto/create', views.producto_create, name='producto_create'), 
    path('producto/update/<int:pk>',views.producto_update,name='producto_update'),

    path('producto/detalle/<int:pk>',views.ProductoDetail.as_view(),name='producto_detalle'),
    path('producto/beneficio/<int:pk>',views.ProductoBeneficio.as_view(),name='producto_beneficio'),
    path('producto/delete/<int:pk>',views.ProductoDelete.as_view(),name='producto_delete'),
]


