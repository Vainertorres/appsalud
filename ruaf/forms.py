from django.forms import *
from django import forms 

from .models import Nacido_vivo, SeguimientoBajoPeso, FileNacidoVivo

class Report_nacido_vivo_Form(Form):
	date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))


class Nacido_vivo_Form(forms.ModelForm):
    class Meta:
        model = Nacido_vivo
        fields = ['nrocertificado','departamento', 'municipio','madre','peso','talla', \
        'fechanac','sexo','ips', 'tipo_parto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #para que se inicialice
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({                
            'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
            })

class Seg_nv_Bajo_Peso_Form(forms.ModelForm):
    class Meta:
        model = SeguimientoBajoPeso
        fields=['nacido_vivo','fecha','hallazgos','educacion','icbf','nutricionista', 'peso','talla','perimetro_cefalico', \
        'perimetro_toraxico']
        exclude=['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs) #para que se inicialice
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({                
                    'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
                })
            self.fields['fecha'].widget.attrs['readonly'] = True

class FileNacidoVivoForm(forms.ModelForm):
    class Meta:
        model = FileNacidoVivo
        fields = ['nacido_vivo','descripcion','archivo']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #para que se inicialice
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({                
                'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
                
            })


