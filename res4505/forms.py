from django import forms 


from .models import Periodo_envio, Resolucion4505ctrl

class PeriodoreporteForm(forms.ModelForm):
	class Meta:
		model = Periodo_envio
		fields=['codigo','descripcion','fechaini','fechafin','fechainiplazo','fechafinplazo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})
		self.fields['fechaini'].widget.attrs['readonly'] = True
		self.fields['fechafin'].widget.attrs['readonly'] = True
		self.fields['fechainiplazo'].widget.attrs['readonly'] = True
		self.fields['fechafinplazo'].widget.attrs['readonly'] = True


class Resolucion4505ctrlForm(forms.ModelForm):
	class Meta:
		model = Resolucion4505ctrl
		fields=['tiporegistro','codigoentidad','eps','municipio','departamento','fechainicial', \
		'fechafinal', 'nrototalreg','actual']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})
		self.fields['tiporegistro'].widget.attrs['readonly'] = True			
		self.fields['fechainicial'].widget.attrs['readonly'] = True
		self.fields['fechafinal'].widget.attrs['readonly'] = True

		