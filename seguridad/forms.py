import json
from django.forms import *
from django.forms import inlineformset_factory

from cnf.models import Paciente
from .models import Casos, Afectados, Organismos_atiende

class SeguridadForm(ModelForm):
	
	class Meta:
		model = Casos
		fields=['fecha', 'descripcion', 'direccion', 'lat', 'lon', 'departamento', \
		'municipio','barrio','acciones']
		
		exclude=['um','fm','uc','fc']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if field.lower() == "descripcion".lower():
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"4"
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})

		self.fields['fecha'].widget.attrs['readonly'] = True


class AfectadosForm(ModelForm):

	class Meta:
		model=Afectados
		fields=['paciente','estadofinal']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			if field.lower() == "paciente".lower():
				self.fields[field].widget.attrs.update({				
				'class':"form-control paciente" #colocar la clase de bootsTrap a todos los controles o campos

				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})

		i = 0
		lista = []
		cant_reg = 0
		dato = ""

		if self.instance.id:
			sqlpac = Afectados.objects.filter(pk = self.instance.id)
			for x in sqlpac:
				lista.append(x.paciente_id)
			paci = Paciente.objects.all().filter(id__in = lista)
			
			self.fields['paciente'].queryset = paci
		else:
			self.fields['paciente'].queryset = Paciente.objects.none() 
			
			#pasar un diccionario a formato Json
			prueba = json.dumps(self.data)
			resultado = json.loads(prueba)
			

			if 'afectados-TOTAL_FORMS' in resultado:	
				cant_reg = resultado['afectados-TOTAL_FORMS']
				cant_reg = int(cant_reg)
				
				
				while i < cant_reg:
					dato = 'afectados-{}-paciente'.format(i)
					
					i = i + 1
					if dato in resultado:
						idpac = resultado[dato]
						if not (idpac == ''):
							lista.append(idpac)
				
				if len(lista) > 0:
					paci = Paciente.objects.all().filter(id__in = lista)
					self.fields['paciente'].queryset = paci
					



class OrganismosForm(ModelForm):
	class Meta:
		model=Organismos_atiende
		fields=['organismo_de_socorro','descripcion']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			if field.lower() == "descripcion".lower():
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"3"
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control pr" #colocar la clase de bootsTrap a todos los controles o campos
				})


AfectadosFormSet = inlineformset_factory(
    Casos, Afectados, form=AfectadosForm,
    extra=1, can_delete=True, can_delete_extra=True
)		

OrganismosFormSet = inlineformset_factory(
    Casos, Organismos_atiende, form=OrganismosForm,
    extra=1, can_delete=True, can_delete_extra=True
)	