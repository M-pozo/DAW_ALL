#Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
#Models
from programacion_didactica.models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD
#Form
from .form import UnidadForm, InstEvaluacionForm, PondRAForm, PondCriterioForm, PondCritUDForm
#Mixins
from common.mixins import DeleteViewMixin, OrderingMixin, BaseCreateUpdateMixin, SuccessMessageCreateUpdateMixin, BaseDeleteMixin
#from .mixins import PonderacionRAMixin


#UD6.7.a BEGIN
#UD7.2.a BEING
#Unidad BEGIN
class UDListView(OrderingMixin, ListView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_list.html'

class UDDetailView(DetailView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_detail.html'

class UDCreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = Unidad
    form_class = UnidadForm
    success_message = "Unidad creada exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'unidad_update'
    titulo_creacion = 'Crear Unidad'

class UDUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = Unidad
    form_class = UnidadForm
    success_message = "Unidad actualizada exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'unidad_update'
    titulo_actualizacion = 'Actualizar Unidad'
    url_borrado = 'unidad_delete'

class UDDeleteView(BaseDeleteMixin, DeleteViewMixin, DeleteView):
    model = Unidad
    template_name = 'common/base_confirm_delete.html'
    success_url = 'unidad_list'
    titulo = "Eliminar Unidad"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta unidad?"

#Unidad END

#InstEvauacion BEGIN
class InstEvListView(OrderingMixin, ListView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_list.html'

class InstEvDetailView(DetailView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_detail.html'

class InstEvCreateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, CreateView):
    model = InstEvaluacion
    form_class = InstEvaluacionForm
    success_message = "Instrumoneto de evaluación creada exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ie_update'
    titulo_creacion = 'Crear Instrumento de evaluación'

class InstEvUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = InstEvaluacion
    form_class = InstEvaluacionForm
    success_message = "Instrumoneto de evaluación actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'ie_update'
    titulo_actualizacion = 'Actualizar Instrumento de evaluación'
    url_borrado = 'ie_delete'

class InstEvDeleteView(BaseDeleteMixin, DeleteViewMixin, DeleteView):
    model = InstEvaluacion
    template_name = 'common/base_confirm_delete.html'
    success_url = 'ie_list'
    titulo = "Eliminar Instrumento de evaluación"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar este instrumento de evaluación?"
#InstEvauacion END

#PondRA BEGIN
class PondRAListView(OrderingMixin, ListView):
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
    titulo_creacion = 'Crear Ponderación por RA'

class PondRAUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = PondRA
    form_class = PondRAForm
    success_message = "Ponderación RA actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ra_update'
    titulo_actualizacion = 'Actualizar Ponderación por RA'
    url_borrado = 'pond_ra_delete'

class PondRADeleteView(BaseDeleteMixin,  DeleteViewMixin, DeleteView):
    model = PondRA
    template_name = 'common/base_confirm_delete.html'
    success_url = 'pond_ra_list'
    titulo = "Eliminar Ponderación por resultado de aprendizaje"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta ponderación por resultado de aprendizaje?"
#PondRA END

#PondCriterio BEGIN
class PondCritListView(OrderingMixin, ListView):
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
    titulo_creacion = 'Crear Ponderación por CE'

class PondCritUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = PondCriterio
    form_class = PondCriterioForm
    success_message = "Ponderación CE actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ce_update'
    titulo_actualizacion = 'Actualizar Ponderación por CE'
    url_borrado = 'pond_ce_delete'

class PondCritDeleteView(BaseDeleteMixin, DeleteViewMixin, DeleteView):
    model = PondCriterio
    template_name = 'common/base_confirm_delete.html'
    success_url = 'pond_ce_list'
    titulo = "Eliminar Ponderación por criterio"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta ponderación por criterio?"
#PondCriterio END

#PondCritUD BEGIN
class PondCritUDListView(OrderingMixin, ListView):
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
    titulo_creacion = 'Crear Ponderación por CE de UD'

class PondCritUDUpdateView(SuccessMessageCreateUpdateMixin, BaseCreateUpdateMixin, UpdateView):
    model = PondCritUD
    form_class = PondCritUDForm
    success_message = "Ponderación CE por UD actualizado exitosamente"
    template_name = 'common/base_create_update.html'
    success_url = 'pond_ce_ud_update'
    titulo_actualizacion = 'Actualizar Ponderación por CE de UD'
    url_borrado = 'pond_ce_ud_delete'

class PondCritUDDeleteView(BaseDeleteMixin, DeleteViewMixin, DeleteView):
    model = PondCritUD
    template_name = 'common/base_confirm_delete.html'
    success_url = 'pond_ce_ud_list'
    titulo = "Eliminar Ponderación por CE de UD"
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta ponderación por CE de UD?"
#PondCritUD END
#UD7.2.a END
#UD6.7.a END