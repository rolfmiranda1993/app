from django.urls import path
from . import views

urlpatterns = [
    path('',views.tarea_views, name = 'tareas'),
    path('add_tarea/',views.add_tarea_views, name = 'AddTarea'),
    path('edit_tarea/',views.edit_tarea_views, name = 'EditTarea'),
    path('delete_tarea/',views.delete_tarea_views, name = 'DeleteTarea'),
]