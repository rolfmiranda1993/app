from django.contrib import admin
from egresos.models import egresos

# Register your models here.
class EgresoAdmin(admin.ModelAdmin):
    list_display = ('rubro','forma_de_pago','tipo_de_pago','nombre_de_pago','titular_de_pago','monto_de_pago','responsable' )
    search_fields = ('rubro','nombre_de_pago','titular_de_pago')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(egresos, EgresoAdmin)