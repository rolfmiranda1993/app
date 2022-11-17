from django.contrib import admin
from roles.models import roles

# Register your models here.
class RolesAdmin(admin.ModelAdmin):
    list_display = ('empleado_o_proveedor','nombre_de_area')
    search_fields = ('empleado_o_proveedor','nombre_de_area')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(roles, RolesAdmin)