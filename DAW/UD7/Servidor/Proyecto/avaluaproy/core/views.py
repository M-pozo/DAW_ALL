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
    template_name = 'common/base_create_update.html'
    success_message = "Modulo creado exitosamente"
    success_url = 'modulo_update'

class ModUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView, SuccessMessageMixin):
    model = Modulo
    form_class = ModuloForm
    template_name = 'common/base_create_update.html'
    success_message = "Modulo actualizado exitosamente"
    success_url = 'modulo_update'


class ModDeleteView(DeleteViewMixin, DeleteView):
    model = Modulo
    template_name = 'common/base_confirm_delete.html'
    success_url = 'modulo_list'
#Modulo END

#ResAprendizaje BEGIN
class RAListView(ListView):
    model = ResAprendizaje
    template_name = 'core/ra_list.html'

class RADetailView(DetailView):
    model = ResAprendizaje
    template_name = 'core/ra_detail.html'

class RACreateView(BaseCreateUpdateMixin, CreateView, SuccessMessageMixin):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    template_name = 'common/base_create_update.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('ra_update', kwargs={'pk': object.id})

class RAUpdateView(BaseCreateUpdateMixin, UpdateView, SuccessMessageMixin):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    template_name = 'common/base_create_update.html'
    

    def get_success_url(self):
        object = self.object
        return reverse_lazy('ra_update', kwargs={'pk': object.id})

class RADeleteView(DeleteView):
    model = ResAprendizaje
    template_name = 'common/base_confirm_delete.html'
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

class CECreateView(BaseCreateUpdateMixin, CreateView, SuccessMessageMixin):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    template_name = 'common/base_create_update.html'
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ce_update', kwargs={'pk': object.id})

class CEUpdateView(BaseCreateUpdateMixin, UpdateView, SuccessMessageMixin):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    template_name = 'common/base_create_update.html'
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ce_update', kwargs={'pk': object.id})

class CEDeleteView(DeleteView):
    model = CritEvaluacion
    template_name = 'common/base_confirm_delete.html'
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