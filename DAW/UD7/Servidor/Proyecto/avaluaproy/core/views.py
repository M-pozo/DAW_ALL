from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect
from django.contrib import messages
from core.models import Modulo, ResAprendizaje, CritEvaluacion
from common.mixins import DeleteViewMixin, OrderingMixin, BaseCreateUpdateMixin, SuccessMessageCreateUpdateMixin
from .form import ModuloForm, ResAprendizajeForm, CritEvaluacionForm
from django.contrib.messages.views import SuccessMessageMixin


#UD7.2.a BEGIN
#Modulo BEGIN
class ModuloListView(OrderingMixin, ListView):
    model = Modulo
    template_name = 'core/modulo_list.html'

class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'

class ModCreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = Modulo
    form_class = ModuloForm
    success_message = "Modulo creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'modulo_update'

class ModUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = Modulo
    form_class = ModuloForm
    success_message = "Modulo actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'modulo_update'

class ModDeleteView(DeleteViewMixin, DeleteView):
    model = Modulo
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('modulo_list')
#Modulo END

#ResAprendizaje BEGIN
class RAListView(ListView):
    model = ResAprendizaje
    template_name = 'core/ra_list.html'

class RADetailView(DetailView):
    model = ResAprendizaje
    template_name = 'core/ra_detail.html'

class RACreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    success_message = "RA creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ra_update'

class RAUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    success_message = "RA creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ra_update'

class RADeleteView(DeleteViewMixin, DeleteView):
    model = ResAprendizaje
    template_name = 'common/base_confirm_delete.html'
    success_url = 'ra_list'
#ResAprendizaje END

#CritEvaluacion BEGIN
class CEListView(ListView):
    model = CritEvaluacion
    template_name = 'core/ce_list.html'

class CEDetailView(DetailView):
    model = CritEvaluacion
    template_name = 'core/ce_detail.html'

class CECreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    success_message = "CE creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ce_update'

class CEUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    success_message = "CE creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ce_update'

class CEDeleteView(DeleteViewMixin, DeleteView):
    model = CritEvaluacion
    template_name = 'common/base_confirm_delete.html'
    success_url = 'ce_list'
#CritEvaluacion END
#UD7.2.a END