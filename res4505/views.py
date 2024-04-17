from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy


from cnf.views import Sin_privilegio
from .forms import PeriodoreporteForm, Resolucion4505ctrlForm
from .models import Periodo_envio, Resolucion4505ctrl, Resolucion4505det 

# Create your views here.


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name='base/baseres4505.html'
    login_url='cnf:login'


class PeriodoreporteList(Sin_privilegio, generic.ListView):
    permission_required="res4505.view_periodo_envio"    
    model = Periodo_envio
    template_name='res4505/periodoenvio_list.html'
    context_object_name = "obj"
    login_url = 'cnf:login'


class PeriodoreporteCreate(LoginRequiredMixin, generic.CreateView):
    permission_required="res4505.add_periodo_envio"        
    model = Periodo_envio
    template_name = 'res4505/periodoenvio_form.html'
    context_object_name = 'obj'
    form_class = PeriodoreporteForm
    success_url = reverse_lazy('res4505:periodoenv_list')
    login_url = 'cnf:login'


class PeriodoreporteUpdate(LoginRequiredMixin, generic.UpdateView):
    permission_required="res4505.add_periodo_envio"        
    model = Periodo_envio
    template_name = 'res4505/periodoenvio_form.html'
    context_object_name = 'obj'
    form_class = PeriodoreporteForm
    success_url = reverse_lazy('res4505:periodoenv_list')
    login_url = 'cnf:login'


class PeriodoreporteDelete(Sin_privilegio, generic.DeleteView):
    permission_required='res4505:delete_periodo_envio'
    model=Periodo_envio
    template_name="res4505/periodoenvio_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('res4505:periodoenv_list')


class Resolucion4505List(Sin_privilegio, generic.ListView):
    permission_required="res4505.view_resolucion4505ctrl"    
    model = Resolucion4505ctrl
    template_name='res4505/regctrl_list.html'
    context_object_name = "obj"
    login_url = 'cnf:login'

class Resolucion4505Create(LoginRequiredMixin, generic.CreateView):
    permission_required="res4505.add_resolucion4505ctrl"        
    model = Resolucion4505ctrl
    template_name = 'res4505/regctrl_forms.html'
    context_object_name = 'obj'
    form_class = Resolucion4505ctrlForm
    success_url = reverse_lazy('res4505:regctrl_list')
    login_url = 'cnf:login'


class Resolucion4505Uptate(LoginRequiredMixin, generic.UpdateView):
    permission_required="res4505.change_resolucion4505ctrl"        
    model = Resolucion4505ctrl
    template_name = 'res4505/regctrl_forms.html'
    context_object_name = 'obj'
    form_class = Resolucion4505ctrlForm
    success_url = reverse_lazy('res4505:regctrl_list')
    login_url = 'cnf:login'


class Registrotipo2Create(LoginRequiredMixin, generic.CreateView):
    permission_required="res4505.add_resolucion4505det"        
    model = Resolucion4505det
    template_name = 'res4505/regctrl_forms.html'
    context_object_name = 'obj'
    form_class = Resolucion4505ctrlForm
    success_url = reverse_lazy('res4505:regctrl_list')
    login_url = 'cnf:login'

    def get_context_data(self, **kwargs):
        context = super(Registrotipo2Create,self).get_context_data(**kwargs)
        pk = self.kwargs.get('id') # El mismo nombre que en tu URL
        enca = Resolucion4505ctrl.objects.get(pk=pk)
        context['enca'] = enca
        context['id'] = pk              
        return context

    def get_success_url(self):
        contactoaislado=self.request.POST['contactoaislado']
        return reverse_lazy('cvd:contactopacnotif_edit', kwargs={'pk':contactoaislado})


class Registrotipo2Update(LoginRequiredMixin, generic.CreateView):
    permission_required="res4505.change_resolucion4505det"        
    model = Resolucion4505det
    template_name = 'res4505/regctrl_forms.html'
    context_object_name = 'obj'
    form_class = Resolucion4505ctrlForm
    success_url = reverse_lazy('res4505:regctrl_list')
    login_url = 'cnf:login'

    def get_context_data(self, **kwargs):
        context = super(Registrotipo2Update,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk') # El mismo nombre que en tu URL
        detalle= Resolucion4505det.objects.get(pk=pk)     
        context['idregtipo1'] = detalle.pk              
        return context

    def get_success_url(self):
        idregtipo1=self.request.POST['resolucion4505ctrl']
        return reverse_lazy('res4505:regctrl_edit', kwargs={'pk':idregtipo1})