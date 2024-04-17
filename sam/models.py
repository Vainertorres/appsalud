from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.db.models import Q, Count, F



# Create your models here.

from cnf.models import ClaseModelo2, Tipodoc, Departamento, Municipio, Funcionario, Pais, \
GestoResiduoHospitalario, ActividadEconomica

'''Unidad salud ambiental'''
class UnidadSalAmb(ClaseModelo2):
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name_plural="Unidad funcional salud ambiental"		
		verbose_name_plural="Unidades funcionales salud ambiental"

	def __str__(self):
		return "{}".format(self.descripcion)

class Actividad(ClaseModelo2):
	codigo = models.CharField(max_length=10, unique=True)
	descripcion = models.CharField(max_length=500)
	unidadsalamb = models.ForeignKey(UnidadSalAmb, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural="Actividad"		
		verbose_name_plural="Actividades"

	def __str__(self):
		return "{}".format(self.descripcion)

class TipoActa(ClaseModelo2):
	idtipoacta = models.CharField(max_length=15, unique=True)
	descripcion = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural="Tipos de Actas"
		ordering=['descripcion']

	def __str__(self):
		return "{} : {}".format(self.idtipoacta, self.descripcion)


class Concepto(ClaseModelo2):
	codigo = models.CharField(max_length=3)
	tipoacta = models.ForeignKey(TipoActa, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=30)
	porcumplemin = models.FloatField()
	porcumplemax = models.FloatField()

	class Meta:
		verbose_name_plural="Conceptos Sanitarios"
		unique_together=(("codigo", "tipoacta"),) #Yave única

	def __str__(self):
		return "{}".format(self.descripcion)

class Evaluacion(ClaseModelo2):
	idevaluacion = models.CharField(max_length=2)
	descripcion = models.CharField(max_length=50)
	nota = models.CharField(max_length=200, null=True, blank=True)

	class Meta:
		verbose_name_plural = "Evaluaciones"

	def __str__(self):
		return "{}".format(self.descripcion)

class LugarUbica(ClaseModelo2):
	idlugarubica = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural="Lugares donde se ubica el Establecimiento"

	def __str__(self):
		return "{}".format(self.descripcion)

class MotivoVisita(ClaseModelo2):
	idmotivovisita = models.CharField(max_length=3)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name_plural="Motivos de Visita"

	def __str__(self):
		return "{}".format(self.descripcion)

class Propietario(ClaseModelo2):
	tipodoc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
	nitcc = models.CharField(max_length=30)
	nombres = models.CharField(max_length=80)
	apellido1 = models.CharField(max_length=40)
	apellido2 = models.CharField(max_length=40, null=True, blank=True)
	telfijo = models.CharField(max_length=20, null=True, blank=True)
	telcelular = models.CharField(max_length=30, null=True, blank=True)
	correoelectronico = models.EmailField(max_length=200, null=True, blank=True)

	class Meta:
		verbose_name_plural='Propietarios'

	def __str__(self):
		razsoc = self.nombres + " " + self.apellido1
		if not (self.apellido2 == "" or self.apellido2==None):
			razsoc += " " + self.apellido2

		return "{} : {}".format(self.nitcc, razsoc)

class Bloque(ClaseModelo2):
	tipoacta = models.ForeignKey(TipoActa, on_delete=models.CASCADE)
	idbloque = models.FloatField()
	descripcion = models.CharField(max_length=300)
	orden = models.FloatField(default=0)
	porcentaje = models.FloatField(default=0)
	bloqueprincipal = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural="Bloques de preguntas"
		ordering = ['tipoacta','orden']

	def __str__(self):
		return "{} : {}".format(self.tipoacta.idtipoacta, self.descripcion)

class Pregunta(ClaseModelo2):
	bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)
	idpregunta = models.CharField(max_length=10)
	descripcion = models.TextField()
	orden = models.FloatField(default=0)
	habilitada=models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Variables a Evaluar'
		ordering = ['orden']


	def __str__(self):
		return "{}-{}".format(self.idpregunta, self.descripcion)


class EvaluacionPregunta(ClaseModelo2):
	evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	puntaje = models.FloatField()

	class Meta:
		verbose_name_plural = "Evaluaciones de preguntas"

	def __str__(self):
		return "{}-{}-{}-{}".format(self.pregunta_id, self.pregunta, self.evaluacion, self.puntaje)


class Establecimiento(ClaseModelo2):
	nitcc = models.CharField(max_length=30, unique=True)
	razonsocial = models.CharField(max_length=150)
	nroinscripcion = models.CharField(max_length=30)
	nombrecomercial = models.CharField(max_length=150)
	direccion = models.CharField(max_length=150)
	telefono = models.CharField(max_length=80)
	fax = models.CharField(max_length=20, null=True, blank=True)
	nromatricula = models.CharField(max_length=30)
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='Dptoubica')
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='mpioubica')
	lugarubica = models.ForeignKey(LugarUbica, on_delete=models.CASCADE, null=True, blank=True)
	correoelectronico = models.EmailField(max_length=150, null=True, blank = True)
	propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, null=True, blank=True, \
	related_name='codpropietario')
	replegal = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='codreplegal')
	direccionotifica = models.CharField(max_length=150)
	dptonotifica= models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='dptonotifica')
	mpionotifica= models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='mpionotifica')
	horariofunciona = models.CharField(max_length=150)
	nrotrabajadores = models.IntegerField()

	class Meta:
		verbose_name_plural="Establecimientos"

	def __str__(self):
		return "{}".format(self.razonsocial)


class TipoSujeto(ClaseModelo2):
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=150)
	
	class Meta:
		verbose_name = 'Tipo de sujeto'
		verbose_name_plural = 'Tipo de sujeto'
		ordering = ['descripcion']


	def __str__(self):
		return "{}".format(self.descripcion)

class ActaEstabEducativo(ClaseModelo2):
	fecha=models.DateField()
	nroacta=models.CharField(max_length=15)
	ciudad=models.CharField(max_length=30)
	establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
	nombrerector=models.CharField(max_length=100, null=True, blank=True)
	tipodocrector=models.ForeignKey(Tipodoc, on_delete=models.CASCADE, related_name='tipodocrector', null=True, blank=True)
	identificacionrector=models.CharField(max_length=20, null=True, blank=True)
	nroestjormanhombres=models.IntegerField(default=0)
	nroestjormanmujeres	=models.IntegerField(default=0)
	nroestjortarhombres=models.IntegerField(default=0)
	nroestjortarmujeres	=models.IntegerField(default=0)
	nroestjornochombres=models.IntegerField(default=0)
	nroestjornocmujeres	=models.IntegerField(default=0)
	nrodocenteshombres=models.IntegerField(default=1)
	nrodocentesmujeres=models.IntegerField(default=1)
	nroaulas=models.IntegerField(default=1)
	nropatios=models.IntegerField(default=0)
	nrocafeterias=models.IntegerField(default=0)
	fechaultinspeccion=models.DateField(null=True, blank=True)
	nroactaultinspeccion=models.CharField(max_length=15, null=True, blank=True)
	ultconcepto=models.ForeignKey(Concepto, on_delete=models.CASCADE, related_name='ultconcepto')
	motivovisita=models.ForeignKey(MotivoVisita, on_delete=models.CASCADE, null=True, blank=True)
	concepto=models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True, related_name='Concepto')
	nrototalmuestrastomadas = models.IntegerField(null=True, blank=True, default=0)
	nroactatomamuestras = models.CharField(max_length=20, null=True, blank=True)
	requerimientosanitario=models.TextField(null=True, blank=True)
	observacionesanitarias=models.TextField(null=True, blank=True)
	observacionestablecimiento=models.TextField(null=True, blank=True)
	clausuratemptotal = models.BooleanField(default=False, verbose_name='Clausura temporal total')
	clausuratemparcial = models.BooleanField(default=False, verbose_name='Clausura temporal parcial')
	susparcialtrabajo = models.BooleanField(default=False, verbose_name='Suspensión parcial de trabajos o servicios')
	susptotaltrabservicio = models.BooleanField(default=False, verbose_name='Suspensión total de trabajos o servicios')
	aislamiento = models.BooleanField(default=False, verbose_name='Aislamiento o internación de personas para evitar la transmisión de enfermedades')
	decomiso = models.BooleanField(default=False, verbose_name='Decomiso')
	destruccion = models.BooleanField(default=False, verbose_name='Destrucción o desnaturalización')
	congelacion = models.BooleanField(default=False, verbose_name='Congelación')
	capturanimales = models.BooleanField(default=False, verbose_name='Captura y observación de animales sospechosos de enfermedades transmisibles')
	vacunacion = models.BooleanField(default=False, verbose_name='Vacunación personas o animales')
	controlinsectos = models.BooleanField(default=False, verbose_name='Control de insectos u otra fauna nociva o transmisora de enfermedades')
	desocupacion = models.BooleanField(default=False, verbose_name='Desocupación o desalojamiento de establecimientos o vivienda')
	nroactamedidasanitaria = models.CharField(max_length=20, null=True, blank=True)
	diashabileplazo = models.IntegerField(default=0, null=True, blank=True)
	fechainiplazo=models.DateField(null=True, blank=True)
	fechafinplazo=models.DateField(null=True, blank=True)

	class Meta:
		verbose_name='Acta de visita a establecimiento educativo'
		ordering = ['-fecha']


	def __str__(self):
		return "{} {}".format(self.nroacta, self.establecimiento) 

class ItemActaEstabEducativo(ClaseModelo2):
	actaestabeducativo = models.ForeignKey(ActaEstabEducativo, on_delete=models.CASCADE)
	pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	evaluacion=models.ForeignKey(Evaluacion, on_delete=models.CASCADE, default=3)
	hallazgos=models.TextField(null=True, blank=True)
	puntaje=models.FloatField(default=0)
	habilitada=models.BooleanField(default=True)

class ActaEstEduFuncionario(ClaseModelo2):
	actaestabeducativo = models.ForeignKey(ActaEstabEducativo, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)

	def __str__(self):
		return "{}".format(self.funcionario)

class Atiende_ActaEstabEduc(ClaseModelo2):
	actaestabeducativo = models.ForeignKey(ActaEstabEducativo, on_delete=models.CASCADE)
	tipodoc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=100)
	identificacion = models.CharField(max_length=20)
	institucion = models.CharField(max_length=100, null=True, blank=True)
	cargo=models.CharField(max_length=80, null=True, blank=True)


'''Acta de propósito General'''
class ActaGeneral(ClaseModelo2):
	fecha = models.DateField()
	actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
	nroacta=models.CharField(max_length=15)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
	tiposujeto = models.ForeignKey(TipoSujeto, on_delete=models.CASCADE)
	observacion = models.TextField()
	requerimiento = models.TextField(null=True,blank=True)
	plazo=models.IntegerField(default=0, null=True, blank=True)
	concepto=models.ForeignKey(Concepto,on_delete=models.CASCADE)

class ActaGeneralFuncionarios(ClaseModelo2):
	actageneral = models.ForeignKey(ActaGeneral, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

	class Meta:
		verbose_name='Funcionarios que realizaron visita'

	def __str__(self):
		return "{}".format(self.funcionario)


class AtiendeActaGeneral(ClaseModelo2):
	actageneral = models.ForeignKey(ActaGeneral, on_delete=models.CASCADE)
	tipodoc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
	identificacion = models.CharField(max_length=20)
	nombre=models.CharField(max_length=100)
	cargo=models.CharField(max_length=80, null=True, blank=True)

	def __str__(self):
		return "{} - {}".format(self.identificacion, self.nombre)

class Embarcaciones(ClaseModelo2):
	matricula = models.CharField(max_length=30, unique=True)
	nombre = models.CharField(max_length=150)
	pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural="Embarcaciones"

	def __str__(self):
		return "{}".format(self.nombre)


class Puertos(ClaseModelo2):
	codigo = models.CharField(max_length=10, unique=True)
	descripcion = models.CharField(max_length=150)
	pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural="Puertos"

	def __str__(self):
		return "{}".format(self.descripcion)

class TipoCarga(ClaseModelo2):
	codigo = models.CharField(max_length=10, unique=True)
	descripcion = models.CharField(max_length=150)

	class Meta:
		verbose_name_plural="Tipo de carga"

	def __str__(self):
		return "{}".format(self.descripcion)

class AgenciaNaviera(ClaseModelo2):
	codigo=models.CharField(max_length=20, unique=True)
	descripcion=models.CharField(max_length=150)

	class Meta:
		verbose_name_plural="Agencias navieras"

	def __str__(self):
		return "{}".format(self.descripcion)

class Visitaen(ClaseModelo2):
	codigo=models.CharField(max_length=3, unique=True)
	descripcion=models.CharField(max_length=80)

	class Meta:
		verbose_name_plural="Visita en "

	def __str__(self):
		return "{}".format(self.descripcion)


class ActaEmbarcacionInter(ClaseModelo2):
	CLASETIEMPO = (
		('H','Horas'),
		('D','Días'),
		('S','Semanas'),
		)
	fecha = models.DateTimeField()	
	nroacta=models.CharField(max_length=15)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	embarcaciones = models.ForeignKey(Embarcaciones, on_delete=models.CASCADE)
	nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='nacionalidad_emb')
	visitaen = models.ForeignKey(Visitaen, on_delete=models.CASCADE)
	procedencia = models.ForeignKey(Puertos, on_delete=models.CASCADE, related_name='procedencia_pto')
	destino = models.ForeignKey(Puertos, on_delete=models.CASCADE, null=True, blank=True, related_name='destino_pto')
	nombrecapitan = models.CharField(max_length=150, null=True, blank=True)
	agencianaviera = models.ForeignKey(AgenciaNaviera, on_delete=models.CASCADE, null=True, blank=True)
	tiempoenpuerto = models.FloatField(default=0, null=True, blank=True)
	clasetiempo = models.CharField(max_length=1, choices=CLASETIEMPO, null=True, blank=True)
	tipocarga = models.ForeignKey(TipoCarga, on_delete=models.CASCADE, null=True, blank=True)
	ctrlsanidadvigente = models.BooleanField(default=True)
	fechaexpcertsanidad = models.DateField(null=True, blank=True)
	paisexpcertificado = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais_expcertificado')
	fechavencecertsanidad = models.DateField(null=True, blank=True)
	renuevacertificado = models.BooleanField(default=False, null=True, blank=True)
	enfermedades = models.TextField(null=True, blank=True)
	nrotripulantes = models.IntegerField(default=1)
	nropasajeros = models.IntegerField(default=0)
	nropolisones = models.IntegerField(default=0)
	vacunafiebreamarilla = models.BooleanField(default=True)
	vacunafavigente = models.BooleanField(default=True)
	tiempovigenciadias=models.IntegerField(default=0)
	ordenvacunacionoficial = models.BooleanField(default=True)
	aguapotable=models.BooleanField(default=True)
	alimentos=models.BooleanField(default=True)
	botiquin=models.BooleanField(default=True)
	depositobasuras=models.BooleanField(default=False)
	desinsectacion=models.BooleanField(default=False)
	desinfeccion=models.BooleanField(default=False)
	desratizacion=models.BooleanField(default=False)
	cuarentena=models.BooleanField(default=False)
	cuarentena=models.BooleanField(default=False)
	aislamientocasos=models.BooleanField(default=False)
	aislamientoembarcacion=models.BooleanField(default=False)
	otramedsan=models.BooleanField(default=False)
	ningunamedsan=models.BooleanField(default=False)
	mallasprotectoras=models.BooleanField(default=False)
	discoatajaratas=models.BooleanField(default=False)
	tapetesanitario=models.BooleanField(default=False)
	cargaparapuerto=models.FloatField(default=0)
	tonelajecargapeligrosa=models.FloatField(default=0)
	observaciones=models.TextField(null=True, blank=True)
	fechalibreplatica = models.DateTimeField()

	class Meta:
		verbose_name_plural="Acta embarcaciones internacionales"

	def __str__(self):
		return "{} - {}".format(self.embarcaciones, self.nroacta)

	
class ActaEmbarcacionInterFuncionarios(ClaseModelo2):
	actaembarcacioninter = models.ForeignKey(ActaEmbarcacionInter, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

	class Meta:
		verbose_name='Funcionarios que realizaron visita'

	def __str__(self):
		return "{}".format(self.funcionario)

class ActaEmbarcacionInterImo(ClaseModelo2):
	actaembarcacioninter = models.ForeignKey(ActaEmbarcacionInter, on_delete=models.CASCADE)
	imo = models.FloatField(default=0)

	class Meta:
		verbose_name='IMO'

	def __str__(self):
		return "{}".format(self.imo)


class ActaEmbarcacionInterPuerto(ClaseModelo2):
	actaembarcacioninter = models.ForeignKey(ActaEmbarcacionInter, on_delete=models.CASCADE)
	puertos = models.ForeignKey(Puertos, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)

	class Meta:
		verbose_name='Puertos visitados'

	def __str__(self):
		return "{}".format(self.puertos)

class PerfilDirector(ClaseModelo2):
	codigo = models.CharField(max_length=3)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name_plural="Perfil director técnico"

	def __str__(self):
		return "{}".format(self.descripcion)


class ObjetivoVisita(ClaseModelo2):
	codigo = models.CharField(max_length=3)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name_plural="Objetivos de visitas"

	def __str__(self):
		return "{}".format(self.descripcion)

class ProductoQuimico(ClaseModelo2):
	codigo = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural="Productos Químicos"

	def __str__(self):
		return "{}".format(self.descripcion)

class MedidaSanitaria(ClaseModelo2):
	codigo = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=500)

	class Meta:
		verbose_name_plural="Medidas sanitarias"

	def __str__(self):
		return "{}".format(self.descripcion)

class ActaBodegasPatios(ClaseModelo2):
	fecha = models.DateTimeField()	
	nroacta=models.CharField(max_length=15)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
	direccion = models.CharField(max_length=150, null=True, blank=True)
	telefono = models.CharField(max_length=80, null=True, blank=True)
	replegal = models.ForeignKey(Propietario, on_delete=models.CASCADE, null=True, blank=True)
	codigociuu = models.CharField(max_length=10, null=True, blank=True)
	objetivovisita = models.ForeignKey(ObjetivoVisita, on_delete=models.CASCADE, null=True, blank=True)
	motivovisita = models.ForeignKey(MotivoVisita, on_delete=models.CASCADE, null=True, blank=True)
	personaladmhombre=models.IntegerField(default=0, null=True, blank=True)
	personaladmmujeres=models.IntegerField(default=0, null=True, blank=True)
	personalopehombre=models.IntegerField(default=0, null=True, blank=True)
	personalopemujeres=models.IntegerField(default=0, null=True, blank=True)
	diasemanalab=models.IntegerField(default=0, null=True, blank=True)
	nroturnos = models.IntegerField(default=1, null=True, blank=True)
	horasxturno = models.IntegerField(default=1, null=True, blank=True)
	requerimiento=models.TextField(null=True, blank=True)
	plazo = models.IntegerField(default=0, null=True, blank=True)
	concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name_plural="Actas de bodegas y patios"

	def __str__(self):
		return "{}".format(self.establecimiento)


class ItemActaBodegasPatios(ClaseModelo2):
	HALLAZGO=(
		('SI','SI'),
		('NO','NO'),
		('NA','NA')
		)
	actabodegaspatios = models.ForeignKey(ActaBodegasPatios, on_delete=models.CASCADE)
	pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	hallazgos=models.CharField(max_length=2, choices=HALLAZGO, default='NO')

	def __str__(self):
		return "{}".format(self.pregunta)


class FuncionariosActaBodegasPatios(ClaseModelo2):
	actabodegaspatios = models.ForeignKey(ActaBodegasPatios, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)

	def __str__(self):
		return "{}".format(self.funcionario)

class AtiendeActaBodegasPatios(ClaseModelo2):
	actabodegaspatios = models.ForeignKey(ActaBodegasPatios, on_delete=models.CASCADE)
	tipodoc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
	identificacion = models.CharField(max_length=20)
	nombre=models.CharField(max_length=150)	
	cargo=models.CharField(max_length=80, null=True, blank=True)

	def __str__(self):
		return "{}".format(self.nombre)

class ProductoQuimicoActaBodegasPatios(ClaseModelo2):
	actabodegaspatios = models.ForeignKey(ActaBodegasPatios, on_delete=models.CASCADE)
	productoquimico = models.ForeignKey(ProductoQuimico, on_delete = models.CASCADE)
	almacena = models.BooleanField(default=True)

	def __str__(self):
		return "{}".format(self.productoquimico)

class MedidaSanitariaActaBodegasPatios(ClaseModelo2):
	HALLAZGO=(
		('SI','SI'),
		('NO','NO'),
		('NA','NA')
		)
	actabodegaspatios = models.ForeignKey(ActaBodegasPatios, on_delete=models.CASCADE)
	medidasanitaria = models.ForeignKey(MedidaSanitaria, on_delete = models.CASCADE)
	hallazgos=models.CharField(max_length=2, choices=HALLAZGO, default='NO')


	def __str__(self):
		return "{}".format(self.medidasanitaria)


def obtener_cumplimiento_condiciones_sanitarias(codacta, puntaje):
	resultado = {}
	resultado = Concepto.objects.filter(tipoacta_id = codacta).filter(
    Q(porcumplemin__lte=puntaje) & Q(porcumplemax__gte=puntaje)
	).first()
	return resultado

#Actas viviendas Transitorias
class ActaViviendaTransitoria(ClaseModelo2):
	fecha = models.DateTimeField()	
	nroacta=models.CharField(max_length=15)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
	inspeccionanterior = models.BooleanField(default=False)
	fechaultinspeccion = models.DateTimeField(null=True, blank=True)	
	conceptoanterior = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True, \
	related_name="vivtran_concepto_anterior")
	porcumplimientoanterior = models.FloatField(default=0, null=True, blank=True)
	nroactanterior=models.CharField(max_length=15, null=True, blank=True)
	motivovisita = models.ForeignKey(MotivoVisita, on_delete=models.CASCADE, null=True, blank=True)
	tipoacta = models.ForeignKey(TipoActa, on_delete=models.CASCADE)
	requerimiento = models.TextField(null=True, blank=True)
	observacionautsan = models.TextField(null=True, blank=True)
	observacionestable = models.TextField(null=True, blank=True)
	puntaje = models.FloatField(default=0)
	concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True, related_name="vivtran_concepto")

	class Meta:
		verbose_name_plural="Acta visita viviendas transitorias"

	def __str__(self):
		return "{}-{}".format(self.fecha, self.establecimiento)

@receiver(pre_save, sender=ActaViviendaTransitoria)
def actaViviendaTransitoria_guardar(sender,instance,**kwargs):
	puntaje = ItemActaViviendaTransitoria.objects.filter(actaviviendatransitoria_id = instance.id).aggregate(total_puntaje=Sum('puntaje'))
	condsanitaria = obtener_cumplimiento_condiciones_sanitarias(instance.tipoacta_id,  puntaje['total_puntaje'])
	print("Condiciones sanitarias")
	if condsanitaria:
		instance.concepto_id = condsanitaria.id
	instance.puntaje = puntaje['total_puntaje']
	
class ItemActaViviendaTransitoria(ClaseModelo2):
	actaviviendatransitoria = models.ForeignKey(ActaViviendaTransitoria, on_delete=models.CASCADE)
	pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	evaluacion=models.ForeignKey(Evaluacion, on_delete=models.CASCADE, default=3)
	puntaje=models.FloatField(default=0)
	habilitada=models.BooleanField(default=True)

	def __str__(self):
		return "{}".format(self.pregunta)

@receiver(pre_save, sender=ItemActaViviendaTransitoria)
def itemActaViviendaTransitoria_guardar(sender,instance,**kwargs):
	evalpregunta = EvaluacionPregunta.objects.filter(pregunta_id = instance.pregunta_id).filter(evaluacion_id=instance.evaluacion_id).first()


	if evalpregunta:
		instance.puntaje = evalpregunta.puntaje
	else:
		instance.puntaje = 0 

class FuncionariosActaViviendaTransitoria(ClaseModelo2):
	actaviviendatransitoria = models.ForeignKey(ActaViviendaTransitoria, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)

	def __str__(self):
		return "{}".format(self.funcionario)

class AtiendeActaViviendaTransitoria(ClaseModelo2):
	actaviviendatransitoria = models.ForeignKey(ActaViviendaTransitoria, on_delete=models.CASCADE)
	tipodoc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
	identificacion = models.CharField(max_length=20)
	nombre=models.CharField(max_length=150)	
	cargo=models.CharField(max_length=80, null=True, blank=True)

	def __str__(self):
		return "{}".format(self.nombre)
#----------------------------

#Actas Centros carcelarios
class ActaCentroCarcelario(ClaseModelo2):
	fecha = models.DateTimeField()	
	nroacta=models.CharField(max_length=15)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	carcel = models.BooleanField(default = True)
	carcelmilitares = models.BooleanField(default = False)
	centromenores = models.BooleanField(default = False)
	centrosalaretencion = models.BooleanField(default = False)
	centroreclusiondamas = models.BooleanField(default = False)
	otrotiporeclusion = models.BooleanField(default = False)
	entidadterritorialsalud = models.CharField(max_length=255, null=True, blank=True)
	codigociuu = models.BooleanField(default=False)
	actividadeconomica = models.ForeignKey(ActividadEconomica, on_delete=models.CASCADE, null=True, blank=True)
	establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
	nroceldas = models.IntegerField(default=1, null=True, blank=True)
	nropatios = models.IntegerField(default=1, null=True, blank=True)
	nroareatalleres = models.IntegerField(default=1, null=True, blank=True)
	nroareaprepalimentos = models.IntegerField(default=1, null=True, blank=True)
	nroretenidos = models.IntegerField(default=1, null=True, blank=True)
	nroretenidoshombres = models.IntegerField(default=1, null=True, blank=True)
	nroretenidosmujeres = models.IntegerField(default=1, null=True, blank=True)
	capacidad = models.IntegerField(default=1, null=True, blank=True)
	pobregultimavisita = models.IntegerField(default=1, null=True, blank=True)
	inspeccionanterior = models.BooleanField(default=False)
	fechaultinspeccion = models.DateTimeField(null=True, blank=True)	
	conceptoanterior = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True, \
	related_name="carcel_concepto_anterior")
	porcumplimientoanterior = models.FloatField(default=0, null=True, blank=True)
	nroactanterior=models.CharField(max_length=15, null=True, blank=True)
	motivovisita = models.ForeignKey(MotivoVisita, on_delete=models.CASCADE, null=True, blank=True)
	tipoacta = models.ForeignKey(TipoActa, on_delete=models.CASCADE)
	concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True, related_name="carcel_concepto")
	puntaje = models.FloatField(default=0)
	nroadministativos = models.IntegerField(default=1, null=True, blank=True)
	nrooperativos = models.IntegerField(default=1, null=True, blank=True)
	nroafiliadosarl = models.IntegerField(default=1, null=True, blank=True)
	nroafiliadosegsocial = models.IntegerField(default=1, null=True, blank=True)
	gestoresiduohospitalario = models.ForeignKey(GestoResiduoHospitalario, on_delete=models.CASCADE, null=True, blank=True)
	nromuestrastomadas = models.IntegerField(default=0, null=True, blank=True)
	nroactatomamuestra=models.CharField(max_length=15, null=True, blank=True)
	requerimiento = models.TextField(null=True, blank=True)
	observacionautsan = models.TextField(null=True, blank=True)
	observacionestable = models.TextField(null=True, blank=True)
	clausuratemptotal = models.BooleanField(default=False, verbose_name='Clausura temporal total')
	clausuratemparcial = models.BooleanField(default=False, verbose_name='Clausura temporal parcial')
	susparcialtrabajo = models.BooleanField(default=False, verbose_name='Suspensión parcial de trabajos o servicios')
	susptotaltrabservicio = models.BooleanField(default=False, verbose_name='Suspensión total de trabajos o servicios')
	aislamiento = models.BooleanField(default=False, verbose_name='Aislamiento o internación de personas para evitar la transmisión de enfermedades')
	decomiso = models.BooleanField(default=False, verbose_name='Decomiso')
	destruccion = models.BooleanField(default=False, verbose_name='Destrucción o desnaturalización')
	congelacion = models.BooleanField(default=False, verbose_name='Congelación')
	capturanimales = models.BooleanField(default=False, verbose_name='Captura y observación de animales sospechosos de enfermedades transmisibles')
	vacunacion = models.BooleanField(default=False, verbose_name='Vacunación personas o animales')	
	controlinsectos = models.BooleanField(default=False, verbose_name='Control de insectos u otra fauna nociva o transmisora de enfermedades')
	desocupacion = models.BooleanField(default=False, verbose_name='Desocupación o desalojamiento de establecimientos o vivienda')
	nroactamedidasanitaria = models.CharField(max_length=20, null=True, blank=True)
	diashabileplazo = models.IntegerField(default=0, null=True, blank=True)
	fechainiplazo=models.DateField(null=True, blank=True)
	fechafinplazo=models.DateField(null=True, blank=True)

	class Meta:
		verbose_name_plural="Acta visita a centros carcelarios"

		ordering = ['-fecha']

	def __str__(self):
		return "{}-{}".format(self.fecha, self.establecimiento)

@receiver(pre_save, sender=ActaCentroCarcelario)
def actaCentroCarcelario_guardar(sender,instance,**kwargs):
	puntaje = ItemActaCentroCarcelario.objects.filter(actacentrocarcelario_id = instance.id).aggregate(total_puntaje=Sum('puntaje'))
	if puntaje['total_puntaje'] != None:
		instance.puntaje = puntaje['total_puntaje']
		condsanitaria = obtener_cumplimiento_condiciones_sanitarias(instance.tipoacta_id,  puntaje['total_puntaje'])
	
		if condsanitaria:
			instance.concepto_id = condsanitaria.id
	
	
class ItemActaCentroCarcelario(ClaseModelo2):
	actacentrocarcelario = models.ForeignKey(ActaCentroCarcelario, on_delete=models.CASCADE)
	pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	evaluacion=models.ForeignKey(Evaluacion, on_delete=models.CASCADE, default=3)
	puntaje=models.FloatField(default=0)
	habilitada=models.BooleanField(default=True)

	def __str__(self):
		return "{}".format(self.pregunta)

@receiver(pre_save, sender=ItemActaCentroCarcelario)
def itemActaCentroCarcelario_guardar(sender,instance,**kwargs):
	evalpregunta = EvaluacionPregunta.objects.filter(pregunta_id = instance.pregunta_id).filter(evaluacion_id=instance.evaluacion_id).first()

	if evalpregunta:
		instance.puntaje = evalpregunta.puntaje
	else:
		instance.puntaje = 0 

class FuncionariosActaCentroCarcelario(ClaseModelo2):
	actacentrocarcelario = models.ForeignKey(ActaCentroCarcelario, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)

	def __str__(self):
		return "{}".format(self.funcionario)

class AtiendeActaCentroCarcelario(ClaseModelo2):
	actacentrocarcelario = models.ForeignKey(ActaCentroCarcelario, on_delete=models.CASCADE)
	tipodoc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
	identificacion = models.CharField(max_length=20)
	nombre=models.CharField(max_length=150)	
	cargo=models.CharField(max_length=80, null=True, blank=True)

	def __str__(self):
		return "{}".format(self.nombre)
#----------------------------


#Actas vigilancia Droguerias y farmacias
class ActaDrogueria(ClaseModelo2):
	fecha = models.DateTimeField()	
	nroacta=models.CharField(max_length=15)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)	
	tipodocdirtec = models.ForeignKey(Tipodoc, on_delete=models.CASCADE, null=True, blank=True)
	identificaciondirtec = models.CharField(max_length=20, null=True, blank=True)
	nombredirtec = models.CharField(max_length=150, null=True, blank=True)
	perfildirector = models.ForeignKey(PerfilDirector, on_delete=models.CASCADE, null=True, blank=True)
	resolucionapertura = models.BooleanField(default=True)
	funcionantes1992 = models.BooleanField(default=False)
	resoluciontraslado = models.BooleanField(default=False)
	tipoautorizacion =models.CharField(max_length=255, blank=True, null=True)
	inspeccionanterior = models.BooleanField(default=False)
	fechaultinspeccion = models.DateTimeField(null=True, blank=True)	
	conceptoanterior = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True, \
	related_name="drogueria_concepto_anterior")
	porcumplimientoanterior = models.FloatField(default=0, null=True, blank=True)
	nroactanterior=models.CharField(max_length=15, null=True, blank=True)	
	tipoacta = models.ForeignKey(TipoActa, on_delete=models.CASCADE)
	concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True, related_name="drogueria_concepto")
	puntaje = models.FloatField(default=0)	
	nroadministativos = models.IntegerField(default=1, null=True, blank=True)
	nrooperativos = models.IntegerField(default=1, null=True, blank=True)
	requerimiento = models.TextField(null=True, blank=True)
	observacionautsan = models.TextField(null=True, blank=True)
	observacionestable = models.TextField(null=True, blank=True)
	diashabileplazo = models.IntegerField(default=0, null=True, blank=True)
	fechainiplazo=models.DateField(null=True, blank=True)
	fechafinplazo=models.DateField(null=True, blank=True)

	class Meta:
		verbose_name_plural="Acta visita a droguerías y farmacias"
		ordering = ['-fecha']

	def __str__(self):
		return "{}-{}".format(self.fecha, self.establecimiento)

@receiver(pre_save, sender=ActaDrogueria)
def actaCentroCarcelario_guardar(sender,instance,**kwargs):
	puntaje = ItemActaDroguerias.objects.filter(actadrogueria_id = instance.id).aggregate(total_puntaje=Sum('puntaje'))
	if puntaje['total_puntaje'] != None:
		instance.puntaje = puntaje['total_puntaje']
		condsanitaria = obtener_cumplimiento_condiciones_sanitarias(instance.tipoacta_id,  puntaje['total_puntaje'])
	
		if condsanitaria:
			instance.concepto_id = condsanitaria.id
	
	
class ItemActaDroguerias(ClaseModelo2):
	actadrogueria = models.ForeignKey(ActaDrogueria, on_delete=models.CASCADE)
	pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	evaluacion=models.ForeignKey(Evaluacion, on_delete=models.CASCADE, default=3)
	puntaje=models.FloatField(default=0)
	habilitada=models.BooleanField(default=True)

	def __str__(self):
		return "{}".format(self.pregunta)

@receiver(pre_save, sender=ItemActaDroguerias)
def itemActaCentroCarcelario_guardar(sender,instance,**kwargs):
	evalpregunta = EvaluacionPregunta.objects.filter(pregunta_id = instance.pregunta_id).filter(evaluacion_id=instance.evaluacion_id).first()

	if evalpregunta:
		instance.puntaje = evalpregunta.puntaje
	else:
		instance.puntaje = 0 

class FuncionariosActaDrogueria(ClaseModelo2):
	actadrogueria = models.ForeignKey(ActaDrogueria, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)

	def __str__(self):
		return "{}".format(self.funcionario)

class AtiendeActaDrogueria(ClaseModelo2):
	actadrogueria = models.ForeignKey(ActaDrogueria, on_delete=models.CASCADE)
	tipodoc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
	identificacion = models.CharField(max_length=20)
	nombre=models.CharField(max_length=150)	
	cargo=models.CharField(max_length=80, null=True, blank=True)

	def __str__(self):
		return "{}".format(self.nombre)
#----------------------------

