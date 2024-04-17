from django.contrib import admin

from .models import Sitio_parto, Atiende_parto, Multiplicidad_embarazo, Tipo_parto, \
Sitio_defuncion, Clase_muerte, Certificador_muerte, Muerte_parto
# Register your models here.

admin.site.register(Sitio_parto)
admin.site.register(Atiende_parto)
admin.site.register(Clase_muerte)
admin.site.register(Certificador_muerte)
admin.site.register(Multiplicidad_embarazo)
admin.site.register(Muerte_parto)
admin.site.register(Tipo_parto)
admin.site.register(Sitio_defuncion)







