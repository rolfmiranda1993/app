from django.contrib import admin
from clientes.models import cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_de_la_empresa','numero_de_ruc','nombre_del_nexo',
    'telefono_del_nexo','mail_del_nexo','nombre_contacto_pagos','telefono_contacto_pagos',
    'mail_contacto_pagos','fecha_de_vinculacion','notas_adicionales','forma_de_pago_habitual',
    'banco','titular_de_la_cuenta','tipo_de_cuenta','numero_de_cuenta',
    'documento_de_cuenta')
    search_fields = ('nombre_de_la_empresa','numero_de_ruc','nombre_del_nexo',
    'nombre_contacto_pagos','banco','titular_de_la_cuenta')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(cliente, ClienteAdmin)