from django.urls import path
from . import views

urlpatterns = [
    path('',views.ingresos_views, name = 'ingresos'),
    path('add_ingreso/',views.add_ingresos_views, name = 'AddIngreso'),
    path('edit_ingreso/',views.edit_ingresos_views, name = 'EditIngreso'),
    path('delete_ingreso/',views.delete_ingresos_views, name = 'DeleteIngreso'),
]