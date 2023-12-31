from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from core.models import Modulo, ResAprendizaje, CritEvaluacion


class ModuloListView(ListView):
    model = Modulo
    template_name = 'core/modulo_list.html'


class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'


class RAListView(ListView):
    model = ResAprendizaje
    template_name = 'core/ra_list.html'


class RADetailView(DetailView):
    model = ResAprendizaje
    template_name = 'core/ra_detail.html'


class CEListView(ListView):
    model = CritEvaluacion
    template_name = 'core/ce_list.html'


class CEDetailView(DetailView):
    model = CritEvaluacion
    template_name = 'core/ce_detail.html'

def listing(request):
    contact_list = Modulo.objects.all()
    paginator = Paginator(contact_list, 1)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})