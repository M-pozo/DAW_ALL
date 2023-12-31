from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import DecoratorsMixin


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'


class PanelView(DecoratorsMixin, TemplateView):
    template_name = 'common/panel.html'
