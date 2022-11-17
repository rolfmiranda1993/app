from django.urls import path
from . import views

urlpatterns = [
    path('',views.miembro_views, name = 'miembro'),
    path('add_miembro/',views.add_miembro_views, name = 'AddMiembro'),
    path('edit_miembro',views.edit_miembro_views, name = 'EditMiembro'),
    path('delete_miembro',views.delete_miembro_views, name = 'DeleteMiembro'),
]