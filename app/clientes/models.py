from django.db import models

# Create your models here.
class cliente(models.Model):
    pagos =((u'1',u'Efectivo'),
    (u'2',u'Cheque'),
    (u'3',u'Transferencia'),
    (u'4',u'Deposito'),
    )
    nombre_de_la_empresa = models.CharField(max_length=250, null=True, blank=True)
    numero_de_ruc = models.CharField(max_length=250, null=True, blank=True)
    nombre_del_nexo = models.CharField(max_length=250, null=True, blank=True)
    telefono_del_nexo = models.CharField(max_length=250, null=True, blank=True)
    mail_del_nexo = models.CharField(max_length=250, null=True, blank=True)
    nombre_contacto_pagos = models.CharField(max_length=250, null=True, blank=True)
    telefono_contacto_pagos = models.CharField(max_length=250, null=True, blank=True)
    mail_contacto_pagos = models.CharField(max_length=250, null=True, blank=True)
    fecha_de_vinculacion = models.CharField(max_length=50, null=True, blank=True)
    notas_adicionales = models.CharField(max_length=250, null=True, blank=True)
    forma_de_pago_habitual = models.CharField(max_length=20, choices=pagos)
    banco = models.CharField(max_length=250, null=True, blank=True)
    titular_de_la_cuenta = models.CharField(max_length=250, null=True, blank=True)
    tipo_de_cuenta = models.CharField(max_length=250, null=True, blank=True)
    numero_de_cuenta = models.CharField(max_length=250, null=True, blank=True)
    documento_de_cuenta = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'cliente'
        Verbose_name_plural = 'clientes'
        order_with_respect_to = 'nombre_de_la_empresa'
    
    def ___str__(self):
        return str(self.nombre_de_la_empresa) + ' - ' + self.numero_de_ruc
