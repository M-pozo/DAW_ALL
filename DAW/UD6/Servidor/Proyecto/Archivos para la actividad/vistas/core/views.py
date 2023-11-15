from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Modulo, ResultadoAprendizaje, CriterioEvaluacion


class ModuloListView(ListView):
    model = Modulo
    template_name = 'core/modulo_list.html'


class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'


class RAListView(ListView):
    model = ResultadoAprendizaje
    template_name = 'core/ra_list.html'


class RADetailView(DetailView):
    model = ResultadoAprendizaje
    template_name = 'core/ra_detail.html'


class CEListView(ListView):
    model = CriterioEvaluacion
    template_name = 'core/ce_list.html'


class CEDetailView(DetailView):
    model = CriterioEvaluacion
    template_name = 'core/ce_detail.html'
