from django.contrib import admin
from miembro.models import miembro

# Register your models here.
class MiembroAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','nacionalidad','numero_de_documento',
    'fecha_de_nacimiento','telefono_particular','telefono_corporativo',
    'mail_particular','mail_corporativo','fecha_de_ingreso','fecha_de_salida','motivo_de_salida',
    'cargo','contribuyente_set','estado_civil','hijos','genero')
    search_fields = ('nombres','apellidos','numero_de_documento')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(miembro, MiembroAdmin)