from django.conf import settings
from django.urls import path

from .views import Home, PeriodoreporteList, PeriodoreporteCreate, PeriodoreporteUpdate, \
PeriodoreporteDelete, Resolucion4505List, Resolucion4505Create, Resolucion4505Uptate

app_name='pai'

urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('perenvio', PeriodoreporteList.as_view(), name='periodoenv_list'),
	path('perenvio/new', PeriodoreporteCreate.as_view(), name='new_periodoenv'),
	path('perenvio/edit/<int:pk>', PeriodoreporteUpdate.as_view(), name='edit_periodoenv'),
	path('perenvio/delete/<int:pk>', PeriodoreporteDelete.as_view(), name='delete_periodoenv'),
	path('regctrl/list', Resolucion4505List.as_view(), name='regctrl_list'),
	path('regctrl/new', Resolucion4505Create.as_view(), name='regctrl_new'),
	path('regctrl/edit/<int:pk>', Resolucion4505Uptate.as_view(), name='regctrl_edit'),



]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)