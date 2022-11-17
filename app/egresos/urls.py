from django.urls import path
from . import views

urlpatterns = [
    path('',views.egresos_views, name = 'egresos'),
    path('add_egreso/',views.add_egresos_views, name = 'AddEgreso'),
    path('edit_egreso/',views.edit_egresos_views, name = 'EditEgreso'),
    path('delete_egreso/',views.delete_egresos_views, name = 'DeleteEgreso'),
]