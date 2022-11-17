from django.urls import path
from . import views

urlpatterns = [
    path('',views.rubros_views, name = 'rubros'),
    path('add_rubro/',views.add_rubros_views, name = 'AddRubro'),
    path('edit_rubro/',views.edit_rubros_views, name = 'EditRubro'),
    path('delete_rubro/',views.delete_rubros_views, name = 'DeleteRubro'),
]