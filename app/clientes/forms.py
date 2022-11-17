from django import forms
from .models import cliente

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ('nombre_de_la_empresa','numero_de_ruc','nombre_del_nexo','telefono_del_nexo','mail_del_nexo','nombre_contacto_pagos','telefono_contacto_pagos','mail_contacto_pagos','fecha_de_vinculacion','notas_adicionales','forma_de_pago_habitual','banco','titular_de_la_cuenta','tipo_de_cuenta','numero_de_cuenta','documento_de_cuenta')
        labels = {
            'nombre_de_la_empresa' : 'Empresa: ',
            'numero_de_ruc' : 'RUC: ',
            'nombre_del_nexo' : 'Nexo°: ',
            'telefono_del_nexo' : 'Tel. Nexo: ',
            'mail_del_nexo' : 'Mail Nexo: ',
            'nombre_contacto_pagos' : 'Contacto Pagos: ',
            'telefono_contacto_pagos' : 'Telefono Pagos: ',
            'mail_contacto_pagos' : 'Mail Pagos: ',
            'fecha_de_vinculacion' : 'Vinculación: ',
            'notas_adicionales' : 'Notas Adicionales: ',
            'forma_de_pago_habitual' : 'Forma de Pago: ',
            'banco': 'Banco: ',
            'titular_de_la_cuenta' : 'Titular: ',            
            'tipo_de_cuenta' : 'Tipo de Cuenta: ',
            'numero_de_cuenta' : 'N° de Cuenta: ',
            'documento_de_cuenta' : 'Documento de Cuenta: '
        }

class EditClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields= ('nombre_de_la_empresa','numero_de_ruc','nombre_del_nexo','telefono_del_nexo','mail_del_nexo','nombre_contacto_pagos','telefono_contacto_pagos','mail_contacto_pagos','fecha_de_vinculacion','notas_adicionales','forma_de_pago_habitual','banco','titular_de_la_cuenta','tipo_de_cuenta','numero_de_cuenta','documento_de_cuenta')
        labels = {
            'nombre_de_la_empresa' : 'Empresa: ',
            'numero_de_ruc' : 'RUC: ',
            'nombre_del_nexo' : 'Nexo°: ',
            'telefono_del_nexo' : 'Tel. Nexo: ',
            'mail_del_nexo' : 'Mail Nexo: ',
            'nombre_contacto_pagos' : 'Contacto Pagos: ',
            'telefono_contacto_pagos' : 'Telefono Pagos: ',
            'mail_contacto_pagos' : 'Mail Pagos: ',
            'fecha_de_vinculacion' : 'Vinculación: ',
            'notas_adicionales' : 'Notas Adicionales: ',
            'forma_de_pago_habitual' : 'Forma de Pago: ',
            'banco': 'Banco: ',
            'titular_de_la_cuenta' : 'Titular: ',            
            'tipo_de_cuenta' : 'Tipo de Cuenta: ',
            'numero_de_cuenta' : 'N° de Cuenta: ',
            'documento_de_cuenta' : 'Documento de Cuenta: '
        }
        widgets = {
            'nombre_de_la_empresa' : forms.TextInput(attrs={'type' : 'text', 'id' : 'nombre_de_la_empresa_editar'}),
            'numero_de_ruc' : forms.TextInput(attrs={ 'id' : 'numero_de_ruc_editar'}),
            'nombre_del_nexo' : forms.TextInput(attrs={ 'id' : 'nombre_del_nexo_editar'}),
            'telefono_del_nexo' : forms.TextInput(attrs={ 'id' : 'telefono_del_nexo_editar'}),
            'mail_del_nexo' : forms.TextInput(attrs={ 'id' : 'mail_del_nexo_editar'}),
            'nombre_contacto_pagos' : forms.TextInput(attrs={ 'id' : 'nombre_contacto_pagos_editar'}),
            'telefono_contacto_pagos' : forms.TextInput(attrs={ 'id' : 'telefono_contacto_pagos_editar'}),
            'mail_contacto_pagos' : forms.TextInput(attrs={ 'id' : 'mail_contacto_pagos_editar'}),
            'fecha_de_vinculacion' : forms.TextInput(attrs={ 'id' : 'fecha_de_vinculacion_editar'}),
            'notas_adicionales' : forms.TextInput(attrs={ 'id' : 'notas_adicionales_editar'}),
            'forma_de_pago_habitual' : forms.TextInput(attrs={ 'id' : 'forma_de_pago_habitual_editar'}),
            'banco': forms.TextInput(attrs={ 'id' : 'banco_editar'}),
            'titular_de_la_cuenta' : forms.TextInput(attrs={ 'id' : 'titular_de_la_cuenta_editar'}),            
            'tipo_de_cuenta' : forms.TextInput(attrs={ 'id' : 'tipo_de_cuenta_editar'}),
            'numero_de_cuenta' : forms.TextInput(attrs={ 'id' : 'numero_de_cuenta_editar'}),
            'documento_de_cuenta' : forms.TextInput(attrs={ 'id' : 'documento_de_cuenta_editar'}),            
        }