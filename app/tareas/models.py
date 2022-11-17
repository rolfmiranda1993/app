from django.db import models
from miembro.models import miembro
# Create your models here.
#class tareaModel(models.Model):
#    tarea_fields = models.CharField(max_length=200)

"""
class colaborador(models.Model):
    nombres = models.CharField(max_length=200, null=True, blank=False)
    apellidos = models.CharField(max_length=200, unique=True, null=True, blank=True)

    def nombre_completo(self):
        return "{} {}".format(self.nombres,self.apellidos)

    def ___str__(self):
        return self.nombre_completo()
    
    class meta:
        Verbose_name = 'colaborador'
        Verbose_name_plural = 'colaboradores'
        db_table='Colaboradores'
        ordering = ['apellidos','nombres']
"""

class tarea(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.CharField(max_length=200, unique=True, null=True, blank=True)
    fecha_entrega = models.DateField(default='dd/mm/aaaa')
    hora_entrega = models.TimeField(default='hh:mm')
    responsable = models.ForeignKey(miembro, on_delete=models.SET_NULL,null=True,related_name='miembro')
    created = models.DateTimeField(auto_now_add=True)
    created_hour = models.TimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'tarea'
        Verbose_name_plural = 'tareas'
        order_with_respect_to = 'fecha_entrega'
   
    def ___str__(self):
        return str(self.nombre)
