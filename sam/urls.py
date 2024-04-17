from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from cnf.views import Sin_privilegio
from django.views import generic

from .views import PropietarioList, PropietarioEdit, PropietarioCreate, EstablecimientoList, \
EstablecimientoCreate, EstablecimientoEdit, homesam, EstablecimientoEducativoList, \
establecimientoEducativoCreate, ActageneralList, ActaGeneralCreate, ActaGeneralUpdate, \
delete_actageneralfuncionarios, delete_atiendeactageneral, EmbarcacionesList, EmbarcacionesCreate, \
EmbarcacionesEdit, ActaEmbarInternalList, ActaEmbarcacionInterCreate, ActaEmbarcacionInterUpdate, \
delete_actaembarcacioninterfuncionarios, delete_actaembarcacioninterimo, delete_actaembarcacioninterpuerto, \
ActaBodegasPatiosList, ActaBodegasPatiosCreate, ActaBodegasPatiosUpdate, delete_productoquimicoactabodegaspatios, \
delete_itemactabodegaspatios, delete_funcionariosactabodegaspatios, delete_atiendeactabodegaspatios, \
delete_medidasanitariaactabodegaspatios, ActaBodegasPatiosList, ActaViviendaTransitoriaList, \
ActaViviendaTransitoriaCreate, ActaViviendaTransitoriaUpdate, delete_itemactaviviendatransitoria, \
delete_atiendeactaviviendatransitoria, delete_funcionariosactaviviendatransitoria, PreguntaList, \
TipoActaList, EvaluacionPreguntaCreate, EvaluacionPreguntaUpdate, delete_evaluacionpregunta, \
ActaCentroCarcelarioList, delete_atiendeactacentrocarcelario, delete_funcionariosactacentrocarcelario, \
delete_itemactacentrocarcelario, ActaCentroCarcelarioUpdate, ActaCentroCarcelarioCreate, \
ActaDrogueriaList, ActaDrogueriaUpdate, ActaDrogueriaCreate, delete_itemactadroguerias, \
delete_funcionariosactadrogueria, delete_atiendeactadrogueria

app_name='sam'

urlpatterns = [

path('propietario', PropietarioList.as_view(), name='propietario_list'),
path('propietario/new', PropietarioCreate.as_view(), name='propietario_new'),
path('propietario/edit/<int:pk>', PropietarioEdit.as_view(), name='propietario_edit'),
path('establecimiento/<int:id>', EstablecimientoList.as_view(), name='establecimiento_list'),
path('establecimiento/new', EstablecimientoCreate.as_view(), name='establecimiento_new'),
path('establecimiento/edit/<int:pk>', EstablecimientoEdit.as_view(), name='establecimiento_edit'),
path('home', homesam, name='home'),
path('actaestedu/list/<int:pk>', EstablecimientoEducativoList.as_view(), name='actaestedu_list'),
path('actaestedu/new/<int:estaedu_id>', establecimientoEducativoCreate, name='actaestedu_new'),
path('actaestedu/update/<int:estaedu_id>/<int:idacta>', establecimientoEducativoCreate, name='actaestedu_update'),
path('actagral/list/<int:pk>', ActageneralList.as_view(), name='actagral_list'),
path('actagral/add/<int:idest>', ActaGeneralCreate.as_view(), name='actagral_create'),
path('actagral/edit/<int:idest>/<int:pk>',ActaGeneralUpdate.as_view(), name='actagral_edit'),
path('delete/actageneralfuncionarios/<int:pk>', delete_actageneralfuncionarios, name='delete_actageneralfuncionarios'),
path('delete/atiendeactageneral/<int:pk>', delete_atiendeactageneral, name='delete_atiendeactageneral'),
path('embarcacion/<int:id>', EmbarcacionesList.as_view(), name='embarcacion_list'),
path('embarcacion/new', EmbarcacionesCreate.as_view(), name='embarcacion_new'),
path('embarcacion/edit/<int:pk>', EmbarcacionesEdit.as_view(), name='embarcacion_edit'),
path('actaembint/list/<int:pk>', ActaEmbarInternalList.as_view(), name='actaembint_list'),
path('actaembint/add/<int:idemb>', ActaEmbarcacionInterCreate.as_view(), name='actaembint_create'),
path('actaembint/edit/<int:idemb>/<int:pk>', ActaEmbarcacionInterUpdate.as_view(), name='actaembint_edit'),
path('delete/actaembinterfunc/<int:pk>', delete_actaembarcacioninterfuncionarios, name='delete_actaembinterfunc'),
path('delete/actaembinterimo/<int:pk>', delete_actaembarcacioninterimo, name='delete_actaembinterimo'),
path('delete/actaembinterpuerto/<int:pk>', delete_actaembarcacioninterpuerto, name='delete_actaembinterpuerto'),
path('actabodpat/list/<int:pk>', ActaBodegasPatiosList.as_view(), name='actabodpat_list'),
path('actabodpat/add/<int:idest>', ActaBodegasPatiosCreate.as_view(), name='actabodpat_create'),
path('actabodpat/edit/<int:idest>/<int:pk>', ActaBodegasPatiosUpdate.as_view(), name='actabodpat_edit'),
path('delete/actabypproducto/<int:pk>', delete_productoquimicoactabodegaspatios, name='delete_actabypproducto'),
path('delete/actabypevalua/<int:pk>', delete_itemactabodegaspatios, name='delete_actabypevalua'),
path('delete/actabypmedsan/<int:pk>', delete_medidasanitariaactabodegaspatios, name='delete_actabypmedsan'),
path('delete/actabypfuncionario/<int:pk>', delete_funcionariosactabodegaspatios, name='delete_actabypfuncionario'),
path('delete/actabypatiende/<int:pk>', delete_atiendeactabodegaspatios, name='delete_actabypatiende'),
path('actavivtrans/list/<int:pk>/<int:codacta>', ActaViviendaTransitoriaList.as_view(), name='actavivtrans_list'),
path('actavivtrans/add/<int:idest>/<int:codacta>', ActaViviendaTransitoriaCreate.as_view(), name='actavivtrans_create'),
path('actavivtrans/edit/<int:idest>/<int:codacta>/<int:pk>', ActaViviendaTransitoriaUpdate.as_view(), name='actavivtrans_edit'),
path('delete/actavivtransitem/<int:pk>/<int:codacta>', delete_itemactaviviendatransitoria, name='delete_actavivtransitem'),
path('delete/actavivtransfunc/<int:pk>/<int:codacta>', delete_funcionariosactaviviendatransitoria, name='delete_actavivtransfunc'),
path('delete/actavivtransati/<int:pk>/<int:codacta>', delete_atiendeactaviviendatransitoria, name='delete_actavivtransati'),
path('preg/tipoacta/list/', TipoActaList.as_view(), name='preg_tipoacta_list'),
path('preg/list/<int:codacta>', PreguntaList.as_view(), name='preguntas_list'),
path('preg/add/<int:codacta>', EvaluacionPreguntaCreate.as_view(), name='preguntas_create'),
path('preg/edit/<int:codacta>/<int:pk>', EvaluacionPreguntaUpdate.as_view(), name='preguntas_edit'),
path('preg/del/<int:pk>/<int:codacta>', delete_evaluacionpregunta, name='delete_preguntas'),
path('estcar/list/<int:idest>', ActaCentroCarcelarioList.as_view(), name='actaestcarcelario_list'),
path('estcar/add/<int:idest>', ActaCentroCarcelarioCreate.as_view(), name='actaestcarcelario_create'),
path('estcar/edit/<int:idest>/<int:pk>', ActaCentroCarcelarioUpdate.as_view(), name='actaestcarcelario_edit'),
path('delete/actaestcaritem/<int:pk>', delete_itemactacentrocarcelario, name='delete_actaestcarcelario_item'),
path('delete/actaestcarfunc/<int:pk>', delete_funcionariosactacentrocarcelario, name='delete_actaestcarcelario_func'),
path('delete/actaestcarati/<int:pk>', delete_atiendeactacentrocarcelario, name='delete_actaestcarcelario_ati'),
path('drog/list/<int:idest>', ActaDrogueriaList.as_view(), name='actadrogueria_list'),
path('drog/add/<int:idest>', ActaDrogueriaCreate.as_view(), name='actadrogueria_create'),
path('drog/edit/<int:idest>/<int:pk>', ActaDrogueriaUpdate.as_view(), name='actadrogueria_edit'),
path('delete/actadrogitem/<int:pk>', delete_itemactadroguerias, name='delete_actadrogueria_item'),
path('delete/actadrogfunc/<int:pk>', delete_funcionariosactadrogueria, name='delete_actadrogueria_func'),
path('delete/actadrogati/<int:pk>', delete_atiendeactadrogueria, name='delete_actadrogueria_ati'),



]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)