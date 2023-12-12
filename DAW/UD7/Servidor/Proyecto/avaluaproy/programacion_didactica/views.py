from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin

from programacion_didactica.models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD
from .form import UnidadForm, InstEvaluacionForm, PondRAForm, PondCriterioForm, PondCritUDForm

from common.mixins import DeleteViewMixin, OrderingMixin, BaseCreateUpdateMixin, SuccessMessageCreateUpdateMixin
from .mixins import PonderacionRAMixin


#UD6.7.a BEGIN
#UD7.2.a BEING
#Unidad BEGIN
class UDListView(ListView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_list.html'

class UDDetailView(DetailView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_detail.html'

class UDCreateView(BaseCreateUpdateMixin, CreateView, SuccessMessageMixin):
    model = Unidad
    form_class = UnidadForm
    success_message = "Unidad creada exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'unidad_update'

class UDUpdateView(BaseCreateUpdateMixin, UpdateView, SuccessMessageMixin):
    model = Unidad
    form_class = UnidadForm
    success_message = "Unidad actualizada exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'unidad_update'

class UDDeleteView(DeleteViewMixin, DeleteView):
    model = Unidad
    template_name = 'common/base_confirm_delete.html'
    success_url = 'unidad_list'

#Unidad END

#InstEvauacion BEGIN
class InstEvListView(ListView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_list.html'

class InstEvDetailView(DetailView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_detail.html'

class InstEvCreateView(BaseCreateUpdateMixin, CreateView, SuccessMessageMixin):
    model = InstEvaluacion
    form_class = InstEvaluacionForm
    success_message = "Instrumoneto de evaluación creada exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ie_update'

class InstEvUpdateView(BaseCreateUpdateMixin, UpdateView, SuccessMessageMixin):
    model = InstEvaluacion
    form_class = InstEvaluacionForm
    success_message = "Instrumoneto de evaluación actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ie_update'

class InstEvDeleteView(DeleteViewMixin, DeleteView):
    model = InstEvaluacion
    template_name = 'common/base_confirm_delete.html'
    success_url = 'ie_list'
#InstEvauacion END

#PondRA BEGIN
class PondRAListView(ListView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_list.html'

class PondRADetailView(DetailView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_detail.html'

class PondRACreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = PondRA
    form_class = PondRAForm
    success_message = "Ponderación RA creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ra_update'

class PondRAUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = PondRA
    form_class = PondRAForm
    success_message = "Ponderación RA actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ra_update'

class PondRADeleteView(DeleteView):
    model = PondRA
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('pond_ra_list')
#PondRA END

#PondCriterio BEGIN
class PondCritListView(ListView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ce_list.html'

class PondCritDetailView(DetailView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ce_detail.html'

class PondCritCreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = PondCriterio
    form_class = PondCriterioForm
    success_message = "Ponderación CE actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ce_update'


class PondCritUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = PondCriterio
    form_class = PondCriterioForm
    success_message = "Ponderación CE actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ce_update'


class PondCritDeleteView(DeleteViewMixin, DeleteView):
    model = PondCriterio
    template_name = 'common/base_confirm_delete.html'
    success_url = 'pond_ce_list'
#PondCriterio END

#PondCritUD BEGIN
class PondCritUDListView(ListView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_list.html'

class PondCritUDDetailView(DetailView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_detail.html'

class PondCritUDCreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = PondCritUD
    form_class = PondCritUDForm
    success_message = "Ponderación CE por UD actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ce_ud_update'

class PondCritUDUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = PondCritUD
    form_class = PondCritUDForm
    success_message = "Ponderación CE por UD actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ce_ud_update'

class PondCritUDDeleteView(DeleteViewMixin, DeleteView):
    model = PondCritUD
    template_name = 'common/base_confirm_delete.html'
    success_url = 'pond_ce_ud_list'
#PondCritUD END
#UD7.2.a END
#UD6.7.a END