
# Create your views here.
from django.shortcuts import render # Para FBV
from django.views.generic import TemplateView # Para CBV
from django.shortcuts import get_object_or_404
from .models import Proyecto


def home_view(request):
    proyectos = Proyecto.objects.all()
    context={'proyectos': proyectos}
    return render(request, 'portfolio/home.html', context)

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        cat_id = kwargs.get('cat_id')
        context['proyectos'] = Proyecto.objects.filter(categorias__id=cat_id) if cat_id else Proyecto.objects.all()
        return context

def proyecto_view(request,pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    context = {'proyecto': proyecto}
    return render(request,'portfolio/proyecto.html',context)

class ProyectoView(TemplateView):
    template_name = 'portfolio/proyecto.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProyectoView, self).get_context_data(**kwargs)
        context['proyecto'] = get_object_or_404(Proyecto, id=kwargs['pk'])
        return context

def contacto_view(request):
    context = {'full_name': 'Miguel Pozo'}
    return render(request,'portfolio/contacto.html',context)

class ContactoView(TemplateView):
    template_name = 'portfolio/contacto.html'

    def get_context_data(self, **kwargs):
        context = super(ContactoView, self).get_context_data(**kwargs)
        context['full_name'] ='Miguel Pozo'
        return context