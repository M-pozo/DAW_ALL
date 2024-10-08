from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Proyecto

class ProyectoMixin(SuccessMessageMixin):
    model = Proyecto
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('proyecto_update', kwargs={'pk': object.id})
    