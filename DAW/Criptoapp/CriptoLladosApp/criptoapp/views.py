# En views.py de tu aplicación Django

from django.shortcuts import render
from .models import Criptomoneda
from .utils import extraer_criptomonedas

def listar_criptomonedas(request):
    extraer_criptomonedas()
    criptomonedas = Criptomoneda.objects.all()
    return render(request, 'listar_criptomonedas.html', {'criptomonedas': criptomonedas})

