from django.db import models
from rubro.models import rubro
from clientes.models import cliente

# Create your models here.
class ingresos(models.Model):
    rubro = models.ForeignKey(rubro, on_delete=models.SET_NULL,null=True,related_name='rubroIngreso')
    forma_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    tipo_de_cobro = models.CharField(max_length=200, unique=True, null=True, blank=True)
    nombre_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    titular_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    monto_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    responsable = models.ForeignKey(cliente, on_delete=models.SET_NULL,null=True,related_name='clienteIngreso')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'ingresos'
        Verbose_name_plural = 'ingresos'
        order_with_respect_to = 'rubro'
    
    def ___str__(self):
        return self.rubro