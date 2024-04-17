from django import forms
from django.forms import inlineformset_factory, ValidationError


from .models import Propietario, Establecimiento, ActaEstabEducativo, ItemActaEstabEducativo, Atiende_ActaEstabEduc, \
ActaEstEduFuncionario, Atiende_ActaEstabEduc, ActaGeneral, ActaGeneralFuncionarios, \
AtiendeActaGeneral, ActaEmbarcacionInter, Embarcaciones, ActaEmbarcacionInterFuncionarios, \
ActaEmbarcacionInterImo, ActaEmbarcacionInterPuerto, ActaBodegasPatios, ItemActaBodegasPatios, \
FuncionariosActaBodegasPatios, AtiendeActaBodegasPatios, ProductoQuimicoActaBodegasPatios, \
MedidaSanitariaActaBodegasPatios, TipoActa, Pregunta, ActaViviendaTransitoria, \
ItemActaViviendaTransitoria, FuncionariosActaViviendaTransitoria, AtiendeActaViviendaTransitoria, \
EvaluacionPregunta, ActaCentroCarcelario, ItemActaCentroCarcelario, \
FuncionariosActaCentroCarcelario, AtiendeActaCentroCarcelario, Concepto, ActaDrogueria, \
ItemActaDroguerias, FuncionariosActaDrogueria, AtiendeActaDrogueria


def filtrar_concepto_sanitario(idtipoacta):
	conceptosan = Concepto.objects.filter(tipoacta_id = idtipoacta).all()
	return conceptosan

class PropietarioForm(forms.ModelForm):

	class Meta:
		model = Propietario
		fields = ['tipodoc','nitcc','nombres','apellido1','apellido2','telfijo','telcelular', \
		'correoelectronico']
		

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})



class EstablecimientoForm(forms.ModelForm):
	class Meta:
		model = Establecimiento
		fields = ['nitcc','razonsocial','nroinscripcion','nombrecomercial','direccion','telefono', \
		'fax', 'nromatricula', 'departamento', 'municipio', 'lugarubica', 'correoelectronico', \
		'propietario', 'replegal', 'direccionotifica', 'dptonotifica', 'mpionotifica', \
		'horariofunciona', 'nrotrabajadores']
		

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})

class ActaEstabEducativoForm(forms.ModelForm):
	class Meta:
		model = ActaEstabEducativo
		fields=['fecha','nroacta','ciudad','establecimiento','nombrerector','tipodocrector','identificacionrector', \
		'nroestjormanhombres','nroestjormanmujeres','nroestjortarhombres','nroestjortarmujeres','nroestjornochombres', \
		'nroestjornocmujeres','nrodocenteshombres','nrodocentesmujeres','nroaulas','nropatios','nrocafeterias', \
		'fechaultinspeccion','nroactaultinspeccion','ultconcepto','motivovisita','concepto']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})
		self.fields['fecha'].widget.attrs['readonly'] = True


class ItemActaEstabEducativoForm(forms.ModelForm):
	tipoacta = TipoActa.objects.filter(idtipoacta='MISFO001').first()	

	class Meta:
		model = ItemActaEstabEducativo
		fields = ['pregunta','evaluacion','hallazgos','habilitada']

	def __init__(self, *args, **kwargs):		
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if field.lower() == "pregunta".lower():
				self.fields[field].widget.attrs.update({				
					'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos
					'rows':"1",				
					'readonly':True,
					'enable':False
					})
				
			else:
				if field.lower() == "hallazgos".lower():
					self.fields[field].widget.attrs.update({				
					'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
					'rows':"1",				
					})
				else:
					self.fields[field].widget.attrs.update({				
					'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
					})
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=self.tipoacta.pk)	


		
class ActaEstEduFuncionarioForm(forms.ModelForm):
	class Meta:
		model = ActaEstEduFuncionario
		fields=['funcionario']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})


class EmbarcacionInternacionalForm(forms.ModelForm):

	def clean_matricula(self):
		matricula = self.cleaned_data["matricula"]
		existe = Embarcaciones.objects.filter(matricula = matricula).exists()
		
		if existe:
			raise ValidationError('Esta matrícula de embarcación ya existe')

		return matricula


	class Meta:
		model = Embarcaciones
		fields=['matricula', 'nombre','pais']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})

class Atiende_ActaEstabEducForm(forms.ModelForm):
	class Meta:
		model= Atiende_ActaEstabEduc
		fields=['tipodoc','identificacion','nombre','institucion','cargo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})

class ActaGeneralForm(forms.ModelForm):
	class Meta:
		model = ActaGeneral
		fields = ['fecha','actividad','nroacta','municipio','establecimiento', 'tiposujeto', \
		'observacion','requerimiento','plazo','concepto']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if (field.lower() == "observacion".lower()) or (field.lower() == "requerimiento".lower()):
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"5",				
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				})

		self.fields['fecha'].widget.attrs['readonly'] = True		


class ActaGeneralFuncionariosForm(forms.ModelForm):
	class Meta:
		model = ActaGeneralFuncionarios
		fields = ['actageneral','funcionario']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actageneral'].widget.attrs['readonly'] = True	

class AtiendeActaGeneralForm(forms.ModelForm):
	class Meta:
		model = AtiendeActaGeneral
		fields = ['actageneral','tipodoc','identificacion','nombre','cargo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actageneral'].widget.attrs['readonly'] = True	


ActaGeneralFuncionariosFormSet = inlineformset_factory(
    ActaGeneral, ActaGeneralFuncionarios, form=ActaGeneralFuncionariosForm,
    extra=1, can_delete=True, can_delete_extra=True
)

AtiendeActaGeneralFormSet = inlineformset_factory(
    ActaGeneral, AtiendeActaGeneral, form=AtiendeActaGeneralForm,
    extra=1, can_delete=True, can_delete_extra=True
)


class ActaEmbarcacionInterForm(forms.ModelForm):
	class Meta:
		model = ActaEmbarcacionInter
		fields = ['fecha','nroacta','municipio','visitaen','embarcaciones','nacionalidad','procedencia', \
		'destino','nombrecapitan','agencianaviera','tiempoenpuerto','clasetiempo','tipocarga',\
		'ctrlsanidadvigente','fechaexpcertsanidad','paisexpcertificado','fechavencecertsanidad','renuevacertificado', \
		'enfermedades','nrotripulantes','nropasajeros','nropolisones','vacunafiebreamarilla', \
		'vacunafavigente','tiempovigenciadias','ordenvacunacionoficial','aguapotable','alimentos', \
		'botiquin','depositobasuras','desinsectacion','desinfeccion','desratizacion','cuarentena', \
		'cuarentena','aislamientocasos','aislamientoembarcacion','otramedsan','ningunamedsan','mallasprotectoras', \
		'discoatajaratas','tapetesanitario','cargaparapuerto','tonelajecargapeligrosa','observaciones','fechalibreplatica']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if (field.lower() == "observaciones".lower()) or (field.lower() == "enfermedades".lower()):
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"2",				
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				})

		self.fields['fecha'].widget.attrs['readonly'] = True			
		self.fields['fechalibreplatica'].widget.attrs['readonly'] = True	
		self.fields['fechaexpcertsanidad'].widget.attrs['readonly'] = True	
		self.fields['fechavencecertsanidad'].widget.attrs['readonly'] = True	


class ActaEmbarcacionInterFuncionariosForm(forms.ModelForm):
	class Meta:
		model = ActaEmbarcacionInterFuncionarios
		fields = ['actaembarcacioninter','funcionario']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actaembarcacioninter'].widget.attrs['readonly'] = True			


class ActaEmbarcacionInterImoForm(forms.ModelForm):
	class Meta:
		model = ActaEmbarcacionInterImo
		fields = ['actaembarcacioninter','imo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actaembarcacioninter'].widget.attrs['readonly'] = True	

class ActaEmbarcacionInterPuertoForm(forms.ModelForm):
	class Meta:
		model = ActaEmbarcacionInterPuerto
		fields = ['actaembarcacioninter','puertos','cantidad']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if field.lower() == "puertos".lower():
				self.fields[field].widget.attrs.update({				
				'class':"form-control id_pto", #colocar la clase de bootsTrap a todos los controles o campos
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['actaembarcacioninter'].widget.attrs['readonly'] = True	


ActaEmbarcacionInterFuncionariosFormSet = inlineformset_factory(
    ActaEmbarcacionInter, ActaEmbarcacionInterFuncionarios, form=ActaEmbarcacionInterFuncionariosForm,
    extra=1, can_delete=True, can_delete_extra=True
)

ActaEmbarcacionInterImoFormSet = inlineformset_factory(
    ActaEmbarcacionInter, ActaEmbarcacionInterImo, form=ActaEmbarcacionInterImoForm,
    extra=1, can_delete=True, can_delete_extra=True
)

ActaEmbarcacionInterPuertoFormSet = inlineformset_factory(
    ActaEmbarcacionInter, ActaEmbarcacionInterPuerto, form=ActaEmbarcacionInterPuertoForm,
    extra=1, can_delete=True, can_delete_extra=True
)

#Bodegas y patios
class ActaBodegasPatiosForm(forms.ModelForm):
	class Meta:
		model = ActaBodegasPatios
		fields = ['fecha','establecimiento','nroacta','municipio', 'codigociuu', \
		'objetivovisita','motivovisita','personaladmhombre','personaladmmujeres', \
		'personalopehombre', 'personalopemujeres', 'diasemanalab', 'nroturnos', \
		'horasxturno','requerimiento','plazo','concepto']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if (field.lower() == "requerimiento".lower()):
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"3",				
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				})

		self.fields['fecha'].widget.attrs['readonly'] = True		

class ItemActaBodegasPatiosForm(forms.ModelForm):

	tipoacta = TipoActa.objects.filter(idtipoacta='MISFOBODPAT').first()
	class Meta:
		model = ItemActaBodegasPatios
		fields = ['actabodegaspatios','pregunta','hallazgos']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos			
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=self.tipoacta.pk)	
		self.fields['actabodegaspatios'].widget.attrs['readonly'] = True
		self.fields['pregunta'].widget.attrs['readonly'] = True
		

class FuncionariosActaBodegasPatiosForm(forms.ModelForm):
	class Meta:
		model = FuncionariosActaBodegasPatios
		fields = ['actabodegaspatios','funcionario']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actabodegaspatios'].widget.attrs['readonly'] = True	

class AtiendeActaBodegasPatiosForm(forms.ModelForm):
	class Meta:
		model = AtiendeActaBodegasPatios
		fields = ['actabodegaspatios','tipodoc','identificacion','nombre','cargo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actabodegaspatios'].widget.attrs['readonly'] = True	


class ProductoQuimicoActaBodegasPatiosForm(forms.ModelForm):
	class Meta:
		model = ProductoQuimicoActaBodegasPatios
		fields = ['actabodegaspatios','productoquimico','almacena']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actabodegaspatios'].widget.attrs['readonly'] = True



class MedidaSanitariaActaBodegasPatiosForm(forms.ModelForm):
	class Meta:
		model = MedidaSanitariaActaBodegasPatios
		fields = ['actabodegaspatios','medidasanitaria', 'hallazgos']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if field.lower == 'hallazgos':
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['actabodegaspatios'].widget.attrs['readonly'] = True

ItemActaBodegasPatiosFormSet = inlineformset_factory(
    ActaBodegasPatios, ItemActaBodegasPatios, form=ItemActaBodegasPatiosForm,
    extra=0, can_delete=True, can_delete_extra=True
)

FuncionariosActaBodegasPatiosFormSet = inlineformset_factory(
    ActaBodegasPatios, FuncionariosActaBodegasPatios, form=FuncionariosActaBodegasPatiosForm,
    extra=1, can_delete=True, can_delete_extra=True
)

AtiendeActaBodegasPatiosFormSet = inlineformset_factory(
    ActaBodegasPatios, AtiendeActaBodegasPatios, form=AtiendeActaBodegasPatiosForm,
    extra=1, can_delete=True, can_delete_extra=True
)

ProductoQuimicoActaBodegasPatiosFormSet = inlineformset_factory(
    ActaBodegasPatios, ProductoQuimicoActaBodegasPatios, form=ProductoQuimicoActaBodegasPatiosForm,
    extra=1, can_delete=True, can_delete_extra=True
)

MedidaSanitariaActaBodegasPatiosFormSet = inlineformset_factory(
    ActaBodegasPatios, MedidaSanitariaActaBodegasPatios, form=MedidaSanitariaActaBodegasPatiosForm,
    extra=1, can_delete=True, can_delete_extra=True
)

#Viviendas transitorias
class ActaViviendaTransitoriaForm(forms.ModelForm):
	qrysetconcepto={}
	tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-VITR').first()
	if tipoacta:
		qrysetconcepto = filtrar_concepto_sanitario(tipoacta['id']).all()

	class Meta:
		model = ActaViviendaTransitoria
		fields = ['fecha','nroacta','municipio','establecimiento','inspeccionanterior', \
		'fechaultinspeccion','conceptoanterior','porcumplimientoanterior','nroactanterior', \
		'motivovisita','tipoacta','requerimiento','observacionautsan','observacionestable', \
		'puntaje','concepto']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if ((field.lower() == "requerimiento".lower())  
			or (field.lower() == "observacionautsan".lower()) 
			or (field.lower() == "observacionestable".lower())):
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"5",				
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['concepto'].queryset = self.qrysetconcepto			
		self.fields['fecha'].widget.attrs['readonly'] = True	
		self.fields['fechaultinspeccion'].widget.attrs['readonly'] = True	

class ItemActaViviendaTransitoria4Form(forms.ModelForm):
	
	class Meta:
		model = ItemActaViviendaTransitoria
		fields = ['actaviviendatransitoria','pregunta','evaluacion','puntaje','habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice

		#Vivienda transitoria
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-VITR').first()
		
		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos			
				'enable': False
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=tipoacta).all()
		self.fields['actaviviendatransitoria'].widget.attrs['readonly'] = True
		self.fields['pregunta'].widget.attrs['readonly'] = True
		self.fields['puntaje'].widget.attrs['readonly'] = True
		self.fields['habilitada'].widget.attrs['readonly'] = True

class ItemActaViviendaTransitoria5Form(forms.ModelForm):
	
	class Meta:
		model = ItemActaViviendaTransitoria
		fields = ['actaviviendatransitoria','pregunta','evaluacion','puntaje','habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice

		#Hogar de paso
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOPA').first()
		
		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos			
				'enable': False
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=tipoacta).all()
		self.fields['actaviviendatransitoria'].widget.attrs['readonly'] = True
		self.fields['pregunta'].widget.attrs['readonly'] = True
		self.fields['puntaje'].widget.attrs['readonly'] = True
		self.fields['habilitada'].widget.attrs['readonly'] = True

class ItemActaViviendaTransitoria6Form(forms.ModelForm):
	
	class Meta:
		model = ItemActaViviendaTransitoria
		fields = ['actaviviendatransitoria','pregunta','evaluacion','puntaje','habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice

		#Hogar comunitario
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOGC').first()
		
		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos			
				'enable': False
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=tipoacta).all()
		self.fields['actaviviendatransitoria'].widget.attrs['readonly'] = True
		self.fields['pregunta'].widget.attrs['readonly'] = True
		self.fields['puntaje'].widget.attrs['readonly'] = True
		self.fields['habilitada'].widget.attrs['readonly'] = True


class ItemActaViviendaTransitoria7Form(forms.ModelForm):
	
	class Meta:
		model = ItemActaViviendaTransitoria
		fields = ['actaviviendatransitoria','pregunta','evaluacion','puntaje','habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice

		#Hogar Hogar geriatrico o de larga estancia
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOGG').first()
		
		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos			
				'enable': False
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=tipoacta).all()
		self.fields['actaviviendatransitoria'].widget.attrs['readonly'] = True
		self.fields['pregunta'].widget.attrs['readonly'] = True
		self.fields['puntaje'].widget.attrs['readonly'] = True
		self.fields['habilitada'].widget.attrs['readonly'] = True

#Centros vida
class ItemActaViviendaTransitoria8Form(forms.ModelForm):
	
	class Meta:
		model = ItemActaViviendaTransitoria
		fields = ['actaviviendatransitoria','pregunta','evaluacion','puntaje','habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice

		#Centros vida
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-ECV').first()

		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos			
				'enable': False,
				'rows':"1",				
				'readonly':True,
				'enable':False
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=tipoacta).all()
		self.fields['actaviviendatransitoria'].widget.attrs['readonly'] = True		
		self.fields['puntaje'].widget.attrs['readonly'] = True
		self.fields['habilitada'].widget.attrs['readonly'] = True



class FuncionariosActaViviendaTransitoriaForm(forms.ModelForm):
	class Meta:
		model = FuncionariosActaViviendaTransitoria
		fields = ['actaviviendatransitoria','funcionario']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actaviviendatransitoria'].widget.attrs['readonly'] = True	

class AtiendeActaViviendaTransitoriaForm(forms.ModelForm):
	class Meta:
		model = AtiendeActaViviendaTransitoria
		fields = ['actaviviendatransitoria','tipodoc','identificacion','nombre','cargo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actaviviendatransitoria'].widget.attrs['readonly'] = True	




FuncionariosActaViviendaTransitoriaFormSet = inlineformset_factory(
    ActaViviendaTransitoria, FuncionariosActaViviendaTransitoria, form=FuncionariosActaViviendaTransitoriaForm,
    extra=1, can_delete=True, can_delete_extra=True
)

AtiendeActaViviendaTransitoriaFormSet = inlineformset_factory(
    ActaViviendaTransitoria, AtiendeActaViviendaTransitoria, form=AtiendeActaViviendaTransitoriaForm,
    extra=1, can_delete=True, can_delete_extra=True
)


class PreguntaForm(forms.ModelForm):
	class Meta:
		model = Pregunta
		fields = ['bloque','idpregunta','descripcion', 'orden', 'habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			if (field.lower() == "descripcion".lower()):
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"3",				
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	

class EvaluacionPreguntaForm(forms.ModelForm):

	class Meta:
		model = EvaluacionPregunta
		fields = ['pregunta','evaluacion','puntaje']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['pregunta'].widget.attrs['readonly'] = True	


EvaluacionPreguntaFormSet = inlineformset_factory(
    Pregunta, EvaluacionPregunta, form=EvaluacionPreguntaForm,
    extra=1, can_delete=True, can_delete_extra=True
)



#Acta Centro carcelario
class ActaCentroCarcelarioForm(forms.ModelForm):
	qrysetconcepto = {}
	tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-CARC').first()
	if tipoacta:
		qrysetconcepto = filtrar_concepto_sanitario(tipoacta['id']).all()

	class Meta:
		model = ActaCentroCarcelario
		fields = ['fecha','nroacta','municipio','carcel','carcelmilitares','centromenores', \
		'centrosalaretencion', 'centroreclusiondamas', 'otrotiporeclusion','entidadterritorialsalud', \
		'codigociuu', 'actividadeconomica', 'establecimiento', 'nroceldas','nropatios','nroareatalleres', \
		'nroareaprepalimentos','nroretenidos','nroretenidoshombres','nroretenidosmujeres', 'capacidad', \
		'pobregultimavisita','inspeccionanterior', \
		'fechaultinspeccion','conceptoanterior','porcumplimientoanterior','nroactanterior', \
		'motivovisita','tipoacta','requerimiento','observacionautsan','observacionestable', \
		'puntaje','concepto','nroadministativos','nrooperativos', 'nroafiliadosarl', 'nroafiliadosegsocial', \
		'gestoresiduohospitalario','nromuestrastomadas','nroactatomamuestra', 'clausuratemptotal', \
		'clausuratemparcial', 'susparcialtrabajo', 'susptotaltrabservicio', 'aislamiento','decomiso', \
		'destruccion', 'congelacion','capturanimales', 'vacunacion','controlinsectos', 'desocupacion', \
		'nroactamedidasanitaria', 'diashabileplazo', 'fechainiplazo', 'fechafinplazo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		

		for field in iter(self.fields):
			if ((field.lower() == "requerimiento".lower())  
			or (field.lower() == "observacionautsan".lower()) 
			or (field.lower() == "observacionestable".lower())):
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"5",				
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		
		self.fields['concepto'].queryset = self.qrysetconcepto			
		self.fields['fecha'].widget.attrs['readonly'] = True	
		self.fields['fechainiplazo'].widget.attrs['readonly'] = True	
		self.fields['fechafinplazo'].widget.attrs['readonly'] = True			
		self.fields['fechaultinspeccion'].widget.attrs['readonly'] = True	

class ItemActaCentroCarcelarioForm(forms.ModelForm):
	
	class Meta:
		model = ItemActaCentroCarcelario
		fields = ['actacentrocarcelario','pregunta','evaluacion','puntaje','habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice

		#Centro carcelario
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-CARC').first()
		
		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos			
				'enable': False
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=tipoacta).all()
		self.fields['actacentrocarcelario'].widget.attrs['readonly'] = True
		self.fields['pregunta'].widget.attrs['readonly'] = True
		self.fields['puntaje'].widget.attrs['readonly'] = True
		self.fields['habilitada'].widget.attrs['readonly'] = True


class FuncionariosActaCentroCarcelarioForm(forms.ModelForm):
	class Meta:
		model = FuncionariosActaCentroCarcelario
		fields = ['actacentrocarcelario','funcionario']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actacentrocarcelario'].widget.attrs['readonly'] = True	

class AtiendeActaCentroCarcelarioForm(forms.ModelForm):
	class Meta:
		model = AtiendeActaCentroCarcelario
		fields = ['actacentrocarcelario','tipodoc','identificacion','nombre','cargo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actacentrocarcelario'].widget.attrs['readonly'] = True	


FuncionariosActaCentroCarcelarioFormSet = inlineformset_factory(
    ActaCentroCarcelario, FuncionariosActaCentroCarcelario, form=FuncionariosActaCentroCarcelarioForm,
    extra=1, can_delete=True, can_delete_extra=True
)

AtiendeActaCentroCarcelarioFormSet = inlineformset_factory(
    ActaCentroCarcelario, AtiendeActaCentroCarcelario, form=AtiendeActaCentroCarcelarioForm,
    extra=1, can_delete=True, can_delete_extra=True
)


#Acta Droguerias
class ActaDrogueriaForm(forms.ModelForm):

	tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-DROG').first()
	if tipoacta:
		qrysetconcepto = filtrar_concepto_sanitario(tipoacta.pk).all()
	else:
		qrysetconcepto={}

	class Meta:
		model = ActaDrogueria
		fields = ['fecha','nroacta','municipio', 'establecimiento', 'tipodocdirtec','identificaciondirtec','nombredirtec', \
		'perfildirector','resolucionapertura','funcionantes1992','resoluciontraslado', 'tipoautorizacion', \
		'inspeccionanterior', 'fechaultinspeccion','conceptoanterior', \
		'porcumplimientoanterior','nroactanterior', 'tipoacta','puntaje','concepto', \
		'nroadministativos','nrooperativos','requerimiento','observacionautsan','observacionestable', \
		'diashabileplazo', 'fechainiplazo', 'fechafinplazo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		

		for field in iter(self.fields):
			if ((field.lower() == "requerimiento".lower())  
			or (field.lower() == "observacionautsan".lower()) 
			or (field.lower() == "observacionestable".lower())):
				self.fields[field].widget.attrs.update({				
				'class':"form-control", #colocar la clase de bootsTrap a todos los controles o campos
				'rows':"5",				
				})
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		
		self.fields['concepto'].queryset = self.qrysetconcepto			
		self.fields['fecha'].widget.attrs['readonly'] = True	
		self.fields['fechainiplazo'].widget.attrs['readonly'] = True	
		self.fields['fechafinplazo'].widget.attrs['readonly'] = True			
		self.fields['fechaultinspeccion'].widget.attrs['readonly'] = True	

class ItemActaDrogueriasForm(forms.ModelForm):
	
	class Meta:
		model = ItemActaDroguerias
		fields = ['actadrogueria','pregunta','evaluacion','puntaje','habilitada']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice

		#Centro carcelario
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-DROG').first()
		
		for field in iter(self.fields):
			if field.lower == 'pregunta':				
				self.fields[field].widget.attrs.update({				
				'class':"form-control itemacta", #colocar la clase de bootsTrap a todos los controles o campos			
				'enable': False
				})	
			else:
				self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
				})	
		self.fields['pregunta'].queryset =  Pregunta.objects.filter(bloque__tipoacta_id=tipoacta).all()
		self.fields['actadrogueria'].widget.attrs['readonly'] = True
		self.fields['pregunta'].widget.attrs['readonly'] = True
		self.fields['puntaje'].widget.attrs['readonly'] = True
		self.fields['habilitada'].widget.attrs['readonly'] = True


class FuncionariosActaDrogueriaForm(forms.ModelForm):
	class Meta:
		model = FuncionariosActaDrogueria
		fields = ['actadrogueria','funcionario']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actadrogueria'].widget.attrs['readonly'] = True	

class AtiendeActaDrogueriaForm(forms.ModelForm):
	class Meta:
		model = AtiendeActaDrogueria
		fields = ['actadrogueria','tipodoc','identificacion','nombre','cargo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) #para que se inicialice
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({				
				'class':"form-control" #colocar la clase de bootsTrap a todos los controles o campos
			})	
		self.fields['actadrogueria'].widget.attrs['readonly'] = True	


FuncionariosActaDrogueriaFormSet = inlineformset_factory(
    ActaDrogueria, FuncionariosActaDrogueria, form=FuncionariosActaDrogueriaForm,
    extra=1, can_delete=True, can_delete_extra=True
)

AtiendeActaDrogueriaFormSet = inlineformset_factory(
    ActaDrogueria, AtiendeActaDrogueria, form=AtiendeActaDrogueriaForm,
    extra=1, can_delete=True, can_delete_extra=True
)



