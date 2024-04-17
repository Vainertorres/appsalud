from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import Principal, Report_nacido_vivo, Seguimiento_bajo_peso, nacidoVivoEdit, \
SegBajoPesoCreate, SegNacVivoUpdate, FileSegBajoPesoCreate, FileSegNacVivoUpdate, \
Estadistica_nacido_vivo, Generar_Estadistica_nacido_vivo, Mortalidadlist

app_name='ruaf'

urlpatterns = [
path('', Principal.as_view(), name='home_ruaf'),
path('report/nv', Report_nacido_vivo.as_view(), name='report_nv'),
path('estadistica/nv', Estadistica_nacido_vivo.as_view(), name='estadistica_nv'),
path('seg/nacvivo/<int:idnv>', nacidoVivoEdit, name='seg_nv'),
path('seg/bajopeso', Seguimiento_bajo_peso.as_view(), name='seg_bajo_peso'),
path('seg/bajopeso/edit/<int:idnv>/<int:pk>', SegNacVivoUpdate.as_view(), name='nacido_vivo_edit'),
path('seg/bajopeso/create/<int:idnv>', SegBajoPesoCreate.as_view(), name='nacido_vivo_new'),
path('file/nv/edit/<int:idnv>/<int:pk>', FileSegNacVivoUpdate.as_view(), name='file_nv_edit'),
path('file/nv/create/<int:idnv>', FileSegBajoPesoCreate.as_view(), name='file_nv_new'),
path('genestadistica/nv/<str:fec_ini>/<str:fec_fin>', Generar_Estadistica_nacido_vivo.as_view(), name='gen_est_nv'),
path('ruaf/mortalidad/list', Mortalidadlist.as_view(), name='mortalidad_list'),


]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)