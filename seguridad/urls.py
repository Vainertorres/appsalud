from django.conf import settings
from django.urls import path

from .views import *

app_name='seguridad'

urlpatterns = [

path('home', SeguridadHome.as_view(), name='home'),
path('seg/list', SeguridadList.as_view(), name='seg_list'),
path('add/seguridad', SeguridadCreate.as_view(), name='seguridad_new'),
path('change/seguridad/<int:pk>', SeguridadUpdate.as_view(), name='seguridad_edit'),
path('delete/afectado/<int:pk>', delete_afectados, name='delete_afectado'),
path('delete/organismo/<int:pk>', delete_organismos_atiende, name='delete_organismos'),
path('seg/about', SeguridadAbout.as_view(), name='about'),
path('seg/geoloc', geolocCasos, name='geoloc_seguridad'),
path('seg/mapa', geolocMapaCalor, name='mapa_de_calor'),




]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)