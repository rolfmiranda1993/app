from django import forms
from miembro.models import miembro

class AddMiembroForm(forms.ModelForm):
    class Meta:
        model = miembro
        fields = ('nombres','apellidos','numero_de_documento','fecha_de_nacimiento','telefono_particular','telefono_corporativo','mail_particular','mail_corporativo','fecha_de_ingreso','fecha_de_salida','motivo_de_salida','cargo','notas_adicionales','contribuyente_set','estado_civil','hijos','genero')
        labels = {
            'nombres' : 'Nombre: ',
            'apellidos' : 'Apellido: ',
            'numero_de_documento' : 'C.I.N°: ',
            'fecha_de_nacimiento' : 'Fecha de Nacimiento: ',
            'telefono_particular' : 'Tel. Particular: ',
            'telefono_corporativo' : 'Tel. Corporativo: ',
            'mail_particular' : 'Mail Particular: ',
            'mail_corporativo' : 'Mail Corporativo: ',
            'fecha_de_ingreso' : 'Fecha de Ingreso: ',
            'fecha_de_salida' : 'Fecha de Salida: ',
            'motivo_de_salida': 'Motivo de Salida: ',
            'cargo' : 'Cargo: ',
            'notas_adicionales' : 'Notas Adicionales: ',
            'contribuyente_set' : 'SET: ',
            'estado_civil' : 'Estado Civil: ',
            'hijos' : 'Hijo/s: ',
            'genero': 'Genero: '
        }

class EditMiembroForm(forms.ModelForm):
    class Meta:
        model = miembro
        fields = ('nombres','apellidos','numero_de_documento','fecha_de_nacimiento','telefono_particular','telefono_corporativo','mail_particular','mail_corporativo','fecha_de_ingreso','fecha_de_salida','motivo_de_salida','cargo','notas_adicionales','contribuyente_set','estado_civil','hijos','genero')
        labels = {
            'nombres' : 'Nombre: ',
            'apellidos' : 'Apellido: ',
            'numero_de_documento' : 'C.I.N°: ',
            'fecha_de_nacimiento' : 'Fecha de Nacimiento: ',
            'telefono_particular' : 'Tel. Particular: ',
            'telefono_corporativo' : 'Tel. Corporativo: ',
            'mail_particular' : 'Mail Particular: ',
            'mail_corporativo' : 'Mail Corporativo: ',
            'fecha_de_ingreso' : 'Fecha de Ingreso: ',
            'fecha_de_salida' : 'Fecha de Salida: ',
            'motivo_de_salida': 'Motivo de Salida: ',
            'cargo' : 'Cargo: ',
            'notas_adicionales' : 'Notas Adicionales: ',
            'contribuyente_set' : 'SET: ',
            'estado_civil' : 'Estado Civil: ',
            'hijos' : 'Hijo/s: ',
            'genero': 'Genero: '
        }
        widgets = {
            'nombres' : forms.TextInput(attrs={'type' : 'text', 'id' : 'nombre_editar'}),
            'apellidos' : forms.TextInput(attrs={ 'id' : 'apellido_editar'}),
            'numero_de_documento' : forms.TextInput(attrs={ 'id' : 'numero_de_documento_editar'}),
            'fecha_de_nacimiento' : forms.DateInput(attrs={ 'id' : 'fecha_de_nacimiento_editar'}),
            'telefono_particular' : forms.TextInput(attrs={ 'id' : 'telefono_particular_editar'}),
            'telefono_corporativo' : forms.TextInput(attrs={ 'id' : 'telefono_corporativo_editar'}),
            'mail_particular' : forms.TextInput(attrs={ 'id' : 'mail_particular_editar'}),
            'mail_corporativo' : forms.TextInput(attrs={ 'id' : 'mail_corporativo_editar'}),
            'fecha_de_ingreso' : forms.DateInput(attrs={ 'id' : 'fecha_de_ingreso_editar'}),
            'fecha_de_salida' : forms.DateInput(attrs={ 'id' : 'fecha_de_salida_editar'}),
            'motivo_de_salida': forms.TextInput(attrs={ 'id' : 'motivo_de_salida_editar'}),
            'cargo' : forms.TextInput(attrs={ 'id' : 'cargo_editar'}),
            'notas_adicionales' : forms.TextInput(attrs={ 'id' : 'notas_adicionales_editar'}),
            'contribuyente_set' : forms.TextInput(attrs={ 'id' : 'contribuyente_set_editar'}),
            'estado_civil' : forms.TextInput(attrs={ 'id' : 'estado_civil_editar'}),
            'hijos' : forms.TextInput(attrs={ 'id' : 'hijos_editar'}),
            'genero': forms.TextInput(attrs={ 'id' : 'genero_editar'})
        }
