
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

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['proyectos'] = Proyecto.objects.all()
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