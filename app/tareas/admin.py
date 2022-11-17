from django.contrib import admin
from tareas.models import tarea
# Register your models here.
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','fecha_entrega','hora_entrega','responsable', )
    search_fields = ('nombre','descripcion','fecha_entrega')
    readonly_fields = ('created','created_hour', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(tarea, TareaAdmin)