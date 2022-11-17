from django.db import models
from departamentos.models import departamentos

# Create your models here.
class rubro(models.Model):
    area = models.ForeignKey(departamentos, on_delete=models.SET_NULL,null=True,related_name='departamentos')
    nombre = models.CharField(max_length=200, unique=True, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'rubro'
        Verbose_name_plural = 'rubros'
        #order_with_respect_to = 'nombre'
    
    def ___str__(self):
        return self.nombre