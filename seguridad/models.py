from django.db import models

# Create your models here.

from cnf.models import ClaseModelo2, Departamento, Municipio, Paciente, Barrio, Organismo_de_socorro

class Acciones(ClaseModelo2):
	codigo = models.CharField(max_length=3, unique=True)
	descripcion = models.CharField(max_length=80)

	class Meta:
		verbose_name = 'Acción desencadenante de muerte violenta'
		verbose_name = 'Acciones desencadenantes de muertes violentas'

	def __str__(self):
		return "{}".format(self.descripcion)


class Casos(ClaseModelo2):
	fecha = models.DateField()
	descripcion = models.TextField()
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, null=True, blank=True)
	direccion = models.CharField(max_length=150)
	lat = models.CharField(max_length=20, blank = True, null=True, default='SD')
	lon = models.CharField(max_length=20, blank=True, null=True, default='SD')
	acciones = models.ForeignKey(Acciones, on_delete=models.CASCADE)

class Afectados(ClaseModelo2):
	ESTADO = (
		('FAL', 'FALLECIDO'),
		('HER', 'HERIDO'),
		('ILE','ILESO'),
		)
	casos = models.ForeignKey(Casos, on_delete=models.CASCADE)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	estadofinal = models.CharField(max_length=3, choices=ESTADO, null=True, blank=True) 

	def __str__(self):
		return "{}".format(self.paciente)

class Organismos_atiende(ClaseModelo2):
	casos = models.ForeignKey(Casos, on_delete=models.CASCADE)	
	organismo_de_socorro = models.ForeignKey(Organismo_de_socorro, on_delete=models.CASCADE)
	descripcion = models.TextField(null=True, blank=True)

	class Meta:
		verbose_name = 'Organismos de socorro intevinientes'

	def __str__(self):
		return "{}".format(self.organismo_de_socorro)
	




