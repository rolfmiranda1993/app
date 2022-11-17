from django import forms
from departamentos.models import departamentos

class AddDepartamentoForm(forms.ModelForm):
    class Meta:
        model = departamentos
        fields = ('nombre','jerarquia',)
        labels = {
            'nombre' : 'Nombre: ',
            'jerarquia' : 'Jerarquia: ',            
        }
class EditDepartamentoForm(forms.ModelForm):
    class Meta:
        model = departamentos
        fields = ('nombre','jerarquia',)
        labels = {
            'nombre' : 'Nombre: ',
            'jerarquia' : 'Jerarquia: ',            
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'type':'text','id' : 'nombre_editar'}),
            'jerarquia' : forms.Select(attrs={'id' : 'jerarquia_editar'}),            
        }
