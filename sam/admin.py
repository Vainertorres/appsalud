from django.contrib import admin

from .models import Propietario, Concepto, MotivoVisita, Evaluacion, TipoActa, Bloque, \
	                Pregunta, LugarUbica, UnidadSalAmb, Actividad, TipoSujeto, TipoCarga, \
	                Puertos, Embarcaciones, AgenciaNaviera, Visitaen, ObjetivoVisita, \
	                ProductoQuimico, MedidaSanitaria, EvaluacionPregunta, PerfilDirector
# Register your models here.
admin.site.register(Actividad)
admin.site.register(Concepto)
admin.site.register(Propietario)
admin.site.register(MotivoVisita)
admin.site.register(Evaluacion)
admin.site.register(TipoActa)
admin.site.register(Bloque)
admin.site.register(Pregunta)
admin.site.register(LugarUbica)
admin.site.register(UnidadSalAmb)
admin.site.register(TipoSujeto)
admin.site.register(Embarcaciones)
admin.site.register(Puertos)
admin.site.register(TipoCarga)
admin.site.register(AgenciaNaviera)
admin.site.register(Visitaen)
admin.site.register(ObjetivoVisita)
admin.site.register(ProductoQuimico)
admin.site.register(MedidaSanitaria)
admin.site.register(EvaluacionPregunta)
admin.site.register(PerfilDirector)

