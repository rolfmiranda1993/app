from django.db import models

# Create your models here.
class departamentos(models.Model):
    nivel_jerarquia=(
        (u'1',u'1'),
        (u'2',u'2'),
        (u'3',u'3'),
        (u'4',u'4'),
        (u'5',u'5'),
        (u'6',u'6'),
        )
    nombre = models.CharField(max_length=200, null=True, blank=True)
    jerarquia = models.CharField(max_length=20, choices=nivel_jerarquia)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'departamentos'
        Verbose_name_plural = 'departamentos'
        order_with_respect_to = 'jerarquia'
    
    def ___str__(self):
        return self.nombre
