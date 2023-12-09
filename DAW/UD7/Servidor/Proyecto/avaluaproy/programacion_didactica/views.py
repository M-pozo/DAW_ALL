from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect
from programacion_didactica.models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD


#UD6.7.a BEGIN
#UD7.2.a BEING
#Unidad BEGIN
class UDListView(ListView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_list.html'

class UDDetailView(DetailView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_detail.html'

class UDCreateView(CreateView):
    model = Unidad
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('unidad_create')

class UDUpdateView(UpdateView):
    model = Unidad
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('unidad_update')

class UDDeleteView(DeleteView):
    model = Unidad
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('unidad_list')
    #Verificacion dependencias
    def delete(self, request, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))
#Unidad END

#InstEvauacion BEGIN
class InstEvListView(ListView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_list.html'

class InstEvDetailView(DetailView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_detail.html'

class InstEvCreateView(CreateView):
    model = InstEvaluacion
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ie_create')

class InstEvUpdateView(UpdateView):
    model = InstEvaluacion
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ie_update')

class InstEvDeleteView(DeleteView):
    model = InstEvaluacion
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('ie_list')
    #Verificacion dependencias
    def delete(self, request, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))
#InstEvauacion END

#PondRA BEGIN
class PondRAListView(ListView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_list.html'

class PondRADetailView(DetailView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_detail.html'

class PondRACreateView(CreateView):
    model = PondRA
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ra_create')

class PondRAUpdateView(UpdateView):
    model = PondRA
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ra_update')

class PondRADeleteView(DeleteView):
    model = PondRA
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ra_list')
#PondRA END

#PondCriterio BEGIN
class PondCritListView(ListView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ce_list.html'

class PondCritDetailView(DetailView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ce_detail.html'

class PondCritCreateView(CreateView):
    model = PondCriterio
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ce_create')

class PondCritUpdateView(UpdateView):
    model = PondCriterio
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ce_update')

class PondCritDeleteView(DeleteView):
    model = PondCriterio
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ce_list')
#PondCriterio END

#PondCritUD BEGIN
class PondCritUDListView(ListView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_list.html'

class PondCritUDDetailView(DetailView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_detail.html'

class PondCritUDCreateView(CreateView):
    model = PondCritUD
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ce_ud_create')

class PondCritUDUpdateView(UpdateView):
    model = PondCritUD
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ce_ud_update')

class PondCritUDDeleteView(DeleteView):
    model = PondCritUD
    template_name = 'common/base_create_update.html'
    success_url = reverse_lazy('pond_ce_ud_list')
#PondCritUD END

#UD7.2.a END
#UD6.7.a END