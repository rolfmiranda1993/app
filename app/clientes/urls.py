from django.urls import path
from . import views

urlpatterns = [
    path('',views.cliente_views, name = 'clientes'),
    path('add_cliente/',views.add_cliente_views, name = 'AddCliente'),
    path('edit_cliente',views.edit_cliente_views, name = 'EditCliente'),
    path('delete_cliente',views.delete_cliente_views, name = 'DeleteCliente'),
]