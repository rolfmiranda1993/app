from django import forms
from tareas.models import tarea

class AddTareaForm(forms.ModelForm):
    class Meta:
        model = tarea
        fields = ('nombre','descripcion','fecha_entrega','hora_entrega','responsable',)
        labels = {
            'nombre' : 'Nombre: ',
            'descripcion' : 'Descripción: ',
            'fecha_entrega' : 'Fecha de Entrega: ',
            'hora_entrega' : 'Hora de Entrega',
            'responsable' : 'Responsable: ',
        }
class EditTareaForm(forms.ModelForm):
    class Meta:
        model = tarea
        fields = ('nombre','descripcion','fecha_entrega','hora_entrega','responsable',)
        labels = {
            'nombre' : 'Nombre: ',
            'descripcion' : 'Descripción: ',
            'fecha_entrega' : 'Fecha de Entrega: ',
            'hora_entrega' : 'Hora de Entrega',
            'responsable' : 'Responsable: ',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'type':'text','id' : 'nombre_editar'}),
            'descripcion' : forms.TextInput(attrs={'id' : 'descripcion_editar'}),
            'fecha_entrega' : forms.DateInput(attrs={'id' : 'fecha_entrega_editar'}),
            'hora_entrega' : forms.TimeInput(attrs={'id' : 'hora_entrega_editar'}),
            'responsable' : forms.Select(attrs={'id' : 'responsable_editar'}),
        }
