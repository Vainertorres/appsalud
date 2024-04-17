from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import modelformset_factory, inlineformset_factory
from cnf.views import Sin_privilegio
from django.views import generic
from django.contrib import messages
from django.db.models import Q, Count, F


from .models import Propietario, Establecimiento, ActaEstabEducativo, ItemActaEstabEducativo, \
	TipoActa, Pregunta, ActaEstEduFuncionario, Atiende_ActaEstabEduc, ActaGeneral,ActaGeneralFuncionarios, \
	AtiendeActaGeneral, Embarcaciones, ActaEmbarcacionInter, ActaEmbarcacionInterImo, \
	ActaEmbarcacionInterFuncionarios, ActaEmbarcacionInterPuerto, ActaBodegasPatios, \
	ItemActaBodegasPatios, FuncionariosActaBodegasPatios, AtiendeActaBodegasPatios, \
	ProductoQuimicoActaBodegasPatios, MedidaSanitariaActaBodegasPatios, \
	ActaViviendaTransitoria, ItemActaViviendaTransitoria, FuncionariosActaViviendaTransitoria, \
	AtiendeActaViviendaTransitoria,Bloque, ActaCentroCarcelario, ItemActaCentroCarcelario, \
	FuncionariosActaCentroCarcelario, AtiendeActaCentroCarcelario, ActaDrogueria, ItemActaDroguerias, \
	FuncionariosActaDrogueria, AtiendeActaDrogueria

from cnf.models import Tipodoc, Departamento, Municipio
from .forms import PropietarioForm, EstablecimientoForm, ActaEstabEducativoForm, \
      ItemActaEstabEducativoForm, ActaEstEduFuncionarioForm, Atiende_ActaEstabEducForm, \
      AtiendeActaGeneralForm, ActaGeneralFuncionariosForm, ActaGeneralForm, \
      ActaGeneralFuncionariosFormSet, AtiendeActaGeneralFormSet, EmbarcacionInternacionalForm, \
      ActaEmbarcacionInterImoForm, ActaEmbarcacionInterFuncionariosForm, \
      ActaEmbarcacionInterForm, ActaEmbarcacionInterFuncionariosFormSet, \
      ActaEmbarcacionInterImoFormSet, ActaEmbarcacionInterPuertoFormSet, \
      ActaBodegasPatiosForm, ItemActaBodegasPatiosFormSet, FuncionariosActaBodegasPatiosFormSet, \
      AtiendeActaBodegasPatiosFormSet, ProductoQuimicoActaBodegasPatiosFormSet, \
      MedidaSanitariaActaBodegasPatiosFormSet, ItemActaBodegasPatiosForm, \
      ActaViviendaTransitoriaForm, \
      FuncionariosActaViviendaTransitoriaFormSet, AtiendeActaViviendaTransitoriaFormSet, \
      ItemActaViviendaTransitoria4Form, ItemActaViviendaTransitoria5Form, \
      ItemActaViviendaTransitoria6Form, ItemActaViviendaTransitoria7Form, \
      ItemActaViviendaTransitoria8Form, EvaluacionPreguntaForm, EvaluacionPreguntaFormSet, \
      PreguntaForm, ActaCentroCarcelarioForm, ItemActaCentroCarcelarioForm, \
      FuncionariosActaCentroCarcelarioFormSet, AtiendeActaCentroCarcelarioFormSet, \
      ActaDrogueriaForm, ItemActaDrogueriasForm, FuncionariosActaDrogueriaFormSet, \
      AtiendeActaDrogueriaFormSet

      
# Create your views here.

def homesam(request):
	contexto ={}
	return render(request, 'base/basesam.html', context=contexto)

class PropietarioList(Sin_privilegio, generic.ListView):
    permission_required="sam.view_Propietario"
    model = Propietario
    template_name='sam/propietario_list.html'
    context_object_name = "obj"
    login_url = 'cnf:login'

class PropietarioCreate(LoginRequiredMixin, generic.CreateView):
	model = Propietario
	template_name = 'sam/propietario_form.html'
	context_object_name = 'obj'
	form_class = PropietarioForm
	success_url = reverse_lazy('sam:propietario_list')
	login_url = 'cnf:login'

class PropietarioEdit(LoginRequiredMixin, generic.UpdateView):
	model = Propietario
	template_name = 'sam/propietario_form.html'
	context_object_name = 'obj'
	form_class = PropietarioForm
	success_url = reverse_lazy('sam:propietario_list')
	login_url = 'cnf:login'  

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(PropietarioEdit,self).get_context_data(**kwargs)
		context['obj'] = Propietario.objects.filter(pk=pk).first()            
		return context  

class EstablecimientoList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_Establecimiento"
	model = Establecimiento
	template_name='sam/establecimiento_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(EstablecimientoList,self).get_context_data(**kwargs)
		context['id'] = self.kwargs.get('id')
		return context

class EstablecimientoCreate(LoginRequiredMixin, generic.CreateView):
	permission_required="sam.create_establecimiento"	
	model = Establecimiento
	template_name = 'sam/establecimiento_form.html'
	context_object_name = 'obj'
	form_class = EstablecimientoForm	
	login_url = 'cnf:login'

	def form_valid(self, form):
		form.instance.uc = self.request.user 
		super().form_valid(form)		
		return super().form_valid(form)
	
	def get_context_data(self, **kwargs):
		context = super(EstablecimientoCreate,self).get_context_data(**kwargs)
		#replegal = Propietario.objects.all()
		mpionot = Municipio.objects.all()
		context['mpionot'] = mpionot	
		#context['replegal'] = replegal
		return context

	def get_success_url(self):		
		return reverse_lazy('sam:establecimiento_list', kwargs={'id':0})

class EstablecimientoEdit(LoginRequiredMixin, generic.UpdateView):
	permission_required="sam.change_establecimiento"		
	model = Establecimiento
	template_name = 'sam/establecimiento_form.html'
	context_object_name = 'obj'
	form_class = EstablecimientoForm		
	login_url = 'cnf:login'

	def form_valid(self, form):
		form.instance.um = self.request.user 
		super().form_valid(form)		
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EstablecimientoEdit,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk') # El mismo nombre que en tu URL				
		mpionot = Municipio.objects.all()		
		context['mpionot'] = mpionot			
		return context

	def get_success_url(self):		
		return reverse('sam:establecimiento_list', kwargs={'id':0})


class EstablecimientoEducativoList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_ActaEstabEducativo"
	model = ActaEstabEducativo
	template_name='sam/actaesteducativo_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(EstablecimientoEducativoList,self).get_context_data(**kwargs)
		estaeduca = ActaEstabEducativo.objects.filter(establecimiento_id=pk)
		establecimiento = Establecimiento.objects.filter(id=pk).first()
		context['obj'] =estaeduca
		context['idestablecimiento'] = pk
		context['nomestablecimiento'] = establecimiento.razonsocial				
		return context
 
def establecimientoEducativoCreate(request, estaedu_id, idacta=None):
	
	template_name='sam/actaesteducativo_form.html'
	contexto={}

	if request.method == 'POST':
		if idacta == None:
			form = ActaEstabEducativoForm(request.POST or None)
		else:
			actaestaeducativo = ActaEstabEducativo.objects.get(pk=idacta)
			form = ActaEstabEducativoForm(request.POST, instance=actaestaeducativo)
			print('ingreso con acta creada para actualizar')

		itemactaesteduFormset = inlineformset_factory(ActaEstabEducativo, ItemActaEstabEducativo,form=ItemActaEstabEducativoForm, extra=1)
		funcionariosFormset = inlineformset_factory(ActaEstabEducativo, ActaEstEduFuncionario,form=ActaEstEduFuncionarioForm, extra=2)
		atiende_ActaEstabEducFormset=inlineformset_factory(ActaEstabEducativo, Atiende_ActaEstabEduc,form=Atiende_ActaEstabEducForm, extra=2)

		if idacta == None:
			if form.is_valid():
				actaestaeducativo = form.save()
		else:
			if form.is_valid():
				form.save()

		formsetitem = itemactaesteduFormset(request.POST, instance=actaestaeducativo)
		formsetfuncionario = funcionariosFormset(request.POST, instance=actaestaeducativo)
		formsetatiendeactaestabeduc = atiende_ActaEstabEducFormset(request.POST, instance=actaestaeducativo)

		if formsetitem.is_valid():
			formsetitem.save()

		if formsetfuncionario.is_valid():
			formsetfuncionario.save()

		if formsetatiendeactaestabeduc.is_valid():
			formsetatiendeactaestabeduc.save()


		return redirect('sam:actaestedu_list', pk=estaedu_id)	

	if request.method == 'GET':
		if idacta == None:
			actablanco = ActaEstabEducativo()
			actablanco.establecimiento_id = estaedu_id
			listapreguntas=[]

			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO001').first()
			preguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk)
			for p in preguntas:
				diccitemacta = {
					'actaestabeducativo':actablanco.id,
					'pregunta':p.id,
					'evaluacion':3,
					'hallazgo':'',
					'puntaje':0,
					'habilitada':p.habilitada
				}
				if p.habilitada == False:
					print('Bloque',p.bloque)

				listapreguntas.append(diccitemacta)

			form = ActaEstabEducativoForm(instance=actablanco)
			itemformset = inlineformset_factory(ActaEstabEducativo, ItemActaEstabEducativo,form=ItemActaEstabEducativoForm, 
				extra=len(listapreguntas), can_delete=False)
			formset = itemformset()
			for subform, data in zip(formset.forms, listapreguntas):
				subform.initial = data

			funcionariosFormset = inlineformset_factory(ActaEstabEducativo, ActaEstEduFuncionario, 
				form=ActaEstEduFuncionarioForm, extra=2)
			formsetfuncionario = funcionariosFormset()

			atiende_ActaEstabEducFormset=inlineformset_factory(ActaEstabEducativo, Atiende_ActaEstabEduc, 
				form=Atiende_ActaEstabEducForm, extra=2)

			formsetatiendeactaestabeduc = atiende_ActaEstabEducFormset()

			contexto={'form':form, 'formset':formset, 'formsetfunc':formsetfuncionario, 'formsetatiende':formsetatiendeactaestabeduc, 'establecimiento_id':estaedu_id} 
		else:
			actaestabeducativo = ActaEstabEducativo.objects.get(pk=idacta)
			form = ActaEstabEducativoForm(instance=actaestabeducativo)
			itemformset = inlineformset_factory(ActaEstabEducativo, ItemActaEstabEducativo,form=ItemActaEstabEducativoForm, \
				extra=0, can_delete=False)
			formset = itemformset(instance=actaestabeducativo)

			funcionariosFormset = inlineformset_factory(ActaEstabEducativo, ActaEstEduFuncionario, form=ActaEstEduFuncionarioForm, extra=2)
			formsetfuncionario = funcionariosFormset(instance=actaestabeducativo) 
			
			atiende_ActaEstabEducFormset=inlineformset_factory(ActaEstabEducativo, Atiende_ActaEstabEduc, 
				  form=Atiende_ActaEstabEducForm, extra=2)
			formsetatiendeactaestabeduc = atiende_ActaEstabEducFormset(instance=actaestabeducativo)

			contexto={'form':form, 'formset':formset, 'formsetfunc':formsetfuncionario, 'formsetatiende':formsetatiendeactaestabeduc, 'establecimiento_id':estaedu_id, 'idacta':idacta, 'obj':actaestabeducativo} 
		return render(request, template_name, contexto)
	return render(request, template_name, contexto)


class ActageneralList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_actageneral"
	model = ActaGeneral
	template_name='sam/actageneral_list.html'	
	login_url = 'cnf:login'
	
	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(ActageneralList,self).get_context_data(**kwargs)
		acta = ActaGeneral.objects.filter(establecimiento_id=pk)
		establecimiento = Establecimiento.objects.filter(id=pk).first()
		context['obj'] =acta
		context['idestablecimiento'] = pk
		context['nomestablecimiento'] = establecimiento.razonsocial		
		print(establecimiento.razonsocial)
		return context


class ActaGeneralInline():
	form_class = ActaGeneralForm	
	model = ActaGeneral
	template_name = 'sam/actageneral_form.html'

	
	def form_valid(self, form):		
		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		self.object.save()
		print(self.object)
		return redirect('sam:actagral_list', pk=self.object.establecimiento.id)

	
	def formset_actageneralfuncionarios_valid(self, formset):		
		actageneralfuncionarios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in actageneralfuncionarios:
			seg.actageneral = self.object
			seg.save()

	def formset_atiendeactageneral_valid(self, formset):		
		atiendeactageneral = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in atiendeactageneral:
			seg.actageneral = self.object
			seg.save()

	

class ActaGeneralCreate(Sin_privilegio, ActaGeneralInline, generic.CreateView):
	permission_required="add_actageneral"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaGeneralCreate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['idestablecimiento'] = idest
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx

	def get_named_formsets(self):
		if self.request.method == "GET":
			return {
                'actageneralfuncionarios': ActaGeneralFuncionariosFormSet(prefix='actageneralfuncionarios'),
                'atiendeactageneral': AtiendeActaGeneralFormSet(prefix='atiendeactageneral'),
                
			}
		else:
			return {
                'actageneralfuncionarios': ActaGeneralFuncionariosFormSet(self.request.POST or None, prefix='actageneralfuncionarios'),
                'atiendeactageneral': AtiendeActaGeneralFormSet(self.request.POST or None, prefix='atiendeactageneral'),
                
            }

class ActaGeneralUpdate(Sin_privilegio, ActaGeneralInline, generic.UpdateView):
	permission_required="change_actageneral"
	#context_object_name = 'obj'
	#success_url = reverse_lazy('pqrs:pqrs_list')		
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaGeneralUpdate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['obj']=self.object
		ctx['idestablecimiento'] = idest
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx
	
	def get_named_formsets(self):
		return {
		'actageneralfuncionarios': ActaGeneralFuncionariosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='actageneralfuncionarios'),
		'atiendeactageneral': AtiendeActaGeneralFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='atiendeactageneral'),
		}	

def delete_actageneralfuncionarios(request, pk):
	try:
		actageneralfuncionarios = ActaGeneralFuncionarios.objects.get(id=pk)
		actageneralInline = ActaGeneralInline()
		idactagral = actageneralfuncionarios.actageneral.id
		actageneral = ActaGeneral.objects.get(id=idactagral)		
	

	except ActaGeneralFuncionarios.DoesNotExist:
		messages.success(
			request, 'Funcionario no existe'
			)
		return redirect('sam:actagral_edit', pk=actageneralfuncionarios.novlcregtipo1.id)

	actageneralfuncionarios.delete()	
	actageneral.save()

	messages.success(
		request, 'Funcionario eliminado satisfactoriamente'
		)
	return redirect('sam:actagral_edit', pk=actageneralfuncionarios.actageneral.id)


def delete_atiendeactageneral(request, pk):
	try:
		atiendeactageneral = AtiendeActaGeneral.objects.get(id=pk)
		actageneralInline = ActaGeneralInline()
		idactagral = atiendeactageneral.actageneral.id
		actageneral = ActaGeneral.objects.get(id=idactagral)		


	except AtiendeActaGeneral.DoesNotExist:
		messages.success(
			request, 'Personal que atiende visita no existe'
			)
		return redirect('sam:actagral_edit', pk=atiendeactageneral.actageneral.id)

	atiendeactageneral.delete()
	actageneral.save()
	messages.success(
		request, 'Personal que atiende visita eliminado satisfactoriamente'
		)
	return redirect('sam:actagral_edit', pk=atiendeactageneral.actageneral.id)



class EmbarcacionesList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_embarcaciones"
	model = Embarcaciones
	template_name='sam/embarcacion_internacional_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(EmbarcacionesList,self).get_context_data(**kwargs)
		context['id'] = self.kwargs.get('id')
		return context

class EmbarcacionesCreate(LoginRequiredMixin, generic.CreateView):
	permission_required="sam.add_embarcaciones"	
	model = Embarcaciones
	template_name = 'sam/embarcacion_internacional_form.html'
	context_object_name = 'obj'
	form_class = EmbarcacionInternacionalForm	
	login_url = 'cnf:login'

	def form_valid(self, form):
		form.instance.uc = self.request.user 
		super().form_valid(form)		
		return super().form_valid(form)	

	def get_success_url(self):		
		return reverse_lazy('sam:embarcacion_list', kwargs={'id':0})

class EmbarcacionesEdit(LoginRequiredMixin, generic.UpdateView):
	permission_required="sam.change_embarcaciones"		
	model = Embarcaciones
	template_name = 'sam/embarcacion_internacional_form.html'
	context_object_name = 'obj'
	form_class = EmbarcacionInternacionalForm		
	login_url = 'cnf:login'

	def form_valid(self, form):
		form.instance.um = self.request.user 
		super().form_valid(form)		
		return super().form_valid(form)

	def get_success_url(self):		
		return reverse('sam:embarcacion_list', kwargs={'id':0})

class ActaEmbarInternalList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_actaembarcacioninterfuncionarios"
	model = ActaEmbarcacionInter
	template_name='sam/acta_embarcion_internacional_list.html'	
	login_url = 'cnf:login'
	
	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(ActaEmbarInternalList,self).get_context_data(**kwargs)
		acta = ActaEmbarcacionInter.objects.filter(embarcaciones_id=pk).all()
		embarcaciones = Embarcaciones.objects.filter(id=pk).first()
		context['obj']=acta
		context['idembarcacion'] = pk
		context['nomembarcacion'] = embarcaciones.nombre		
		return context


class ActaEmbarcacionInterInline():
	form_class = ActaEmbarcacionInterForm	
	model = ActaEmbarcacionInter
	template_name = 'sam/acta_embarcacion_internacional_form.html'

	
	def form_valid(self, form):		
		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		self.object.save()
		print(self.object)
		return redirect('sam:actaembint_list', pk=self.object.embarcaciones.id)

	
	def formset_actaembarcacioninterfuncionarios_valid(self, formset):		
		actaembarcacioninterfuncionarios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in actaembarcacioninterfuncionarios:
			seg.actaembarcacioninter = self.object
			seg.save()

	def formset_actaembarcacioninterimo_valid(self, formset):		
		actaembarcacioninterimo = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in actaembarcacioninterimo:
			seg.actaembarcacioninter = self.object
			seg.save()

	def formset_actaembarcacioninterpuerto_valid(self, formset):		
		actaembarcacioninterpuerto = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in actaembarcacioninterpuerto:
			seg.actaembarcacioninter = self.object
			seg.save()


class ActaEmbarcacionInterCreate(Sin_privilegio, ActaEmbarcacionInterInline, generic.CreateView):
	permission_required="sam.add_actaembarcacioninterfuncionarios"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaEmbarcacionInterCreate, self).get_context_data(**kwargs)
		idemb = self.kwargs.get('idemb')
		embarcaciones = Embarcaciones.objects.filter(id=idemb).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['idembarcacion'] = idemb
		ctx['nomembarcacion'] = embarcaciones.nombre
		return ctx

	def get_named_formsets(self):
		if self.request.method == "GET":
			return {
                'actaembarcacioninterfuncionarios': ActaEmbarcacionInterFuncionariosFormSet(prefix='actaembarcacioninterfuncionarios'),
                'actaembarcacioninterimo': ActaEmbarcacionInterImoFormSet(prefix='actaembarcacioninterimo'),
                'actaembarcacioninterpuerto': ActaEmbarcacionInterPuertoFormSet(prefix='actaembarcacioninterpuerto'),

                
			}
		else:
			return {
                'actaembarcacioninterfuncionarios': ActaEmbarcacionInterFuncionariosFormSet(self.request.POST or None, prefix='actaembarcacioninterfuncionarios'),
                'actaembarcacioninterimo': ActaEmbarcacionInterImoFormSet(self.request.POST or None, prefix='actaembarcacioninterimo'),
                'actaembarcacioninterpuerto': ActaEmbarcacionInterPuertoFormSet(self.request.POST or None, prefix='actaembarcacioninterpuerto'),

                
            }

class ActaEmbarcacionInterUpdate(Sin_privilegio, ActaEmbarcacionInterInline, generic.UpdateView):
	permission_required="sam.change_actaembarcacioninterfuncionarios"	
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaEmbarcacionInterUpdate, self).get_context_data(**kwargs)
		idemb = self.kwargs.get('idemb')
		embarcaciones = Embarcaciones.objects.filter(id=idemb).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['obj']=self.object
		ctx['idembarcacion'] = idemb
		ctx['nomembarcacion'] = embarcaciones.nombre
		return ctx
	
	def get_named_formsets(self):
		return {
		'actaembarcacioninterfuncionarios': ActaEmbarcacionInterFuncionariosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='actaembarcacioninterfuncionarios'),
		'actaembarcacioninterimo': ActaEmbarcacionInterImoFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='actaembarcacioninterimo'),
		'actaembarcacioninterpuerto': ActaEmbarcacionInterPuertoFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='actaembarcacioninterpuerto'),

		}	

def delete_actaembarcacioninterfuncionarios(request, pk):
	try:
		actaembarcacioninterfuncionarios = ActaEmbarcacionInterFuncionarios.objects.get(id=pk)
		actaembarcacioninterinline = ActaEmbarcacionInterInline()
		idactagral = actaembarcacioninterfuncionarios.actaembarcacioninter.id
		actageneral = ActaEmbarcacionInter.objects.get(id=idactagral)		
	

	except ActaEmbarcacionInterFuncionarios.DoesNotExist:
		messages.success(
			request, 'Funcionario no existe'
			)
		return redirect('sam:actaembint_edit', idemb= actageneral.embarcaciones.id, pk=actaembarcacioninterfuncionarios.actaembarcacioninter.id)

	actaembarcacioninterfuncionarios.delete()	
	actageneral.save()

	messages.success(
		request, 'Funcionario eliminado satisfactoriamente'
		)
	return redirect('sam:actaembint_edit', idemb= actageneral.embarcaciones.id, pk=actaembarcacioninterfuncionarios.actaembarcacioninter.id)

def delete_actaembarcacioninterimo(request, pk):
	try:
		actaembarcacioninterimo = ActaEmbarcacionInterImo.objects.get(id=pk)
		actaembarcacioninterinline = ActaEmbarcacionInterInline()
		idactagral = actaembarcacioninterimo.actaembarcacioninter.id
		actageneral = ActaEmbarcacionInter.objects.get(id=idactagral)		
	

	except ActaEmbarcacionInterImo.DoesNotExist:
		messages.success(
			request, 'IMO no existe'
			)
		return redirect('sam:actaembint_edit', idemb= actageneral.embarcaciones.id, pk=actaembarcacioninterimo.actaembarcacioninter.id)

	actaembarcacioninterimo.delete()	
	actageneral.save()

	messages.success(
		request, 'IMO eliminado satisfactoriamente'
		)
	return redirect('sam:actaembint_edit', idemb= actageneral.embarcaciones.id, pk=actaembarcacioninterimo.actaembarcacioninter.id)


def delete_actaembarcacioninterpuerto(request, pk):
	try:
		actaembarcacioninterpuerto = ActaEmbarcacionInterPuerto.objects.get(id=pk)
		actaembarcacioninterinline = ActaEmbarcacionInterInline()
		idactagral = actaembarcacioninterpuerto.actaembarcacioninter.id
		actageneral = ActaEmbarcacionInter.objects.get(id=idactagral)		
	

	except ActaEmbarcacionInterPuerto.DoesNotExist:
		messages.success(
			request, 'Puertos no existe'
			)
		return redirect('sam:actaembint_edit', idemb= actageneral.embarcaciones.id, pk=actaembarcacioninterpuerto.actaembarcacioninter.id)

	actaembarcacioninterpuerto.delete()	
	actageneral.save()

	messages.success(
		request, 'Puerto visitado... eliminado satisfactoriamente'
		)
	return redirect('sam:actaembint_edit', idemb= actageneral.embarcaciones.id, pk=actaembarcacioninterpuerto.actaembarcacioninter.id)


class ActaBodegasPatiosList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_actabodegaspatios"
	model = ActaBodegasPatios
	template_name='sam/actabodegasypatios_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(ActaBodegasPatiosList,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		acta = ActaBodegasPatios.objects.filter(establecimiento_id=pk)
		establecimiento = Establecimiento.objects.filter(id=pk).first()
		context['obj'] =acta
		context['idestablecimiento'] = pk
		context['nomestablecimiento'] = establecimiento.razonsocial		
		return context

class ActaBodegasPatiosInline():
	form_class = ActaBodegasPatiosForm	
	model = ActaBodegasPatios
	template_name = 'sam/actabodegasypatios_form.html'

	
	def form_valid(self, form):		
		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		self.object.save()
		print(self.object)
		return redirect('sam:actabodpat_list', pk=self.object.establecimiento.id)

	
	def formset_itemactabodegaspatios_valid(self, formset):		
		itemactabodegaspatios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in itemactabodegaspatios:
			seg.actabodegaspatios = self.object
			seg.save()

	def formset_funcionariosactabodegaspatios_valid(self, formset):		
		funcionariosactabodegaspatios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in funcionariosactabodegaspatios:
			seg.actabodegaspatios = self.object
			seg.save()

	def formset_atiendeactabodegaspatios_valid(self, formset):		
		atiendeactabodegaspatios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in atiendeactabodegaspatios:
			seg.actabodegaspatios = self.object
			seg.save()

	def formset_productoquimicoactabodegaspatios_valid(self, formset):		
		productoquimicoActabodegaspatios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in productoquimicoActabodegaspatios:
			seg.actabodegaspatios = self.object
			seg.save()

	def formset_medidasanitariaactabodegaspatios_valid(self, formset):		
		medidasanitariaactabodegaspatios = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in medidasanitariaactabodegaspatios:
			seg.actabodegaspatios = self.object
			seg.save()

	

class ActaBodegasPatiosCreate(Sin_privilegio, ActaBodegasPatiosInline, generic.CreateView):
	permission_required="sam.add_actabodegaspatios"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaBodegasPatiosCreate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['idestablecimiento'] = idest
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx

	def cantidadPreguntasItemEvaluar(self, idtipoacta):
		tipoacta = TipoActa.objects.filter(idtipoacta=idtipoacta).first()
		cantpreguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk).count()
		return cantpreguntas

	def listaPreguntasItemEvaluar(self):
		listapreguntas=[]
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFOBODPAT').first()
		preguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk)
		
		for p in preguntas:
			diccitemacta = {
			'actabodegaspatios':self.model.id,
			'pregunta':p.id,		
			'hallazgo':'NO',
		
			}
			if p.habilitada == False:
				print('Bloque',p.bloque)

			listapreguntas.append(diccitemacta)

		return listapreguntas

	def get_named_formsets(self):
		listapreguntas = []
		
		if self.request.method == "GET":
			ItemActaBodegasPatiosFormSet1 = inlineformset_factory(
 	   		ActaBodegasPatios, ItemActaBodegasPatios, form=ItemActaBodegasPatiosForm,	
    		extra=self.cantidadPreguntasItemEvaluar('MISFOBODPAT'), can_delete=True, can_delete_extra=True
			)
			itemFormset = ItemActaBodegasPatiosFormSet1(prefix='itemactabodegaspatios')
			listapreguntas = self.listaPreguntasItemEvaluar()			
			for subform, data in zip(itemFormset.forms, listapreguntas):
				subform.initial = data

			return {
                'itemactabodegaspatios': itemFormset,
                'funcionariosactabodegaspatios': FuncionariosActaBodegasPatiosFormSet(prefix='funcionariosactabodegaspatios'),
                'atiendeactabodegaspatios': AtiendeActaBodegasPatiosFormSet(prefix='atiendeactabodegaspatios'),
                'productoquimicoactabodegaspatios': ProductoQuimicoActaBodegasPatiosFormSet(prefix='productoquimicoactabodegaspatios'),
                'medidasanitariaactabodegaspatios': MedidaSanitariaActaBodegasPatiosFormSet(prefix='medidasanitariaactabodegaspatios'),

			}
		else:
			return {
                'itemactabodegaspatios': ItemActaBodegasPatiosFormSet(self.request.POST or None, prefix='itemactabodegaspatios'),               
                'funcionariosactabodegaspatios': FuncionariosActaBodegasPatiosFormSet(self.request.POST or None, prefix='funcionariosactabodegaspatios'),
                'atiendeactabodegaspatios': AtiendeActaBodegasPatiosFormSet(self.request.POST or None, prefix='atiendeactabodegaspatios'),
                'productoquimicoactabodegaspatios': ProductoQuimicoActaBodegasPatiosFormSet(self.request.POST or None, prefix='productoquimicoactabodegaspatios'),
                'medidasanitariaactabodegaspatios': MedidaSanitariaActaBodegasPatiosFormSet(self.request.POST or None, prefix='medidasanitariaactabodegaspatios'),
              
            }

class ActaBodegasPatiosUpdate(Sin_privilegio, ActaBodegasPatiosInline, generic.UpdateView):
	permission_required="sam.change_actageneral"
	#context_object_name = 'obj'
	#success_url = reverse_lazy('pqrs:pqrs_list')		
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaBodegasPatiosUpdate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['obj']=self.object
		ctx['idestablecimiento'] = idest
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx
	
	def get_named_formsets(self):
		return {
		'itemactabodegaspatios': ItemActaBodegasPatiosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='itemactabodegaspatios'),
		'funcionariosactabodegaspatios': FuncionariosActaBodegasPatiosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='funcionariosactabodegaspatios'),
		'atiendeactabodegaspatios': AtiendeActaBodegasPatiosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='atiendeactabodegaspatios'),
		'productoquimicoactabodegaspatios': ProductoQuimicoActaBodegasPatiosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='productoquimicoactabodegaspatios'),
		'medidasanitariaactabodegaspatios': MedidaSanitariaActaBodegasPatiosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='medidasanitariaactabodegaspatios'),

		}	

def delete_itemactabodegaspatios(request, pk):
	try:
		itemactabodegaspatios = ItemActaBodegasPatios.objects.get(id=pk)
		actabodegaspatiosinline = ActaBodegasPatiosInline()
		idactagral = itemactabodegaspatios.actabodegaspatios.id
		actageneral = ActaBodegasPatios.objects.get(id=idactagral)		
	

	except ItemActaBodegasPatios.DoesNotExist:
		messages.success(
			request, 'Item a evaluar no existe'
			)
		return redirect('sam:actabodpat_list', pk=itemactabodegaspatios.actabodegaspatios.id)

	itemactabodegaspatios.delete()	
	actageneral.save()

	messages.success(
		request, 'Item a evaluar eliminado satisfactoriamente'
		)
	return redirect('sam:actabodpat_list', pk=itemactabodegaspatios.actabodegaspatios.id)

def delete_funcionariosactabodegaspatios(request, pk):
	try:
		funcionariosactabodegaspatios = FuncionariosActaBodegasPatios.objects.get(id=pk)
		actabodegaspatiosinline = ActaBodegasPatiosInline()
		idactagral = funcionariosactabodegaspatios.actabodegaspatios.id
		actageneral = ActaBodegasPatios.objects.get(id=idactagral)		
	

	except FuncionariosActaBodegasPatios.DoesNotExist:
		messages.success(
			request, 'Funcionario no existe'
			)
		return redirect('sam:actabodpat_list', pk=funcionariosactabodegaspatios.actabodegaspatios.id)

	funcionariosactabodegaspatios.delete()	
	actageneral.save()

	messages.success(
		request, 'Funcionario eliminado satisfactoriamente'
		)
	return redirect('sam:actabodpat_list', pk=funcionariosactabodegaspatios.actabodegaspatios.id)


def delete_atiendeactabodegaspatios(request, pk):
	try:
		atiendeactabodegaspatios = AtiendeActaBodegasPatios.objects.get(id=pk)
		actabodegaspatiosinline = ActaBodegasPatiosInline()
		idactagral = atiendeactabodegaspatios.actabodegaspatios.id
		actageneral = ActaBodegasPatios.objects.get(id=idactagral)		
	

	except AtiendeActaBodegasPatios.DoesNotExist:
		messages.success(
			request, 'Usuario que atiende no existe'
			)
		return redirect('sam:actabodpat_list', pk=atiendeactabodegaspatios.actabodegaspatios.id)

	atiendeactabodegaspatios.delete()	
	actageneral.save()

	messages.success(
		request, 'Usuario que atiende eliminado satisfactoriamente'
		)
	return redirect('sam:actabodpat_list', pk=atiendeactabodegaspatios.actabodegaspatios.id)


def delete_productoquimicoactabodegaspatios(request, pk):
	try:
		productoquimicoactabodegaspatios = ProductoQuimicoActaBodegasPatios.objects.get(id=pk)
		actabodegaspatiosinline = ActaBodegasPatiosInline()
		idactagral = productoquimicoactabodegaspatios.actabodegaspatios.id
		actageneral = ActaBodegasPatios.objects.get(id=idactagral)		
	

	except ProductoQuimicoActaBodegasPatios.DoesNotExist:
		messages.success(
			request, 'Producto químico que atiende no existe'
			)
		return redirect('sam:actabodpat_list', pk=productoquimicoactabodegaspatios.actabodegaspatios.id)

	productoquimicoactabodegaspatios.delete()	
	actageneral.save()

	messages.success(
		request, 'Producto químico eliminado satisfactoriamente'
		)
	return redirect('sam:actabodpat_list', pk=productoquimicoactabodegaspatios.actabodegaspatios.id)


def delete_medidasanitariaactabodegaspatios(request, pk):
	try:
		medidasanitariaactabodegaspatios = MedidaSanitariaActaBodegasPatios.objects.get(id=pk)
		actabodegaspatiosinline = ActaBodegasPatiosInline()
		idactagral = medidasanitariaactabodegaspatios.actabodegaspatios.id
		actageneral = ActaBodegasPatios.objects.get(id=idactagral)		
	

	except MedidaSanitariaActaBodegasPatios.DoesNotExist:
		messages.success(
			request, 'Medida sanitaria no existe'
			)
		return redirect('sam:actabodpat_list', pk=medidasanitariaactabodegaspatios.actabodegaspatios.id)

	medidasanitariaactabodegaspatios.delete()	
	actageneral.save()

	messages.success(
		request, 'Medida sanitaria eliminada satisfactoriamente'
		)
	return redirect('sam:actabodpat_list', pk=medidasanitariaactabodegaspatios.actabodegaspatios.id)

#Viviendas transitorias
class ActaViviendaTransitoriaList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_actaviviendatransitoria"
	model = ActaViviendaTransitoria
	template_name='sam/actaviviendatransitoria_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def obtenerTipoActa(self, codacta):
		tipoacta = 4
		if codacta == 4:
			#Vivienda transitoria
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-VITR').first()
		elif codacta == 5:
			#Hogar de paso
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOPA').first()
		elif codacta == 6:
			#Hogar comunitario
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOGC').first()
		elif codacta == 7:
			#Hogar Hogar geriatrico o de larga estancia
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOGG').first()
		else:
			#Centros vida
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-ECV').first()

		return tipoacta

	def get_context_data(self, **kwargs):
		context = super(ActaViviendaTransitoriaList,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		codacta = self.kwargs.get('codacta')
		tipoacta = self.obtenerTipoActa(codacta)


		acta = ActaViviendaTransitoria.objects.filter(establecimiento_id=pk).filter(tipoacta_id=tipoacta.pk)
		establecimiento = Establecimiento.objects.filter(id=pk).first()
		context['obj'] =acta
		context['codacta'] = self.kwargs.get('codacta')
		context['idestablecimiento'] = pk
		context['nomestablecimiento'] = establecimiento.razonsocial		
		return context


class ActaViviendaTransitoriaInline():
	form_class = ActaViviendaTransitoriaForm	
	model = ActaViviendaTransitoria
	template_name = 'sam/actaviviendatransitoria_form.html'

	
	def form_valid(self, form):		
		codacta = self.kwargs.get('codacta')

		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		self.object.save()
		return redirect('sam:actavivtrans_list', pk=self.object.establecimiento.id, codacta=codacta)

	
	def formset_itemactaviviendatransitoria_valid(self, formset):		
		itemactaviviendatransitoria = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in itemactaviviendatransitoria:
			seg.actaviviendatransitoria = self.object
			seg.save()

	def formset_funcionariosactaviviendatransitoria_valid(self, formset):		
		funcionariosactaviviendatransitoria = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in funcionariosactaviviendatransitoria:
			seg.actaviviendatransitoria = self.object
			seg.save()

	def formset_atiendeactaviviendatransitoria_valid(self, formset):		
		atiendeactaviviendatransitoria = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in atiendeactaviviendatransitoria:
			seg.actaviviendatransitoria = self.object
			seg.save()

	
class ActaViviendaTransitoriaCreate(Sin_privilegio, ActaViviendaTransitoriaInline, generic.CreateView):
	permission_required="sam.add_actaviviendatransitoria"
	login_url = 'cnf:login'
	codacta = 4

	def get_context_data(self, **kwargs):
		ctx = super(ActaViviendaTransitoriaCreate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		self.codacta = self.kwargs.get('codacta')
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['idestablecimiento'] = idest
		ctx['codacta'] = self.codacta
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx

	def cantidadPreguntasItemEvaluar(self, idtipoacta):
		tipoacta = TipoActa.objects.filter(idtipoacta=idtipoacta).first()
		cantpreguntas = 0
		if tipoacta:
			cantpreguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk).count()
		return cantpreguntas

	def listaPreguntasItemEvaluar(self):
		listapreguntas=[]
		if self.codacta == 4:
			#Vivienda transitoria
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-VITR').first()
		elif self.codacta == 5:
			#Hogar de paso
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOPA').first()
		elif self.codacta == 6:
			#Hogar comunitario
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOGC').first()
		elif self.codacta == 7:
			#Hogar Hogar geriatrico o de larga estancia
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-HOGG').first()
		else:
			#Centros vida
			tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-ECV').first()
		print(tipoacta)

		preguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk)
		
		for p in preguntas:
			diccitemacta = {
			'actaviviendatransitoria':self.model.id,
			'pregunta':p.id,		
			'evaluacion':'',
			'puntaje':0,
			'habilitada':p.habilitada		
			}
			
			listapreguntas.append(diccitemacta)

		return listapreguntas

	def get_named_formsets(self):
		listapreguntas = []
		cantpreguntas = 0


		if self.codacta == 4:
			#Vivienda transitoria
			if self.request.method == "GET":
				cantpreguntas = self.cantidadPreguntasItemEvaluar('MISFO-VITR')

			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
 			ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria4Form,
    		extra=cantpreguntas, can_delete=True, can_delete_extra=True
			)
		elif self.codacta == 5:
			#Hogar de paso
			if self.request.method == "GET":
				cantpreguntas = self.cantidadPreguntasItemEvaluar('MISFO-HOPA')

			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria5Form,
				extra=cantpreguntas, can_delete=True, can_delete_extra=True
				)
		elif self.codacta == 6:
			#Hogar comunitario
			if self.request.method == "GET":
				cantpreguntas = self.cantidadPreguntasItemEvaluar('MISFO-HOGC')

			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria6Form,
				extra=cantpreguntas, can_delete=True, can_delete_extra=True
				)
			
		elif self.codacta == 7:
			if self.request.method == "GET":
				cantpreguntas = self.cantidadPreguntasItemEvaluar('MISFO-HOGG')

			#Hogar Hogar geriatrico o de larga estancia
			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria7Form,
				extra=cantpreguntas, can_delete=True, can_delete_extra=True
				)			
		else:
			#Centros vida
			if self.request.method == "GET":
				cantpreguntas = self.cantidadPreguntasItemEvaluar('MISFO-ECV')

			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria8Form,
				extra=cantpreguntas, can_delete=True, can_delete_extra=True
				)
			
		
		if self.request.method == "GET":
			
			itemFormset = ItemActaViviendaTransitoriaFormSet(prefix='itemactaviviendatransitoria')
			listapreguntas = self.listaPreguntasItemEvaluar()			
			for subform, data in zip(itemFormset.forms, listapreguntas):
				subform.initial = data

			return {
                'itemactaviviendatransitoria': itemFormset,
                'funcionariosactaviviendatransitoria': FuncionariosActaViviendaTransitoriaFormSet(prefix='funcionariosactaviviendatransitoria'),
                'atiendeactaviviendatransitoria': AtiendeActaViviendaTransitoriaFormSet(prefix='atiendeactaviviendatransitoria'),
                
			}
		else:
			return {
                'itemactaviviendatransitoria': ItemActaViviendaTransitoriaFormSet(self.request.POST or None, prefix='itemactaviviendatransitoria'),               
                'funcionariosactaviviendatransitoria': FuncionariosActaViviendaTransitoriaFormSet(self.request.POST or None, prefix='funcionariosactaviviendatransitoria'),
                'atiendeactaviviendatransitoria': AtiendeActaViviendaTransitoriaFormSet(self.request.POST or None, prefix='atiendeactaviviendatransitoria'),
                
            }


class ActaViviendaTransitoriaUpdate(Sin_privilegio, ActaViviendaTransitoriaInline, generic.UpdateView):
	permission_required="sam.change_actaviviendatransitoria"
	login_url = 'cnf:login'
	codacta = 4


	def get_context_data(self, **kwargs):
		ctx = super(ActaViviendaTransitoriaUpdate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		self.codacta = self.kwargs.get('codacta')		
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['obj']=self.object
		ctx['idestablecimiento'] = idest
		ctx['codacta'] = self.codacta		
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx
	
	def get_named_formsets(self):

		if self.codacta == 4:
			#Vivienda transitoria
			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
 			ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria4Form,
    		extra=0, can_delete=True, can_delete_extra=True
			)
		elif self.codacta == 5:
			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria5Form,
				extra=0, can_delete=True, can_delete_extra=True
				)
		elif self.codacta == 6:
			#Hogar comunitario
			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria6Form,
				extra=0, can_delete=True, can_delete_extra=True
				)
			
		elif self.codacta == 7:
			#Hogar Hogar geriatrico o de larga estancia
			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria7Form,
				extra=0, can_delete=True, can_delete_extra=True
				)			
		else:
			#Centros vida
			ItemActaViviendaTransitoriaFormSet = inlineformset_factory(
				ActaViviendaTransitoria, ItemActaViviendaTransitoria, form=ItemActaViviendaTransitoria8Form,
				extra=0, can_delete=True, can_delete_extra=True
				)
		
		return {
		'itemactaviviendatransitoria': ItemActaViviendaTransitoriaFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='itemactaviviendatransitoria'),
		'funcionariosactaviviendatransitoria': FuncionariosActaViviendaTransitoriaFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='funcionariosactaviviendatransitoria'),
		'atiendeactaviviendatransitoria': AtiendeActaViviendaTransitoriaFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='atiendeactaviviendatransitoria')		
		}	

def delete_itemactaviviendatransitoria(request, pk, codacta):
	try:
		itemactaviviendatransitoria = ItemActaViviendaTransitoria.objects.get(id=pk)
		actaviviendatransitoria = ActaViviendaTransitoriaInline()
		idactagral = itemactaviviendatransitoria.actaviviendatransitoria.id
		actageneral = ActaViviendaTransitoria.objects.get(id=idactagral)		
	

	except ItemActaViviendaTransitoria.DoesNotExist:
		messages.success(
			request, 'Item a evaluar no existe'
			)
		return redirect('sam:actavivtrans_list', pk=itemactaviviendatransitoria.actaviviendatransitoria.id, codacta=codacta)

	itemactaviviendatransitoria.delete()	
	actageneral.save()

	messages.success(
		request, 'Item a evaluar eliminado satisfactoriamente'
		)
	return redirect('sam:actavivtrans_list', pk=itemactaviviendatransitoria.actaviviendatransitoria.id, codacta=codacta)

def delete_funcionariosactaviviendatransitoria(request, pk, codacta):
	try:
		funcionariosactaviviendatransitoria = FuncionariosActaViviendaTransitoria.objects.get(id=pk)
		actaviviendatransitoria = ActaViviendaTransitoriaInline()
		idactagral = funcionariosactaviviendatransitoria.actaviviendatransitoria.id
		actageneral = ActaViviendaTransitoria.objects.get(id=idactagral)		
	

	except FuncionariosActaViviendaTransitoria.DoesNotExist:
		messages.success(
			request, 'Funcionario no existe'
			)
		return redirect('sam:actavivtrans_list', pk=funcionariosactaviviendatransitoria.actaviviendatransitoria.id, codacta=codacta)

	funcionariosactaviviendatransitoria.delete()	
	actageneral.save()

	messages.success(
		request, 'Funcionario eliminado satisfactoriamente'
		)
	return redirect('sam:actavivtrans_list', pk=funcionariosactaviviendatransitoria.actaviviendatransitoria.id, codacta=codacta)


def delete_atiendeactaviviendatransitoria(request, pk):
	try:
		atiendeactaviviendatransitoria = AtiendeActaViviendaTransitoria.objects.get(id=pk)
		actaviviendatransitoria = ActaViviendaTransitoriaInline()
		idactagral = atiendeactaviviendatransitoria.actaviviendatransitoria.id
		actageneral = ActaViviendaTransitoria.objects.get(id=idactagral)		
	

	except AtiendeActaBodegasPatios.DoesNotExist:
		messages.success(
			request, 'Usuario que atiende no existe'
			)
		return redirect('sam:actavivtrans_list', pk=atiendeactaviviendatransitoria.actaviviendatransitoria.id, codacta=codacta)

	atiendeactaviviendatransitoria.delete()	
	actageneral.save()

	messages.success(
		request, 'Usuario que atiende eliminado satisfactoriamente'
		)
	return redirect('sam:actavivtrans_list', pk=atiendeactaviviendatransitoria.actaviviendatransitoria.id, codacta=codacta)


# Preguntas Tipo Acta

class TipoActaList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_tipoacta"
	model = TipoActa
	template_name='sam/tipoactaspreguntas_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(TipoActaList,self).get_context_data(**kwargs)		
		return context


class PreguntaList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_pregunta"
	model = Pregunta
	template_name='sam/preguntas_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(PreguntaList,self).get_context_data(**kwargs)
		codacta = self.kwargs.get('codacta')	
		pregunta = Pregunta.objects.filter(bloque__tipoacta_id=codacta).all()
		tipoacta = TipoActa.objects.filter(pk=codacta).first()
		
		context['obj'] = pregunta
		context['codacta'] = codacta
		context['tipoacta'] = tipoacta.descripcion		
		return context


class PreguntasInline():
	form_class = PreguntaForm	
	model = Pregunta
	template_name = 'sam/preguntas_form.html'

	
	def form_valid(self, form):		
		codacta = self.kwargs.get('codacta')

		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		self.object.save()
		return redirect('sam:preguntas_list', codacta=codacta)

	
	def formset_evaluacionpregunta_valid(self, formset):		
		evaluacionpregunta = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in evaluacionpregunta:
			seg.pregunta = self.object
			seg.save()



class EvaluacionPreguntaCreate(Sin_privilegio, PreguntasInline, generic.CreateView):
	permission_required="sam.add_pregunta"
	login_url = 'cnf:login'


	def get_context_data(self, **kwargs):
		ctx = super(EvaluacionPreguntaCreate, self).get_context_data(**kwargs)		
		codacta = self.kwargs.get('codacta')
		tipoacta = TipoActa.objects.filter(id=codacta).first()
		bloque = Bloque.objects.filter(tipoacta=codacta).all()		
		ctx['named_formsets'] = self.get_named_formsets()		
		ctx['codacta'] = codacta
		ctx['bloque'] = bloque				
		ctx['tipoacta'] = tipoacta.descripcion
		return ctx

	
	def get_named_formsets(self):
		listapreguntas = []

		if self.request.method == "GET":
			return {            
                'evaluacionpregunta': EvaluacionPreguntaFormSet(prefix='evaluacionpregunta'),
			}
		else:
			return {
                'evaluacionpregunta': EvaluacionPreguntaFormSet(self.request.POST or None, prefix='evaluacionpregunta'),               
            }


class EvaluacionPreguntaUpdate(Sin_privilegio, PreguntasInline, generic.UpdateView):
	permission_required="sam.change_pregunta"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(EvaluacionPreguntaUpdate, self).get_context_data(**kwargs)		
		codacta = self.kwargs.get('codacta')
		tipoacta = TipoActa.objects.filter(id=codacta).first()
		bloque = Bloque.objects.filter(tipoacta=codacta).all()
		ctx['named_formsets'] = self.get_named_formsets()		
		ctx['obj']=self.object		
		ctx['codacta'] = codacta
		ctx['bloque'] = bloque		
		ctx['tipoacta'] = tipoacta.descripcion
		return ctx
	
	def get_named_formsets(self):		
		return {
		'evaluacionpregunta': EvaluacionPreguntaFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='evaluacionpregunta')
		}	

def delete_evaluacionpregunta(request, pk, codacta):
	try:
		evaluacionpregunta = EvaluacionPregunta.objects.get(id=pk)
		preguntasInline = PreguntasInline()
		idpregunta = evaluacionpregunta.pregunta.id
		pregunta = Pregunta.objects.get(id=idpregunta)		
	

	except EvaluacionPregunta.DoesNotExist:
		messages.success(
			request, 'Evaluación de la pregunta no existe'
			)
		return redirect('sam:preguntas_list', codacta=codacta)

	evaluacionpregunta.delete()	
	pregunta.save()

	messages.success(
		request, 'Evaluación eliminada satisfactoriamente'
		)
	return redirect('sam:preguntas_list', codacta=codacta)


#Actas de visitas a establecimientos carcelarios
class ActaCentroCarcelarioList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_atiendeactacentrocarcelario"
	model = ActaCentroCarcelario
	template_name='sam/actacentrocarcelario_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(ActaCentroCarcelarioList,self).get_context_data(**kwargs)
		pk = self.kwargs.get('idest')		
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-CARC').first()

		acta = ActaCentroCarcelario.objects.filter(establecimiento_id=pk).all()
		establecimiento = Establecimiento.objects.filter(id=pk).first()
		context['obj'] =acta		
		context['idestablecimiento'] = pk
		context['nomestablecimiento'] = establecimiento.razonsocial		
		return context

class ActaCentroCarcelarioInline():
	form_class = ActaCentroCarcelarioForm	
	model = ActaCentroCarcelario
	template_name = 'sam/actacentrocarcelario_form.html'

	def form_valid(self, form):		
		
		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		self.object.save()
		return redirect('sam:actaestcarcelario_list', idest=self.object.establecimiento.id)

	
	def formset_itemactacentrocarcelario_valid(self, formset):		
		itemactacentrocarcelario = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in itemactacentrocarcelario:
			seg.actacentrocarcelario = self.object
			seg.save()

	def formset_funcionariosactacentrocarcelario_valid(self, formset):		
		funcionariosactacentrocarcelario = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in funcionariosactacentrocarcelario:
			seg.actacentrocarcelario = self.object
			seg.save()

	def formset_atiendeactacentrocarcelario_valid(self, formset):		
		atiendeactacentrocarcelario = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in atiendeactacentrocarcelario:
			seg.actacentrocarcelario = self.object
			seg.save()


class ActaCentroCarcelarioCreate(Sin_privilegio, ActaCentroCarcelarioInline, generic.CreateView):
	permission_required="sam.add_actacentrocarcelario"
	login_url = 'cnf:login'


	def get_context_data(self, **kwargs):
		ctx = super(ActaCentroCarcelarioCreate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-CARC').first()

		
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['idestablecimiento'] = idest
		ctx['codtipoacta'] = tipoacta.pk
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx

	def cantidadPreguntasItemEvaluar(self):
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-CARC').first()
		cantpreguntas = 0
		if tipoacta:
			cantpreguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk).count()
		return cantpreguntas

	def listaPreguntasItemEvaluar(self):
		listapreguntas=[]	
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-CARC').first()
		print("Tipo acta = ", tipoacta)

		preguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk)
		print(preguntas)
		
		for p in preguntas:
			diccitemacta = {
			'actacentrocarcelario':self.model.id,
			'pregunta':p.id,		
			'evaluacion':'',
			'puntaje':0,
			'habilitada':p.habilitada		
			}
			
			listapreguntas.append(diccitemacta)

		return listapreguntas

	def get_named_formsets(self):
		listapreguntas = []
		cantpreguntas = 0

		if self.request.method == "GET":
			cantpreguntas = self.cantidadPreguntasItemEvaluar()

			itemactacentrocarcelarioFormSet = inlineformset_factory(
				ActaCentroCarcelario, ItemActaCentroCarcelario, form=ItemActaCentroCarcelarioForm,
				extra=cantpreguntas, can_delete=True, can_delete_extra=True
				)
			
			itemFormset = itemactacentrocarcelarioFormSet(prefix='itemactacentrocarcelario')
			listapreguntas = self.listaPreguntasItemEvaluar()			
			for subform, data in zip(itemFormset.forms, listapreguntas):
				subform.initial = data

			return {
                'itemactacentrocarcelario': itemFormset,
                'funcionariosactacentrocarcelario': FuncionariosActaCentroCarcelarioFormSet(prefix='funcionariosactacentrocarcelario'),
                'atiendeactacentrocarcelario': AtiendeActaCentroCarcelarioFormSet(prefix='atiendeactacentrocarcelario'),
                
			}
		else:
			itemactacentrocarcelarioFormSet = inlineformset_factory(
				ActaCentroCarcelario, ItemActaCentroCarcelario, form=ItemActaCentroCarcelarioForm,
				extra=0, can_delete=True, can_delete_extra=True
				)
			
			return {
                'itemactacentrocarcelario': itemactacentrocarcelarioFormSet(self.request.POST or None, prefix='itemactacentrocarcelario'),               
                'funcionariosactacentrocarcelario': FuncionariosActaCentroCarcelarioFormSet(self.request.POST or None, prefix='funcionariosactacentrocarcelario'),
                'atiendeactacentrocarcelario': AtiendeActaCentroCarcelarioFormSet(self.request.POST or None, prefix='atiendeactacentrocarcelario'),
            }


class ActaCentroCarcelarioUpdate(Sin_privilegio, ActaCentroCarcelarioInline, generic.UpdateView):
	permission_required="sam.change_actacentrocarcelario"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaCentroCarcelarioUpdate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')			
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-CARC').first()

		ctx['named_formsets'] = self.get_named_formsets()
		ctx['obj']=self.object
		ctx['idestablecimiento'] = idest	
		ctx['codtipoacta'] = tipoacta.pk		
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx
	
	def get_named_formsets(self):

	
		#Vivienda transitoria
		itemactacentrocarcelarioFormSet = inlineformset_factory(
 		ActaCentroCarcelario, ItemActaCentroCarcelario, form=ItemActaCentroCarcelarioForm,
    	extra=0, can_delete=True, can_delete_extra=True
		)
		
		return {
		'itemactacentrocarcelario': itemactacentrocarcelarioFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='itemactacentrocarcelario'),
		'funcionariosactacentrocarcelario': FuncionariosActaCentroCarcelarioFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='funcionariosactacentrocarcelario'),
		'atiendeactacentrocarcelario': AtiendeActaCentroCarcelarioFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='atiendeactacentrocarcelario')		
		}	

def delete_itemactacentrocarcelario(request, pk, codacta):
	try:
		itemactacentrocarcelario = ItemActaCentroCarcelario.objects.get(id=pk)
		actacentrocarcelarioinline = ActaCentroCarcelarioInline()
		idactagral = itemactacentrocarcelario.actacentrocarcelario.id
		actageneral = ActaCentroCarcelario.objects.get(id=idactagral)		
	

	except ItemActaCentroCarcelario.DoesNotExist:
		messages.success(
			request, 'Item a evaluar no existe'
			)
		return redirect('sam:actaestcarcelario_list', idest=actageneral.establecimiento.id)

	itemactacentrocarcelario.delete()	
	actageneral.save()

	messages.success(
		request, 'Item a evaluar eliminado satisfactoriamente'
		)
	return redirect('sam:actaestcarcelario_list', idest=actageneral.establecimiento.id)

def delete_funcionariosactacentrocarcelario(request, pk):
	try:
		funcionariosactacentrocarcelario = FuncionariosActaCentroCarcelario.objects.get(id=pk)
		actacentrocarcelarioinline = ActaCentroCarcelarioInline()
		idactagral = funcionariosactacentrocarcelario.actacentrocarcelario.id
		actageneral = ActaCentroCarcelario.objects.get(id=idactagral)		
	

	except FuncionariosActaCentroCarcelario.DoesNotExist:
		messages.success(
			request, 'Funcionario no existe'
			)
		return redirect('sam:actaestcarcelario_list', idest=actageneral.establecimiento.id)

	funcionariosactacentrocarcelario.delete()	
	actageneral.save()

	messages.success(
		request, 'Funcionario eliminado satisfactoriamente'
		)
	return redirect('sam:actaestcarcelario_list', idest=actageneral.establecimiento.id)


def delete_atiendeactacentrocarcelario(request, pk):
	try:
		atiendeactacentrocarcelario = AtiendeActaCentroCarcelario.objects.get(id=pk)
		actacentrocarcelarioinline = ActaCentroCarcelarioInline()
		idactagral = atiendeactacentrocarcelario.actacentrocarcelario.id
		actageneral = ActaCentroCarcelario.objects.get(id=idactagral)		
	

	except AtiendeActaCentroCarcelario.DoesNotExist:
		messages.success(
			request, 'Usuario que atiende no existe'
			)
		return redirect('sam:actaestcarcelario_list', idest=actageneral.establecimiento.id)

	atiendeactacentrocarcelario.delete()	
	actageneral.save()

	messages.success(
		request, 'Usuario que atiende eliminado satisfactoriamente'
		)
	return redirect('sam:actaestcarcelario_list', idest=actageneral.establecimiento.id)

#Actas de vigilancias droguerías y farmacia
class ActaDrogueriaList(Sin_privilegio, generic.ListView):
	permission_required="sam.view_actadrogueria"
	model = ActaDrogueria
	template_name='sam/actadrogueria_list.html'
	context_object_name = "obj"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		context = super(ActaDrogueriaList,self).get_context_data(**kwargs)
		pk = self.kwargs.get('idest')		
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-DROG').first()

		acta = ActaDrogueria.objects.filter(establecimiento_id=pk).all()
		establecimiento = Establecimiento.objects.filter(id=pk).first()
		context['obj'] =acta		
		context['idestablecimiento'] = pk
		context['nomestablecimiento'] = establecimiento.razonsocial		
		return context

class ActaDrogueriaInline():
	form_class = ActaDrogueriaForm	
	model = ActaDrogueria
	template_name = 'sam/actadrogueria_form.html'

	def form_valid(self, form):		
		
		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:				
				formset_save_func(formset)
			else:
				formset.save()

		self.object.save()
		return redirect('sam:actadrogueria_list', idest=self.object.establecimiento.id)

	
	def formset_itemactadroguerias_valid(self, formset):		
		itemactadroguerias = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in itemactadroguerias:
			seg.actadrogueria = self.object
			seg.save()

	def formset_funcionariosactadrogueria_valid(self, formset):		
		funcionariosactadrogueria = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in funcionariosactadrogueria:
			seg.actadrogueria = self.object
			seg.save()

	def formset_atiendeactadrogueria_valid(self, formset):		
		atiendeactadrogueria = formset.save(commit=False)  # self.save_formset(formset, contact)
		for obj in formset.deleted_objects:
			obj.delete()

		for seg in atiendeactadrogueria:
			seg.actadrogueria = self.object
			seg.save()


class ActaDrogueriaCreate(Sin_privilegio, ActaDrogueriaInline, generic.CreateView):
	permission_required="sam.add_actadrogueria"
	login_url = 'cnf:login'


	def get_context_data(self, **kwargs):
		ctx = super(ActaDrogueriaCreate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-DROG').first()

		
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		ctx['named_formsets'] = self.get_named_formsets()
		ctx['idestablecimiento'] = idest
		ctx['codtipoacta'] = tipoacta.pk
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx

	def cantidadPreguntasItemEvaluar(self):
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-DROG').first()
		cantpreguntas = 0
		if tipoacta:
			cantpreguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk).count()
		return cantpreguntas

	def listaPreguntasItemEvaluar(self):
		listapreguntas=[]	
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-DROG').first()
		preguntas = Pregunta.objects.filter(bloque__tipoacta_id=tipoacta.pk)
		
		
		for p in preguntas:
			diccitemacta = {
			'actadrogueria':self.model.id,
			'pregunta':p.id,		
			'evaluacion':'',
			'puntaje':0,
			'habilitada':p.habilitada		
			}
			
			listapreguntas.append(diccitemacta)

		return listapreguntas

	def get_named_formsets(self):
		listapreguntas = []
		cantpreguntas = 0

		if self.request.method == "GET":
			cantpreguntas = self.cantidadPreguntasItemEvaluar()

			itemactadrogueriasFormSet = inlineformset_factory(
				ActaDrogueria, ItemActaDroguerias, form=ItemActaDrogueriasForm,
				extra=cantpreguntas, can_delete=True, can_delete_extra=True
				)
			
			itemFormset = itemactadrogueriasFormSet(prefix='itemactadroguerias')
			listapreguntas = self.listaPreguntasItemEvaluar()			
			for subform, data in zip(itemFormset.forms, listapreguntas):
				subform.initial = data

			return {
                'itemactadroguerias': itemFormset,
                'funcionariosactadrogueria': FuncionariosActaDrogueriaFormSet(prefix='funcionariosactadrogueria'),
                'atiendeactadrogueria': AtiendeActaDrogueriaFormSet(prefix='atiendeactadrogueria'),
                
			}
		else:
			itemactadrogueriasFormSet = inlineformset_factory(
				ActaDrogueria, ItemActaDroguerias, form=ItemActaDrogueriasForm,
				extra=0, can_delete=True, can_delete_extra=True
				)
			
			return {
                'itemactadroguerias': itemactadrogueriasFormSet(self.request.POST or None, prefix='itemactadroguerias'),               
                'funcionariosactadrogueria': FuncionariosActaDrogueriaFormSet(self.request.POST or None, prefix='funcionariosactadrogueria'),
                'atiendeactadrogueria': AtiendeActaDrogueriaFormSet(self.request.POST or None, prefix='atiendeactadrogueria'),
            }


class ActaDrogueriaUpdate(Sin_privilegio, ActaDrogueriaInline, generic.UpdateView):
	permission_required="sam.change_actadrogueria"
	login_url = 'cnf:login'

	def get_context_data(self, **kwargs):
		ctx = super(ActaDrogueriaUpdate, self).get_context_data(**kwargs)
		idest = self.kwargs.get('idest')			
		establecimiento = Establecimiento.objects.filter(id=idest).first()
		tipoacta = TipoActa.objects.filter(idtipoacta='MISFO-DROG').first()

		ctx['named_formsets'] = self.get_named_formsets()
		ctx['obj']=self.object
		ctx['idestablecimiento'] = idest	
		ctx['codtipoacta'] = tipoacta.pk		
		ctx['nomestablecimiento'] = establecimiento.razonsocial
		return ctx
	
	def get_named_formsets(self):		
		itemactadrogueriasFormSet = inlineformset_factory(
 		ActaDrogueria, ItemActaDroguerias, form=ItemActaDrogueriasForm,
    	extra=0, can_delete=True, can_delete_extra=True
		)
		
		return {
		'itemactadroguerias': itemactadrogueriasFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='itemactadroguerias'),
		'funcionariosactadrogueria': FuncionariosActaDrogueriaFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='funcionariosactadrogueria'),
		'atiendeactadrogueria': AtiendeActaDrogueriaFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='atiendeactadrogueria')		
		}	

def delete_itemactadroguerias(request, pk):
	try:
		itemactadroguerias = ItemActaDroguerias.objects.get(id=pk)
		idactagral = itemactadroguerias.actadrogueria.id
		actageneral = ActaDrogueria.objects.get(id=idactagral)		
	

	except ItemActaDroguerias.DoesNotExist:
		messages.success(
			request, 'Item a evaluar no existe'
			)
		return redirect('sam:actadrogueria_list', idest=actageneral.establecimiento.id)

	itemactadroguerias.delete()	
	actageneral.save()

	messages.success(
		request, 'Item a evaluar eliminado satisfactoriamente'
		)
	return redirect('sam:actadrogueria_list', idest=actageneral.establecimiento.id)

def delete_funcionariosactadrogueria(request, pk):
	try:
		funcionariosactadrogueria = FuncionariosActaDrogueria.objects.get(id=pk)		
		idactagral = funcionariosactadrogueria.actadrogueria.id
		actageneral = ActaDrogueria.objects.get(id=idactagral)		
	

	except FuncionariosActaDrogueria.DoesNotExist:
		messages.success(
			request, 'Funcionario no existe'
			)
		return redirect('sam:actadrogueria_list', idest=actageneral.establecimiento.id)

	funcionariosactadrogueria.delete()	
	actageneral.save()

	messages.success(
		request, 'Funcionario eliminado satisfactoriamente'
		)
	return redirect('sam:actadrogueria_list', idest=actageneral.establecimiento.id)


def delete_atiendeactadrogueria(request, pk):
	try:
		atiendeactadrogueria = AtiendeActaDrogueria.objects.get(id=pk)
		idactagral = atiendeactadrogueria.actadrogueria.id
		actageneral = ActaDrogueria.objects.get(id=idactagral)		
	

	except AtiendeActaDrogueria.DoesNotExist:
		messages.success(
			request, 'Usuario que atiende no existe'
			)
		return redirect('sam:actadrogueria_list', idest=actageneral.establecimiento.id)

	atiendeactadrogueria.delete()	
	actageneral.save()

	messages.success(
		request, 'Usuario que atiende eliminado satisfactoriamente'
		)
	return redirect('sam:actadrogueria_list', idest=actageneral.establecimiento.id)
