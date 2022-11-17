from django.urls import path
from . import views

urlpatterns = [
    path('',views.roles_views, name = 'roles'),
    path('add_rol/',views.add_roles_views, name = 'AddRol'),
    path('edit_rol/',views.edit_roles_views, name = 'EditRol'),
    path('delete_rol/',views.delete_roles_views, name = 'DeleteRol'),
]