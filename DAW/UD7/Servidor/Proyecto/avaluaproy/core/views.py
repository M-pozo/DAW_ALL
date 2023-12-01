from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect
from core.models import Modulo, ResAprendizaje, CritEvaluacion

#UD7.2.a BEGIN
#Modulo BEGIN
class ModuloListView(ListView):
    model = Modulo
    template_name = 'core/modulo_list.html'


class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'

class ModCreateView(CreateView):
    model = Modulo
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('modulo_create')

class ModUpdateView(UpdateView):
    model = Modulo
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('modulo_update')

class ModDeleteView(DeleteView):
    model = Modulo
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('modulo_delete')
    #Verificacion dependencias
    def delete(self, request, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))
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
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('ra_create')

class RAUpdateView(UpdateView):
    model = ResAprendizaje
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('ra_update')

class RADeleteView(DeleteView):
    model = ResAprendizaje
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('ra_delete')
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
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('ce_create')

class CEUpdateView(UpdateView):
    model = CritEvaluacion
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('ce_update')

class CEDeleteView(DeleteView):
    model = CritEvaluacion
    template_name = 'base_create_update.html'
    success_url = reverse_lazy('ce_delete')
    #Verificacion dependencias
    def delete(self, request, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))
#CritEvaluacion END
#UD7.2.a END