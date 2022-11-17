from django import forms
from egresos.models import egresos

class AddEgresoForm(forms.ModelForm):
    class Meta:
        model = egresos
        fields = ('rubro','forma_de_pago','tipo_de_pago','nombre_de_pago','titular_de_pago','monto_de_pago','responsable',)
        labels = {
            'rubro' : 'Rubro: ',
            'forma_de_pago' : 'Forma de Pago: ',
            'tipo_de_pago' : 'Tipo de Pago: ',
            'nombre_de_pago' : 'Nombre de Pago: ',
            'titular_de_pago' : 'Titular de Pago: ',
            'monto_de_pago' : 'Monto de Pago: ',
            'responsable' : 'Responsable: ',
        }

class EditEgresoForm(forms.ModelForm):
    class Meta:
        model = egresos
        fields = ('rubro','forma_de_pago','tipo_de_pago','nombre_de_pago','titular_de_pago','monto_de_pago','responsable',)
        labels = {
            'rubro' : 'Rubro: ',
            'forma_de_pago' : 'Forma de Pago: ',
            'tipo_de_pago' : 'Tipo de Pago: ',
            'nombre_de_pago' : 'Nombre de Pago: ',
            'titular_de_pago' : 'Titular de Pago: ',
            'monto_de_pago' : 'Monto de Pago: ',
            'responsable' : 'Responsable: ',
        }
        widgets = {
            'rubro' : forms.Select(attrs={'type':'text','id' : 'rubro_editar'}),
            'forma_de_pago' : forms.TextInput(attrs={'id' : 'forma_de_pago_editar'}),
            'tipo_de_pago' : forms.TextInput(attrs={'id' : 'tipo_de_pago_editar'}),
            'nombre_de_pago' : forms.TextInput(attrs={'id' : 'nombre_de_pago_editar'}),
            'titular_de_pago' : forms.TextInput(attrs={'id' : 'titular_de_pago_editar'}),
            'monto_de_pago' : forms.TextInput(attrs={'id' : 'monto_de_pago_editar'}),
            'responsable' : forms.Select(attrs={'id' : 'responsable_editar'}),
        }