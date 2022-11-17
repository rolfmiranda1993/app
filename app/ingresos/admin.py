from django.contrib import admin
from ingresos.models import ingresos

# Register your models here.

class IngresoAdmin(admin.ModelAdmin):
    list_display = ('rubro','forma_de_pago','tipo_de_cobro','nombre_de_pago','titular_de_pago','monto_de_pago','responsable' )
    search_fields = ('rubro','nombre_de_pago','titular_de_pago')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ingresos, IngresoAdmin)