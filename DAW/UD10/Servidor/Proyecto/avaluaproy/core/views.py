#Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#Models
from core.models import Modulo, ResAprendizaje, CritEvaluacion
#Form
from .form import ModuloForm, ResAprendizajeForm, CritEvaluacionForm
#Mixins
from common.mixins import DeleteViewMixin, OrderingMixin, BaseCreateUpdateMixin, SuccessMessageCreateUpdateMixin, BaseDeleteMixin, DecoratorsMixin


#UD7.2.a BEGIN
#Modulo BEGIN
class ModuloListView(DecoratorsMixin, OrderingMixin, ListView):
    model = Modulo
    template_name = 'core/modulo_list.html'

class ModuloDetailView(DecoratorsMixin, DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'

class ModCreateView(DecoratorsMixin, SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = Modulo
    form_class = ModuloForm
    success_message = "Modulo creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'modulo_update'
    titulo_creacion = 'Crear Modulo'
    
class ModUpdateView(DecoratorsMixin, SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = Modulo
    form_class = ModuloForm
    success_message = "Modulo actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'modulo_update'
    titulo_actualizacion = 'Actualizar Modulo'
    url_borrado = 'modulo_delete'

class ModDeleteView(DecoratorsMixin, BaseDeleteMixin, DeleteViewMixin, DeleteView):
    model = Modulo
    template_name = 'common/base_confirm_delete.html'
    success_url = 'modulo_list'
    titulo = "Eliminar Modulo"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar este objeto?"
#Modulo END

#ResAprendizaje BEGIN
class RAListView(DecoratorsMixin, OrderingMixin, ListView):
    model = ResAprendizaje
    template_name = 'core/ra_list.html'

class RADetailView(DecoratorsMixin, DetailView):
    model = ResAprendizaje
    template_name = 'core/ra_detail.html'

class RACreateView(DecoratorsMixin, SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    success_message = "RA creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ra_update'
    titulo_creacion = 'Crear Resultado de aprendizaje'

class RAUpdateView(DecoratorsMixin, SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = ResAprendizaje
    form_class = ResAprendizajeForm
    success_message = "RA creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ra_update'
    titulo_actualizacion = 'Actualizar Resultado de aprendizaje'
    url_borrado = 'ra_delete'

class RADeleteView(DecoratorsMixin, BaseDeleteMixin, DeleteViewMixin, DeleteView):
    model = ResAprendizaje
    template_name = 'common/base_confirm_delete.html'
    success_url = 'ra_list'
    titulo = "Eliminar Resultado de aprendizaje"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar este Resultado de aprendizaje?"
#ResAprendizaje END

#CritEvaluacion BEGIN
class CEListView(DecoratorsMixin, OrderingMixin, ListView):
    model = CritEvaluacion
    template_name = 'core/ce_list.html'

class CEDetailView(DecoratorsMixin, DetailView):
    model = CritEvaluacion
    template_name = 'core/ce_detail.html'

class CECreateView(DecoratorsMixin, SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    success_message = "CE creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ce_update'
    titulo_creacion = 'Crear Criterio de evaluación'

class CEUpdateView(DecoratorsMixin, SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = CritEvaluacion
    form_class = CritEvaluacionForm
    success_message = "CE creado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ce_update'
    titulo_actualizacion = 'Actualizar Criterio de evaluación'
    url_borrado = 'ce_delete'

class CEDeleteView(DecoratorsMixin, BaseDeleteMixin, DeleteViewMixin, DeleteView):
    model = CritEvaluacion
    template_name = 'common/base_confirm_delete.html'
    success_url = 'ce_list'
    titulo = "Eliminar Criterio de Evaluación"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar este Criterio de Evaluación?"
#CritEvaluacion END
#UD7.2.a END