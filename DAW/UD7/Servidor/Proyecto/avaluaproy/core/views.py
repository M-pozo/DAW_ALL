from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect
from core.models import Modulo, ResAprendizaje, CritEvaluacion
from common.mixins import DeleteViewMixin, OrderingMixin, BaseCreateUpdateMixin
from .form import ModuloForm, ResAprendizajeForm, CritEvaluacionForm

#UD7.2.a BEGIN
#Modulo BEGIN
class ModuloListView(OrderingMixin, ListView):
    model = Modulo
    template_name = 'core/modulo_list.html'

class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'

class ModCreateView(BaseCreateUpdateMixin, CreateView):
    model = Modulo
    form_class = ModuloForm
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('modulo_create')

class ModUpdateView(BaseCreateUpdateMixin, UpdateView):
    model = Modulo
    form_class = ModuloForm
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('modulo_update')

class ModDeleteView(DeleteView, DeleteViewMixin):
    model = Modulo
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('modulo_list')
    fields = [];

#Modulo END

#ResAprendizaje BEGIN
class RAListView(ListView):
    model = ResAprendizaje
    template_name = 'core/ra_list.html'

class RADetailView(DetailView):
    model = ResAprendizaje
    template_name = 'core/ra_detail.html'

class RACreateView(CreateView):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ra_create')

class RAUpdateView(UpdateView):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ra_update')

class RADeleteView(DeleteView):
    model = ResAprendizaje
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ra_list')
    #Verificacion dependencias
    def delete(self, request, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))
#ResAprendizaje end

#CritEvaluacion BEGIN
class CEListView(ListView):
    model = CritEvaluacion
    template_name = 'core/ce_list.html'


class CEDetailView(DetailView):
    model = CritEvaluacion
    template_name = 'core/ce_detail.html'

class CECreateView(CreateView):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ce_create')

class CEUpdateView(UpdateView):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ce_update')

class CEDeleteView(DeleteView):
    model = CritEvaluacion
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ce_list')
    #Verificacion dependencias
    def delete(self, request, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))
#CritEvaluacion END
#UD7.2.a END