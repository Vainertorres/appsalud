from django.db import models


from cnf.models import ClaseModelo2, Ips, Eps, Tipodoc, Paciente, Ocupacion, \
Escolaridad, Pais, Departamento, Municipio

# Create your models here.


class Gestante(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Gestante'

	def __str__(self):
		return "{}".format(self.descripcion)


class Sifilisges(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Sifilis gestacional'

	def __str__(self):
		return "{}".format(self.descripcion)


class Pruminimental(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de la prueba mini - mental'

	def __str__(self):
		return "{}".format(self.descripcion)


class Hipotiroidismo(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Hipotiroidismo congénito'

	def __str__(self):
		return "{}".format(self.descripcion)


class Sintomaticoresp(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Sintomático respiratorio'

	def __str__(self):
		return "{}".format(self.descripcion)


class Consumo_tabaco(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Consumo de tabaco'

	def __str__(self):
		return "{}".format(self.descripcion)

class Lepra(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Lepra'

	def __str__(self):
		return "{}".format(self.descripcion)


class Obecidad_desnutricion(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Obecidad desnutrición, proteico calórica'

	def __str__(self):
		return "{}".format(self.descripcion)


class Tacto_rectal(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Resultado del Tacto rectal'

	def __str__(self):
		return "{}".format(self.descripcion)

class Acido_folico(ClaseModelo2): #23
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Ácido fólico preconcepcional'

	def __str__(self):
		return "{}".format(self.descripcion)


class Sangre_matfecal(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Resultado de la prueba de sangre en materia fecal'

	def __str__(self):
		return "{}".format(self.descripcion)


class Enfermedad_mental(ClaseModelo2):
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Enfermedad mental'

	def __str__(self):
		return "{}".format(self.descripcion)

class Cancer_cervix(ClaseModelo2): #26
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Cáncer de cervix'

	def __str__(self):
		return "{}".format(self.descripcion)

class Agudeza_visual_ojoizq(ClaseModelo2): #27
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Agudeza visual lejana ojo izquierdo'

	def __str__(self):
		return "{}".format(self.descripcion)


class Agudeza_visual_ojoder(ClaseModelo2): #27
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Agudeza visual lejana ojo derecho'

	def __str__(self):
		return "{}".format(self.descripcion)


class Riesgo_gestacional(ClaseModelo2): #35
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Clasificación del riesgo gestacional'

	def __str__(self):
		return "{}".format(self.descripcion)


class Colonoscopia(ClaseModelo2): #36
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Resultado de colonoscopia tamizaje'

	def __str__(self):
		return "{}".format(self.descripcion)


class Tamizaje_auditivo_neonatal(ClaseModelo2): #37
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Tamizaje auditivo neonatal'

	def __str__(self):
		return "{}".format(self.descripcion)

class Tamizaje_visual_neonatal(ClaseModelo2): #38
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Tamizaje visual neonatal'

	def __str__(self):
		return "{}".format(self.descripcion)

class Dpt(ClaseModelo2): #39
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'DPT'

	def __str__(self):
		return "{}".format(self.descripcion)

class Tamizaje_vale(ClaseModelo2): #40
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Tamizaje VALE'

	def __str__(self):
		return "{}".format(self.descripcion)

class Neumococo(ClaseModelo2): #41
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Neumococo'

	def __str__(self):
		return "{}".format(self.descripcion)

class Hepatitisc(ClaseModelo2): #42
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Hepatitis C'

	def __str__(self):
		return "{}".format(self.descripcion)


class Motricidad_gruesa(ClaseModelo2): #43
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Escala abreviada de desarrollo Motricidad gruesa'

	def __str__(self):
		return "{}".format(self.descripcion)

class Motricidad_finoadaptativa(ClaseModelo2): #44
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Escala abreviada de desarrollo Motricidad finoadaptativa'

	def __str__(self):
		return "{}".format(self.descripcion)		

class Personal_social(ClaseModelo2): #45
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Escala abreviada de desarrollo área personal social'

	def __str__(self):
		return "{}".format(self.descripcion)

class Motricidad_audicion_lenguaje(ClaseModelo2): #46
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)


	class Meta:
		verbose_name = 'Escala abreviada de desarrollo área Motricidad audición lenguaje'

	def __str__(self):
		return "{}".format(self.descripcion)	


class Tratamiento_ablativo(ClaseModelo2): #47
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Tratamiento ablativo (Crioterapia o LETZ)'

	def __str__(self):
		return "{}".format(self.descripcion)	

class Oximetria(ClaseModelo2): #48
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de tamización con Oximetría'

	def __str__(self):
		return "{}".format(self.descripcion)

class Metodo_anticonceptivo(ClaseModelo2): #54
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Método anticonceptivo'

	def __str__(self):
		return "{}".format(self.descripcion)

class Acido_folico_ctrlpren(ClaseModelo2): #59
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Suministro de ácido fólico en el control prenatal'

	def __str__(self):
		return "{}".format(self.descripcion)

class Sulfato_ferroso_ctrlpren(ClaseModelo2): #60
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Suministro de sultado ferroso en el control prenatal'

	def __str__(self):
		return "{}".format(self.descripcion)

class Carbonato_calcio_ctrlpren(ClaseModelo2): #61
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Suministro de carbonato de calcio en el control prenatal'

	def __str__(self):
		return "{}".format(self.descripcion)

class Fortificacion_cacera_prinfancia(ClaseModelo2): #70
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Suministro de Fortificación casera en la primera infancia'
		verbose_name_plural = 'Suministros de Fortificación casera en la primera infancia'


	def __str__(self):
		return "{}".format(self.descripcion)

class Vitamina_a_prinfancia(ClaseModelo2): #71
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Vitamina A en la primera infancia'

	def __str__(self):
		return "{}".format(self.descripcion)

class Hierro_prinfancia(ClaseModelo2): #77
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Suministro de Hierro en la primera infancia'

	def __str__(self):
		return "{}".format(self.descripcion)

class Antigeno_hep_b(ClaseModelo2): #79
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de Antígeno de superficie Hep B'

	def __str__(self):
		return "{}".format(self.descripcion)

class Prueba_sifilis(ClaseModelo2): #81
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de prueba tamizaje para sifilis'

	def __str__(self):
		return "{}".format(self.descripcion)

class Prueba_vih(ClaseModelo2): #83
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de prueba para VIH'

	def __str__(self):
		return "{}".format(self.descripcion)

class Prueba_tsh(ClaseModelo2): #85
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de TSH neonatal'

	def __str__(self):
		return "{}".format(self.descripcion)

class Tamizaje_cancer_cuello_uterino(ClaseModelo2): #86
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Tamizaje del cáncer de cuello uterino'

	def __str__(self):
		return "{}".format(self.descripcion)

class Res_tam_cancer_cue_ute(ClaseModelo2): #88
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado Tamizaje cáncer de cuello uterino'

	def __str__(self):
		return "{}".format(self.descripcion)

class Calidad_muestra_citologia(ClaseModelo2): #89
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Calidad en la muestra de citología cervicouterina'

	def __str__(self):
		return "{}".format(self.descripcion)


class Res_biopsia_cervicouterina(ClaseModelo2): #94
	codigo = models.CharField(max_length=2, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de biopsia cervicouterina'

	def __str__(self):
		return "{}".format(self.descripcion)

class Res_mamografia(ClaseModelo2): #97
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de mamografía'

	def __str__(self):
		return "{}".format(self.descripcion)

class Res_biopsia_mama(ClaseModelo2): #101
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de biopsia de mama'

	def __str__(self):
		return "{}".format(self.descripcion)


class Res_bk_diag(ClaseModelo2): #113
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Resultado de baciloscopia de diagnóstico'

	def __str__(self):
		return "{}".format(self.descripcion)


class Riesgo_cardiovascular(ClaseModelo2): #114
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Clasificación del riesgo cardiovascular'

	def __str__(self):
		return "{}".format(self.descripcion)

class Trat_sifilis_gest(ClaseModelo2): #115
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Tratamiento para sifilis gestional'

	def __str__(self):
		return "{}".format(self.descripcion)	


class Trat_sifilis_congenita(ClaseModelo2): #116
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Tratamiento para sifilis congénita'

	def __str__(self):
		return "{}".format(self.descripcion)	

class Riesgo_metabolico(ClaseModelo2): #117
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Clasificación del riesgo metabólico'
		verbose_name_plural = 'Clasificación del riesgo metabólico'


	def __str__(self):
		return "{}".format(self.descripcion)

class Resolucion4505ctrl(ClaseModelo2): 
	tiporegistro = models.IntegerField(default=1)
	codigoentidad=models.CharField(max_length=6)
	eps=models.ForeignKey(Eps, on_delete=models.CASCADE, null=True, blank=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
	fechainicial = models.DateField()
	fechafinal = models.DateField()
	nrototalreg = models.IntegerField(default=0)
	actual = models.BooleanField(default=False)

	class Meta:
		verbose_name='Registro tipo 1 Res: 4505 - Act: 202 - 2021'

	def __str__(self):
		return "{} {} {} : {} - {}".format( self.eps, self.municipio, self.departamento, self.fechainicial, self.fechafinal )


class Resolucion4505det(ClaseModelo2): 
	resolucion4505ctrl = models.ForeignKey(Resolucion4505ctrl, on_delete=models.CASCADE, related_name='regtipo1')
	tiporegistro = models.IntegerField(default=2)
	consecutivo = models.IntegerField()
	ips = models.ForeignKey(Ips, on_delete=models.CASCADE, related_name='ips4505')
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente4505')
	ocupacion = models.ForeignKey(Ocupacion, on_delete=models.CASCADE, related_name='ocupacion4505')
	escolaridad = models.ForeignKey(Escolaridad, on_delete=models.CASCADE, related_name='escolaridad4505')
	gestante = models.ForeignKey(Gestante, on_delete=models.CASCADE, related_name='gestante4505')
	sifilisges = models.ForeignKey(Sifilisges, on_delete=models.CASCADE, related_name='sifilisgest4505')
	pruminimental = models.ForeignKey(Pruminimental, on_delete=models.CASCADE, related_name='pruminimental4505')
	hipotiroidismo = models.ForeignKey(Hipotiroidismo, on_delete=models.CASCADE, related_name='hipotiroidismo4505')
	sintomaticoresp = models.ForeignKey(Sintomaticoresp, on_delete=models.CASCADE, related_name='sintomaticoresp4505')
	consumo_tabaco = models.ForeignKey(Consumo_tabaco, on_delete=models.CASCADE, related_name='consumotabaco4505')
	lepra = models.ForeignKey(Lepra, on_delete=models.CASCADE, related_name='lepra4505')
	obecidad_desnutricion = models.ForeignKey(Obecidad_desnutricion, on_delete=models.CASCADE, related_name='obecidaddesnutricion4505')
	tacto_rectal = models.ForeignKey(Tacto_rectal, on_delete=models.CASCADE, related_name='tactorectal4505')
	acido_folico = models.ForeignKey(Acido_folico, on_delete=models.CASCADE, related_name='acidofolico4505')
	sangre_matfecal = models.ForeignKey(Sangre_matfecal, on_delete=models.CASCADE, related_name='sangrematfecal4505')
	enfermedad_mental = models.ForeignKey(Enfermedad_mental, on_delete=models.CASCADE, related_name='enfermedadmental4505')
	cancer_cervix = models.ForeignKey(Cancer_cervix, on_delete=models.CASCADE, related_name='cancercervix4505')
	agudeza_visual_ojoizq = models.ForeignKey(Agudeza_visual_ojoizq, on_delete=models.CASCADE, related_name='agudezavisualojoizq4505')
	agudeza_visual_ojoder = models.ForeignKey(Agudeza_visual_ojoder, on_delete=models.CASCADE, related_name='agudeza_visualojoder4505')
	fechapeso = models.DateField()
	peso = models.FloatField(default=999) #peso en Kilogramos sino se toma = 999
	fechatalla = models.DateField()
	talla = models.IntegerField(default=999) #Talla en centrimetros sino se toma = 999
	fechapp = models.DateField() #Fecha probable de parto Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais4505')
	riesgo_gestacional = models.ForeignKey(Riesgo_gestacional, on_delete=models.CASCADE, related_name='riesgogestacional4505')
	colonoscopia = models.ForeignKey(Colonoscopia, on_delete=models.CASCADE, related_name='colonoscopia4505')
	tamizaje_auditivo_neonatal = models.ForeignKey(Tamizaje_auditivo_neonatal, on_delete=models.CASCADE, related_name='tamizajeauditivo_neonatal4505')
	tamizaje_visual_neonatal = models.ForeignKey(Tamizaje_visual_neonatal, on_delete=models.CASCADE, related_name='tamizajevisualneonatal4505')
	dpt = models.ForeignKey(Dpt, on_delete=models.CASCADE, related_name='dpt4505')
	tamizaje_vale = models.ForeignKey(Tamizaje_vale, on_delete=models.CASCADE, related_name='tamizajevale4505')
	neumococo = models.ForeignKey(Neumococo, on_delete=models.CASCADE, related_name='neumococo4505')
	hepatitisc = models.ForeignKey(Hepatitisc, on_delete=models.CASCADE, related_name='hepatitisc4505')
	motricidad_gruesa = models.ForeignKey(Motricidad_gruesa, on_delete=models.CASCADE, related_name='motricidadgruesa4505')
	motricidad_finoadaptativa = models.ForeignKey(Motricidad_finoadaptativa, on_delete=models.CASCADE, related_name='motricidadfinoadaptativa4505')
	personal_social = models.ForeignKey(Personal_social, on_delete=models.CASCADE, related_name='personalsocial4505')
	motricidad_audicion_lenguaje = models.ForeignKey(Motricidad_audicion_lenguaje, on_delete=models.CASCADE, related_name='motricidadaudicionlenguaje4505')
	tratamiento_ablativo = models.ForeignKey(Tratamiento_ablativo, on_delete=models.CASCADE, related_name='tratamientoablativo4505')
	oximetria = models.ForeignKey(Oximetria, on_delete=models.CASCADE, related_name='oximetria4505')
	fechaparto = models.DateField() #Fecha parto o cesarea Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechasaleatenparto = models.DateField() #Fecha de salida atención parto o cesarea Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatenlatmaterna = models.DateField() #Fecha de salida atención parto o cesarea Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechaconsvalgeneral = models.DateField() #Fecha de salida atención parto o cesarea Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechaseanticoncepcion = models.DateField() #Fecha de salida atención parto o cesarea Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	metodo_anticonceptivo =models.ForeignKey(Metodo_anticonceptivo, on_delete=models.CASCADE, related_name='metodoanticonceptivo4505')
	fecha1raconsultapren = models.DateField() #56 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	glicemia = models.IntegerField(default=998)
	fechaultcontolpren = models.DateField() #56 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	acido_folico_ctrlpren = models.ForeignKey(Acido_folico_ctrlpren, on_delete=models.CASCADE, related_name='acidofolicoctrlpren4505')
	sulfato_ferroso_ctrlpren = models.ForeignKey(Sulfato_ferroso_ctrlpren, on_delete=models.CASCADE, related_name='sulfatoferrosoctrlpren4505')
	carbonato_calcio_ctrlpren = models.ForeignKey(Carbonato_calcio_ctrlpren, on_delete=models.CASCADE, related_name='carbonatocalcioctrlpren4505')
	fechavalaguvisual = models.DateField() #62 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatamizajevale = models.DateField() #63 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatactorectal = models.DateField() #64 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechaoximetria = models.DateField() #65 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechacolonoscopia = models.DateField() #66 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechaprucacolon = models.DateField() #67 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechaconspsicologia = models.DateField() #68 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatamaudineonatal = models.DateField() #69 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fortificacion_cacera_prinfancia = models.ForeignKey(Fortificacion_cacera_prinfancia, on_delete=models.CASCADE, related_name='fortificacioncaceraprinfancia4505')
	vitamina_a_prinfancia = models.ForeignKey(Vitamina_a_prinfancia, on_delete=models.CASCADE, related_name='vitaminaaprinfancia4505')
	fechatomaldl = models.DateField() #72 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatomapsa = models.DateField() #73 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	preservativoscant = models.IntegerField(default=0) #74 Preservaticos entregados a pacientes con ITS
	fechatamvisualneonatal = models.DateField() #75 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatensaludbucal = models.DateField() #76 Fecha primera consulta prenatal  Si no se tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	hierro_prinfancia = models.ForeignKey(Hierro_prinfancia, on_delete=models.CASCADE, related_name='hierroprinfancia4505')
	fechantighepb = models.DateField() #78 Fecha antígeno Hep B sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	antigeno_hep_b = models.ForeignKey(Antigeno_hep_b, on_delete=models.CASCADE, related_name='antigenohepb4505')
	fechatomaprusifilis = models.DateField() #80 Fecha antígeno Hep B sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	prueba_sifilis = models.ForeignKey(Prueba_sifilis, on_delete=models.CASCADE, related_name='pruebasifilis4505')
	fechatomapruvih = models.DateField() #82 Fecha antígeno Hep B sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	prueba_vih = models.ForeignKey(Prueba_vih, on_delete=models.CASCADE, related_name='pruebavih4505')
	fechatomatsh = models.DateField() #84 Fecha antígeno Hep B sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	prueba_tsh = models.ForeignKey(Prueba_tsh, on_delete=models.CASCADE, related_name='pruebatsh4505')
	tamizaje_cancer_cuello_uterino = models.ForeignKey(Tamizaje_cancer_cuello_uterino, on_delete=models.CASCADE, related_name='Tamizajecancercuello_uterino4505')
	fechatamcancercuterino = models.DateField() #87 Fecha antígeno Hep B sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	res_tam_cancer_cue_ute = models.ForeignKey(Res_tam_cancer_cue_ute, on_delete=models.CASCADE, related_name='restamcancercueute4505')
	calidad_muestra_citologia = models.ForeignKey(Calidad_muestra_citologia, on_delete=models.CASCADE, related_name='calidadmuestracitologia4505')
	ipscancercuello =  models.ForeignKey(Ips, on_delete=models.CASCADE, related_name='ipscancercuello4505') #90 Ips donde realiza tamizaje de cancer de cuello uterino
	fechacolposcopia = models.DateField() #91 Fecha antígeno Hep B sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	resultadoldl =  models.IntegerField(default=998)
	fechabiopsiacu = models.DateField() #93 Fecha Biopsia cervico uterina sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	res_biopsia_cervicouterina =  models.ForeignKey(Res_biopsia_cervicouterina, on_delete=models.CASCADE, related_name='resbiopsiacervicouterina4505') #94 Resultado de Biopsia CU
	resultadohdl =  models.IntegerField(default=998)
	fechamamografia = models.DateField() #96 Fecha de mamografía sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	res_mamografia =  models.ForeignKey(Res_mamografia, on_delete=models.CASCADE, related_name='resmamografia4505') #97 Resultado de mamografía
	resultadotrigliceridos =  models.IntegerField(default=998)
	fechatomabiopsiamama = models.DateField() #99 Fecha de toma de biopsia de mama sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fecharesbiopsiamama = models.DateField() #100 Fecha de toma de biopsia de mama sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	res_biopsia_mama = models.ForeignKey(Res_biopsia_mama, on_delete=models.CASCADE, related_name='resbiopsiamama4505') #101
	indicecop = models.IntegerField(default=21)
	fechatomaemoglobina = models.DateField() #103 Fecha de toma de hemoglobina sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	resultadohemoglobina = models.FloatField(default=998)
	fechatomaglisemiabasal = models.DateField() #105 Fecha de toma de glisemia basal sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatomacreatinina = models.DateField() #106 Fecha de toma de Creatinina basal sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	resultadocreatinina = models.FloatField(default=998) #107
	fechaentregapreservativos = models.DateField() #108 Fecha de toma de Creatinina basal sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	resultadopsa = models.FloatField(default=998) #109
	fechatamhepc = models.DateField() #110 Fecha de toma de tamizaje hep C sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatomahdl = models.DateField() #111 Fecha de toma de tamizaje hep C sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	fechatomabk = models.DateField() #112 Fecha de toma de tamizaje hep C sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01
	res_bk_diag = models.ForeignKey(Res_bk_diag, on_delete=models.CASCADE, related_name='resbkdiag4505') #101
	riesgo_cardiovascular = models.ForeignKey(Riesgo_cardiovascular, on_delete=models.CASCADE, related_name='riesgocardiovascular4505') #114
	trat_sifilis_gest = models.ForeignKey(Trat_sifilis_gest, on_delete=models.CASCADE, related_name='tratsifilisgest4505') #115
	trat_sifilis_congenita = models.ForeignKey(Trat_sifilis_congenita, on_delete=models.CASCADE, related_name='tratsifiliscongenita4505') #116
	riesgo_metabolico = models.ForeignKey(Riesgo_metabolico, on_delete=models.CASCADE, related_name='riesgometabolico4505') #117
	fechatomatrigliceridos = models.DateField() #118 Fecha de toma de trigliceridos sino tiene el dato registrar 1800-01-01 - Si no aplica reqistrar 1845-01-01

	class Meta:
		verbose_name='Resolución 4505 - Actualizada 202-2021'


	def __str__(self):
		return "{}".format(self.paciente)







































































































	
	class Meta:
		verbose_name = 'Resolución 4505 - Actualizado 202-2021'
		verbose_name_plural = 'Resolución 4505 - Actualizado 202-2021'


	def __str__(self):
		return "{}".format(self.descripcion)







'''Configuración de los periodos de envío Res 202-2021
antes llamada Resolucion 4505'''
class Periodo_envio(ClaseModelo2): 
	codigo = models.CharField(max_length=10, unique=True)
	descripcion = models.CharField(max_length=80)
	fechaini = models.DateField()
	fechafin = models.DateField()
	fechainiplazo = models.DateField()
	fechafinplazo = models.DateField()

	class Meta:
		verbose_name = 'Periodo de reporte'
		verbose_name_plural = 'Periodos de reportes'


	def __str__(self):
		return "{}".format(self.descripcion)


