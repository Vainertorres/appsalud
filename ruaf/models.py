from django.db import models

from cnf.models import ClaseModelo2, Departamento, Municipio, Area, Ips, Sexo, Etnia, \
Pais, Paciente, Barrio, Eps, Escolaridad, Pueblo_indigena, Regimen, UmEdad

from bai.models import Diagnosticos

# Create your models here.

class Atiende_parto(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Parto atendido por"
        verbose_name_plural="Parto atendido por"
    
    def __str__(self):
        return "{}".format(self.descripcion)

class Multiplicidad_embarazo(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Multiplicidad de embarazo"
        verbose_name_plural="Multiplicidad de embarazos"
    
    def __str__(self):
        return "{}".format(self.descripcion)

class Sitio_parto(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Sitio del parto"
        verbose_name_plural="Sitios donde se produjo el parto"
        
    
    def __str__(self):
        return "{}".format(self.descripcion)

class Tipo_parto(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Tipo de parto"
        verbose_name_plural="Tipos de partos"
    
    def __str__(self):
        return "{}".format(self.descripcion)

class Nacido_vivo(ClaseModelo2):
    nrocertificado = models.CharField(max_length=20, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='dpto_nto')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='mpio_nto')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True, related_name='area_nace')
    sitio_parto = models.ForeignKey(Sitio_parto, on_delete=models.CASCADE, blank=True, null=True)
    ips = models.ForeignKey(Ips, on_delete=models.CASCADE, null=True, blank=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, null=True, blank=True)
    peso = models.IntegerField(default = 0, null=True, blank=True)
    talla = models.IntegerField(default=0, null=True, blank = True)
    fechanac = models.DateField()
    horanac = models.TimeField(null=True, blank=True)
    tiempo_gestacion=models.IntegerField(default=0, null=True, blank=True)
    nroconsultapren=models.IntegerField(default=0, null=True, blank=True)    
    tipo_parto = models.ForeignKey(Tipo_parto, on_delete=models.CASCADE, null=True, blank=True)
    multiplicidad_embarazo = models.ForeignKey(Multiplicidad_embarazo, on_delete=models.CASCADE, null=True, blank=True)
    apgar1 = models.IntegerField(default=0, null=True, blank=True)
    apgar5 = models.IntegerField(default=0, null=True, blank=True)
    gruposanguineo = models.CharField(max_length=2, null=True, blank=True)
    factor_rh = models.CharField(max_length=10, null=True, blank=True)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE, null=True, blank = True)
    pueblo_indigena=models.CharField(max_length=150, null=True, blank=True)
    paisnac = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True, related_name="pais_nac")
    madre = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True, related_name="rltd_madre")
    edad_madre = models.IntegerField(default=0, null=True, blank=True)
    nrohijosnv = models.IntegerField(default=0, null=True, blank=True)
    nroembarazos = models.IntegerField(default=0, null=True, blank=True)
    edad_padre = models.IntegerField(default=0, null=True, blank=True)
    certificador = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True, related_name='certificador')
    fecharegistro = models.DateField(null=True, blank=True)
    fechaultmod = models.DateField(null=True, blank=True)
    eps=models.ForeignKey(Eps, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name="Certificado de nacido vivo"
        
    def __str__(self):
        return "{} - {}".format(self.fecharegistro, self.madre)


class SeguimientoBajoPeso(ClaseModelo2):
    SINO = (
        ('1', 'Si'),
        ('2', 'No'),
    )
    nacido_vivo = models.ForeignKey(Nacido_vivo, on_delete=models.CASCADE)
    fecha=models.DateField()
    hallazgos = models.TextField()
    educacion = models.CharField(max_length=1, choices=SINO, null=True, blank=True)
    icbf = models.CharField(max_length=1, choices=SINO, null=True, blank=True)
    nutricionista = models.CharField(max_length=1, choices=SINO, null=True, blank=True)
    peso = models.IntegerField(default = 0, null=True, blank=True)
    talla = models.IntegerField(default=0, null=True, blank = True)
    perimetro_cefalico = models.IntegerField(default=0, null=True, blank = True)
    perimetro_toraxico = models.IntegerField(default=0, null=True, blank = True)


    class Meta:
        verbose_name='Seguimiento bajo peso al nacer'

class FileNacidoVivo(ClaseModelo2):
    nacido_vivo = models.ForeignKey(Nacido_vivo, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='ruaf/nv/', null=True, blank=True)

    class Meta:
        verbose_name_plural="Archivos nacidos vivos"

    def __str__(self):
        return "{}".format(self.descripcion)


class Sitio_defuncion(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Sitio de defunción"
        verbose_name_plural="Sitios de defunciones"
        
    def __str__(self):
        return "{}".format(self.descripcion)


class Clase_muerte(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Clase de defunción"
        verbose_name_plural="Clases de defunciones"
        
    def __str__(self):
        return "{}".format(self.descripcion)

class Certificador_muerte(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Certificador de defunción"
        verbose_name_plural="Certificadores de defunciones"
        
    def __str__(self):
        return "{}".format(self.descripcion)

class Muerte_parto(ClaseModelo2):
    codigo=models.CharField(max_length=3, unique=True)
    descripcion = models.CharField(max_length=80)
    
    class Meta:
        verbose_name="Muerte relacionada con parto"
        verbose_name_plural="Muerte relacionada con parto"
        
    def __str__(self):
        return "{}".format(self.descripcion)


class Mortalidad_ruaf(ClaseModelo2):
    nrocertificado=models.CharField(max_length=20, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True, related_name='dpto_def')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True, related_name='mpio_def')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True, related_name='area_def')
    sitio_defuncion = models.ForeignKey(Sitio_defuncion, on_delete=models.CASCADE, blank=True, null=True)
    otro_sitio = models.CharField(max_length=150, null=True, blank=True)
    ips = models.ForeignKey(Ips, on_delete=models.CASCADE, null=True, blank=True)
    fechadef=models.DateField()
    horadef=models.TimeField(null=True, blank=True)
    horasinestablecer=models.CharField(max_length=10, default='NO', null=True, blank=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais_nac_def', null=True, blank=True)
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="paciente_difunto")
    edad=models.IntegerField(null=True, blank=True, default=0)
    escolaridad = models.ForeignKey(Escolaridad, on_delete=models.CASCADE, null=True, blank=True)
    ocupacion_relacionada=models.BooleanField(null=True, blank=True, default=False)
    ocupacion_asociado_mte = models.CharField(max_length=255, null=True, blank=True)
    ocupacion_habitual = models.CharField(max_length=255, null=True, blank=True)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE, null=True, blank=True)    
    pueblo_indigena = models.ForeignKey(Pueblo_indigena, on_delete=models.CASCADE, null=True, blank=True)
    pais_reside = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True, null=True, related_name='pais_reside_def')
    departamento_reside = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True, related_name='dpto_reside_def')
    municipio_reside = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=True, null=True, related_name='mpio_reside_def')
    direccion = models.CharField(max_length=255, null=True, blank=True)
    regimen = models.ForeignKey(Regimen, on_delete=models.CASCADE, null=True, blank=True)
    eps = models.ForeignKey(Eps, on_delete=models.CASCADE, null=True, blank=True)
    clase_muerte = models.ForeignKey(Clase_muerte, on_delete=models.CASCADE, null=True, blank=True)
    certificador_muerte = models.ForeignKey(Certificador_muerte, on_delete=models.CASCADE, null=True, blank=True)
    muerte_parto = models.ForeignKey(Muerte_parto, on_delete=models.CASCADE, null=True, blank=True)
    tipo_parto = models.ForeignKey(Tipo_parto, on_delete=models.CASCADE, null=True, blank=True)
    multiplicidad_embarazo = models.ForeignKey(Multiplicidad_embarazo, on_delete=models.CASCADE, null=True, blank=True)
    tiempo_gestacion=models.IntegerField(default=0, null=True, blank=True)
    tiempo_gest_ignorado=models.CharField(max_length=20, null=True, blank=True)
    pesorn = models.IntegerField(default=0, null=True, blank=True)
    madre = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True, related_name="madre_def")
    realizo_cirugia = models.CharField(max_length=20, null=True, blank=True)
    fecha_cirugia = models.DateField(null=True, blank=True)
    motivo_cirugia = models.CharField(max_length=255, null=True, blank=True)
    necrosia_medleg = models.CharField(max_length=20, null=True, blank=True)
    necrosia_clinica = models.CharField(max_length=20, null=True, blank=True)
    historia_clinica = models.CharField(max_length=20, null=True, blank=True)
    prueba_diagnostica = models.CharField(max_length=20, null=True, blank=True)
    interrpgatorio_familiar = models.CharField(max_length=20, null=True, blank=True)
    vigilancia_demografica = models.CharField(max_length=20, null=True, blank=True)
    recibio_atencion_medica = models.CharField(max_length=20, null=True, blank=True)
    muerte_sin_certificacion = models.CharField(max_length=255, null=True, blank=True)
    diagnosticoa = models.ForeignKey(Diagnosticos, on_delete=models.CASCADE, null=True, blank=True, related_name="diagnosticoA_def")
    tiempodiaga = models.IntegerField(default=0, null=True, blank=True)
    umedada = models.ForeignKey(UmEdad, on_delete=models.CASCADE, blank=True, null=True, related_name="umedada_def")
    diagnosticob = models.ForeignKey(Diagnosticos, on_delete=models.CASCADE, null=True, blank=True, related_name="diagnosticoB_def")
    tiempodiagb = models.IntegerField(default=0, null=True, blank=True)
    umedadb = models.ForeignKey(UmEdad, on_delete=models.CASCADE, blank=True, null=True, related_name="umedadb_def")
    diagnosticoc = models.ForeignKey(Diagnosticos, on_delete=models.CASCADE, null=True, blank=True, related_name="diagnosticoC_def")
    tiempodiagc = models.IntegerField(default=0, null=True, blank=True)
    umedadc = models.ForeignKey(UmEdad, on_delete=models.CASCADE, blank=True, null=True, related_name="umedadc_def")
    diagnosticod = models.ForeignKey(Diagnosticos, on_delete=models.CASCADE, null=True, blank=True, related_name="diagnosticoD_def")
    tiempodiagd = models.IntegerField(default=0, null=True, blank=True)
    umedadd = models.ForeignKey(UmEdad, on_delete=models.CASCADE, blank=True, null=True, related_name="umedadd_def")
    otros_estados_pat = models.CharField(max_length=255, null=True, blank=True, verbose_name="Otros estados patológicos")
    certificador = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True, related_name="certificador_muerte")

    class Meta:
        verbose_name="Defunción Ruaf"
        verbose_name_plural="Defunciones Ruaf"

    def __str__(self):
        return "Certificado Nro: {} Fecha def: {} - {}".format(self.nrocertificado, self.fechadef, self.paciente)

    
















    

    


    

    


    












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
 




