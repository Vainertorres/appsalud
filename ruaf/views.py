from datetime import date
from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Count, Q, F

from cnf.views import Sin_privilegio
from .forms import Report_nacido_vivo_Form, Nacido_vivo_Form, Seg_nv_Bajo_Peso_Form, \
FileNacidoVivoForm

from .models import Nacido_vivo, SeguimientoBajoPeso, FileNacidoVivo, Mortalidad_ruaf

# Create your views here.

class Principal(Sin_privilegio, generic.TemplateView):
	permission_required="ruaf.view_nacido_vivo"	
	template_name='base/baseruaf.html'


class Report_nacido_vivo(Sin_privilegio, generic.TemplateView):
	permission_required="ruaf.view_nacido_vivo"
	template_name = 'ruaf/reporte_nacidos_vivos_rep.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	
	def post(self, request, *args, **kwargs):
		data= {}
				
		try:			
			action=request.POST.get("action")
			if action == 'search_report':
				data=[]
				
				start_date=request.POST.get('start_date','')
				end_date=request.POST.get('end_date','')
				search =Nacido_vivo.objects.all().values("nrocertificado", "fechanac","departamento__descripcion",\
					"municipio__descripcion", "tipo_parto__descripcion", "peso", "talla", \
					"madre__identificacion","madre__razonsocial", "sexo__descripcion")
				if len(start_date) and len(end_date):
					search = search.filter(fechanac__range=[start_date, end_date])
				for s in search:
					data.append([
							s['nrocertificado'],
							s['fechanac'].strftime('%Y-%m-%d'),							
							s['departamento__descripcion'],							
							s['municipio__descripcion'],
							s['peso'],
							s['talla'],
							s['sexo__descripcion'],
							s['madre__identificacion'],
							s['madre__razonsocial'],
							s['tipo_parto__descripcion']							
						])

			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data[0] = str(e)			
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		context['list_url']= reverse_lazy('ruaf:report_nv')
		context['titulo']= 'Generar reporte de Ruaf nacivos vivos'		
		context['form']=Report_nacido_vivo_Form()
		return context


class Generar_Estadistica_nacido_vivo(Sin_privilegio, generic.TemplateView):
	permission_required="ruaf.view_nacido_vivo"
	template_name = 'ruaf/estadisticaNV.html'


	def estadistica_x_ipsnac(self, start_date,end_date):
		diccionario={}
		data = []
			
		search =Nacido_vivo.objects.filter(fechanac__range=[start_date, end_date]).values("ips__razonsocial").annotate(cant=Count('id'))
		for x in search:
			cant = x['cant']
			nameclasificacion = x['ips__razonsocial']
			diccionario = {'name':nameclasificacion, 'y':cant}
			data.append(diccionario)		
		return data

	def estadistica_x_sitionac(self, start_date,end_date):
		diccionario={}
		data = []
			
		search =Nacido_vivo.objects.filter(fechanac__range=[start_date, end_date]).values("sitio_parto__descripcion").annotate(cant=Count('id'))
		for x in search:
			cant = x['cant']
			nameclasificacion = x['sitio_parto__descripcion']
			diccionario = {'name':nameclasificacion, 'y':cant}
			data.append(diccionario)		
		return data

	def estadistica_x_sexo(self, start_date,end_date):
		diccionario={}
		data = []
			
		search =Nacido_vivo.objects.filter(fechanac__range=[start_date, end_date]).values("sexo__descripcion").annotate(cant=Count('id'))
		for x in search:
			cant = x['cant']
			nameclasificacion = x['sexo__descripcion']
			diccionario = {'name':nameclasificacion, 'y':cant}
			data.append(diccionario)		
		return data



	def get_context_data(self, **kwargs):
		fec_ini = kwargs['fec_ini']
		fec_fin = kwargs['fec_fin']
	
		context = super().get_context_data(**kwargs)		
		context['list_url']= reverse_lazy('ruaf:estadistica_nv')
		context['titulo']= 'Generar estadística Ruaf nacivos vivos'		
		context['form']=Report_nacido_vivo_Form()
		context['ips']=self.estadistica_x_ipsnac(fec_ini, fec_fin)		
		context['sitio']=self.estadistica_x_sitionac(fec_ini, fec_fin)				
		context['sexo']=self.estadistica_x_sexo(fec_ini, fec_fin)	
		context['fec_ini'] = fec_ini
		context['fec_fin'] = fec_fin
		dato = 'Nacidos vivos entre: {} al {}'.format(fec_ini, fec_fin)
		context['subtitle'] = {'align': 'left', 'text':dato}

		
		return context



class Estadistica_nacido_vivo(Sin_privilegio, generic.TemplateView):
	permission_required="ruaf.view_nacido_vivo"
	template_name = 'ruaf/estadisticaNV.html'


	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		context['list_url']= reverse_lazy('ruaf:estadistica_nv')
		context['titulo']= 'Generar estadística Ruaf nacivos vivos'		
		context['form']=Report_nacido_vivo_Form()		
		return context

class Seguimiento_bajo_peso(Sin_privilegio, generic.TemplateView):
	permission_required="ruaf.view_nacido_vivo"
	template_name = 'ruaf/seg_nv_bajo_peso_nacer_list.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		data= {}
				
		try:			
			action=request.POST.get("action")
			if action == 'search_report':
				data=[]
				
				start_date=request.POST.get('start_date','')
				end_date=request.POST.get('end_date','')
				search =Nacido_vivo.objects.values("id","nrocertificado", "fechanac","departamento__descripcion",\
					"municipio__descripcion", "tipo_parto__descripcion", "peso", "talla", \
					"madre__identificacion","madre__razonsocial", "sexo__descripcion")
				if len(start_date) and len(end_date):
					search = search.filter(fechanac__range=[start_date, end_date]).filter(peso__lt=2500)
				for s in search:
					data.append([
							s['nrocertificado'],
							s['fechanac'].strftime('%Y-%m-%d'),							
							s['departamento__descripcion'],							
							s['municipio__descripcion'],
							s['peso'],
							s['talla'],
							s['sexo__descripcion'],
							s['madre__identificacion'],
							s['madre__razonsocial'],
							s['tipo_parto__descripcion'],
							'<a href="nacvivo/{}"><i class="fa-solid fa-pen-to-square"></i></a>'.format(s['id'])
						])

			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data[0] = str(e)			
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		context['list_url']= reverse_lazy('ruaf:seg_bajo_peso')
		context['titulo']= 'Seguimiento bajo peso al nacer'		
		context['form']=Report_nacido_vivo_Form()
		return context

class SegBajoPesoCreate(Sin_privilegio, generic.CreateView):
	permission_required="ruaf.add_seguimientobajopeso"
	model = SeguimientoBajoPeso
	template_name = 'ruaf/seguimientos_bajo_peso_nacer_form.html'
	context_object_name = 'obj'
	form_class = Seg_nv_Bajo_Peso_Form	
	login_url = 'cnf:login'


	def get_context_data(self, **kwargs):
		context = super(SegBajoPesoCreate,self).get_context_data(**kwargs)
		pk = self.kwargs.get('idnv') # El mismo nombre que en tu URL
		nac_vivo = Nacido_vivo.objects.get(pk=pk)		
		context['idnv'] = pk		
		return context

	def get_success_url(self):
		idnv=self.request.POST['nacido_vivo']
		return reverse_lazy('ruaf:seg_nv', kwargs={'idnv':idnv})


class SegNacVivoUpdate(Sin_privilegio, generic.UpdateView):
	permission_required="ruaf.change_seguimientobajopeso"
	model = SeguimientoBajoPeso
	template_name = 'ruaf/seguimientos_bajo_peso_nacer_form.html'
	context_object_name = 'obj'
	form_class = Seg_nv_Bajo_Peso_Form
	#success_url = reverse_lazy('den:dengue_edit', kwargs={'iddengue':dengue_id} )
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(SegNacVivoUpdate,self).get_context_data(**kwargs)
		pk =  self.kwargs.get('idnv') # El mismo nombre que en tu URL		
		context['idnv'] = pk		
		return context

	def get_success_url(self):
		idnv=self.request.POST['nacido_vivo']
		return reverse_lazy('ruaf:seg_nv', kwargs={'idnv':idnv})		

def nacidoVivoEdit(request, idnv):
	form = Nacido_vivo_Form()	
	model = Nacido_vivo.objects.filter(pk=idnv).first()
	second_model = SeguimientoBajoPeso.objects.filter(nacido_vivo=idnv).all()
	tercer_model = FileNacidoVivo.objects.filter(nacido_vivo=idnv).all()

	contexto = {'nv':model, 'seguimiento':second_model, 'filenv':tercer_model}	
	template='ruaf/seg_nv_bajo_peso_form.html'
	return render(request,template, contexto)

class FileSegBajoPesoCreate(Sin_privilegio, generic.CreateView):
	permission_required="ruaf.add_filenacidovivo"
	model = FileNacidoVivo
	template_name = 'ruaf/file_seg_bajo_peso_nacer_form.html'
	context_object_name = 'obj'
	form_class = FileNacidoVivoForm	
	login_url = 'cnf:login'


	def get_context_data(self, **kwargs):
		context = super(FileSegBajoPesoCreate,self).get_context_data(**kwargs)
		pk = self.kwargs.get('idnv') # El mismo nombre que en tu URL
		nac_vivo = Nacido_vivo.objects.get(pk=pk)		
		context['idnv'] = pk		
		return context

	def get_success_url(self):
		idnv=self.request.POST['nacido_vivo']
		return reverse_lazy('ruaf:seg_nv', kwargs={'idnv':idnv})


class FileSegNacVivoUpdate(Sin_privilegio, generic.UpdateView):
	permission_required="ruaf.change_filenacidovivo"
	model = FileNacidoVivo
	template_name = 'ruaf/file_seg_bajo_peso_nacer_form.html'
	context_object_name = 'obj'
	form_class = FileNacidoVivoForm	
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(FileSegNacVivoUpdate,self).get_context_data(**kwargs)
		pk =  self.kwargs.get('idnv') # El mismo nombre que en tu URL		
		context['idnv'] = pk		
		return context

	def get_success_url(self):
		idnv=self.request.POST['nacido_vivo']
		return reverse_lazy('ruaf:seg_nv', kwargs={'idnv':idnv})		




class Mortalidadlist(Sin_privilegio, generic.TemplateView):
	permission_required="ruaf.view_mortalidad_ruaf"
	template_name = 'ruaf/mortalidad_ruaf_list.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		data= {}
				
		try:			
			action=request.POST.get("action")
			if action == 'search_report':
				data=[]
				
				start_date=request.POST.get('start_date','')
				end_date=request.POST.get('end_date','')
				search =Mortalidad_ruaf.objects.values("id","nrocertificado", "fechadef","diagnosticoa__descripcion",\
					"clase_muerte__descripcion", "sitio_defuncion__descripcion", "edad", "eps__descripcion", \
					"paciente__identificacion","paciente__razonsocial", "sexo__descripcion")
				if len(start_date) and len(end_date):
					search = search.filter(fechadef__range=[start_date, end_date])
				for s in search:
					data.append([
							s['nrocertificado'],
							s['fechadef'].strftime('%Y-%m-%d'),							
							s['paciente__identificacion'],
							s['paciente__razonsocial'],
							s['sexo__descripcion'],
							s['edad'],
							s['eps__descripcion'],							
							s['diagnosticoa__descripcion'],
							s['sitio_defuncion__descripcion'],
							s['clase_muerte__descripcion']
							#'<a href="nacvivo/{}"><i class="fa-solid fa-pen-to-square"></i></a>'.format(s['id'])
						])
				print(search)

			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data[0] = str(e)			
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		context['list_url']= reverse_lazy('ruaf:mortalidad_list')
		context['titulo']= 'Gestionar Mortalidad Ruaf'		
		context['form']=Report_nacido_vivo_Form()
		return context

