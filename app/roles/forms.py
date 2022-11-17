from django import forms
from roles.models import roles

class AddRolesForm(forms.ModelForm):
    class Meta:
        model = roles
        fields = ('empleado_o_proveedor','nombre_de_area',)
        labels = {
            'empleado_o_proveedor' : 'Empreado/Proveedor: ',
            'nombre_de_area' : 'Nombre de Área: ',
        }

class EditRolesForm(forms.ModelForm):
    class Meta:
        model = roles
        fields = ('empleado_o_proveedor','nombre_de_area',)
        labels = {
            'empleado_o_proveedor' : 'Empreado/Proveedor: ',
            'nombre_de_area' : 'Nombre de Área: ',
        }
        widgets = {
            'empleado_o_proveedor' : forms.Select(attrs={'type' : 'text','id' : 'empleado_o_proveedor_editar'}),
            'nombre_de_area' : forms.Select(attrs={'id' : 'nombre_de_area_editar'}),
        }