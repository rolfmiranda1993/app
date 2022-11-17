from django.urls import path
from . import views

urlpatterns = [
    path('',views.departamentos_views, name = 'departamentos'),
    path('add_departamento/',views.add_departamentos_views, name = 'AddDepartamento'),
    path('edit_departamento/',views.edit_departamentos_views, name = 'EditDepartamento'),
    path('delete_departamento/',views.delete_departamentos_views, name = 'DeleteDepartamento'),
]
