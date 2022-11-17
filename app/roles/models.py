from django.db import models
from clientes.models import cliente
from departamentos.models import departamentos

# Create your models here.
class roles(models.Model):
    empleado_o_proveedor = models.ForeignKey(cliente, on_delete=models.SET_NULL,null=True,related_name='clienteRol')
    nombre_de_area = models.ForeignKey(departamentos, on_delete=models.SET_NULL,null=True,related_name='departamentoRol')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'roles'
        Verbose_name_plural = 'roles'
        order_with_respect_to = 'empleado_o_proveedor'
    
    def ___str__(self):
        return str(self.empleado_o_proveedor)