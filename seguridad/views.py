from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from mpl_toolkits.basemap.test import Basemap
from geopy.geocoders import Nominatim
from django.db.models import Q
import folium
from folium.plugins import MarkerCluster

import pandas as pd
import webbrowser




from cnf.views import Sin_privilegio

from .models import Casos, Afectados, Organismos_atiende

from .forms import SeguridadForm, AfectadosFormSet, OrganismosFormSet

# Create your views here.

class SeguridadHome(Sin_privilegio, generic.TemplateView):
	permission_required="seguridad.view_casos"	
	template_name='base/baseseguridad.html'

class SeguridadAbout(generic.TemplateView):	
	template_name='seguridad/seguridad_about.html'

def obtener_lat_lon(direcc):
    latlong = {'lat':'SD', 'lon':'SD'}
    print(direcc)
    if (direcc != '') and (direcc != None) :
        if direcc.strip() != '':
            geo = Nominatim(user_agent='MyApp', timeout=10)
            direcc = direcc.lower()
            loc = geo.geocode(direcc, timeout=10)   
              
            if loc:             
                latlong ={'lat':loc.latitude, 'lon':loc.longitude}

    return latlong

class SeguridadList(Sin_privilegio, generic.ListView):
	permission_required="seguridad.view_casos"	
	model = Casos
	template_name='seguridad/seguridad_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

class SeguridadInline():
	form_class = SeguridadForm	
	model = Casos
	template_name = 'seguridad/seguridad_form.html'

	def form_valid(self, form):		
		named_formsets = self.get_named_formsets()
				
		if not all((x.is_valid() for x in named_formsets.values())):
			prueba = self.get_context_data(form=form)			
			return self.render_to_response(self.get_context_data(form=form))

		direcc = form.instance.direccion
		latlong = obtener_lat_lon(form.cleaned_data.get('direccion'))
		print('Latitud: ',latlong['lat'])
		if latlong['lat'] != 'SD':
			form.instance.lat = latlong['lat']
		if  latlong['lon'] != 'SD':
			form.instance.lon = latlong['lon']
		self.object = form.save()

		for name, formset in named_formsets.items():			
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		return redirect('seguridad:seg_list')

	
	def formset_afectados_valid(self, formset):		
		print("afectados")
		usuarios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for item in usuarios:
			item.casos = self.object
			item.save()

	def formset_organismos_atiende_valid(self, formset):		
		org_socorro = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for item in org_socorro:
			item.casos = self.object
			item.save()

def delete_afectados(request, pk):
	try:				
		afectado = Afectados.objects.get(id=pk)
	except afectado.DoesNotExist:
		messages.success(
			request, 'Afectados evento de seguridad no existe'
			)
		return redirect('seguridad:seguridad_edit', pk=afectado.casos.id)

	afectado.delete()
	messages.success(
		request, 'Afectado Eliminado satisfactoria mente'
		)
	return redirect('seguridad:seguridad_edit', pk=afectado.casos.id)


def delete_organismos_atiende(request, pk):
	try:		
		organismos_atiende = Organismos_atiende.objects.get(id=pk)
	except afectado.DoesNotExist:
		messages.success(
			request, 'Organismo que atiende evento de seguridad no existe'
			)
		return redirect('seguridad:seguridad_edit', pk=organismos_atiende.casos.id)

	organismos_atiende.delete()
	messages.success(
		request, 'Organismo Eliminado satisfactoria mente'
		)
	return redirect('seguridad:seguridad_edit', pk=organismos_atiende.casos.id)


class SeguridadCreate(Sin_privilegio, SeguridadInline, generic.CreateView):
	permission_required="seguridad.add_casos"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(SeguridadCreate, self).get_context_data(**kwargs)
		ctx['named_formsets'] = self.get_named_formsets()
		return ctx

	def get_named_formsets(self):		
		if self.request.method == "GET":
			return {
                'afectados': AfectadosFormSet(prefix='afectados'),
                'organismos_atiende': OrganismosFormSet(prefix='organismos_atiende')
            }
		else:
			return {
                'afectados': AfectadosFormSet(self.request.POST or None,  prefix='afectados'),
                'organismos_atiende': OrganismosFormSet(self.request.POST or None,  prefix='organismos_atiende'),
            }


class SeguridadUpdate(Sin_privilegio, SeguridadInline, generic.UpdateView):
	permission_required="seguridad.change_casos"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(SeguridadUpdate, self).get_context_data(**kwargs)
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['obj']=self.object
		ctx['editando']= True
		return ctx
	
	def get_named_formsets(self):
		return {
		'afectados': AfectadosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='afectados'),
		'organismos_atiende': OrganismosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='organismos_atiende')
		}	

def geolocCasos(request):	
	casos = Casos.objects.filter(~Q(lat='SD')).filter(~Q(lon='SD')).values('acciones__descripcion', 'lat','lon')
	
	primero = casos.first()
	some_map = folium.Map(location=[primero['lat'],primero['lon']], zoom_start = 15)
	
	for row in casos:
		lat = row['lat']
		lon = row['lon']
		tipocaso = row['acciones__descripcion']
		some_map.add_child(folium.Marker(location=[lat, lon], popup=tipocaso,icon=folium.Icon(color='red', icon='info-sign')))

	filepath = 'C:/mapas/mapa.html'
	some_map.save(filepath)
	webbrowser.open('file://' + filepath)

	html_string = some_map.get_root().render()
	context = {'sm':some_map, 'casos':casos, 'hs':html_string}

	return redirect('seguridad:seg_list')


def geolocMapaCalor(request):
	casos = Casos.objects.filter(~Q(lat='SD')).filter(~Q(lon='SD')).values('acciones__descripcion', 'lat','lon')
	primero = casos.first()

	some_map2 = folium.Map(location=[primero['lat'],primero['lon']], zoom_start = 10)
	mc = MarkerCluster()


	for row in casos:
		lat = row['lat']
		lon = row['lon']
		tipocaso = row['acciones__descripcion']
		mc.add_child(folium.Marker(location=[lat,lon], popup=tipocaso))

	some_map2.add_child(mc)

	filepath = 'C:/mapas/mapacalor.html'
	some_map2.save(filepath)
	webbrowser.open('file://' + filepath)

	html_string = some_map2.get_root().render()
	context = {'sm':some_map2, 'casos':casos, 'hs':html_string}

	return redirect('seguridad:seg_list')
