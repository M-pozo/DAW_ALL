from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class BaseCreateUpdateMixin():
    template_name = 'common/base_create_udpate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_creacion'] = "Crear"
        context['titulo_actualizacion'] = "Actualizar"
        context['url_borrado'] = "delete_url"
        return context
    
class BaseConfirmDeleteMixin():
    template_name = 'common/base_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Delete confirm"
        context['mensaje_confirmacion'] = "Usted esta seguro que desea eliminar"
        return context

class DeleteViewMixin():
    def delete(self, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))

class PonderacionRAMixin():
    def validacion(self):
        porcentaje_total = sum(self.porcentaje)
        if porcentaje_total > 100:
            error_message = "La suma de las ponderaciones de los RAs en el módulo supera el 100%."
            messages.error(self.request, error_message)

class  PonderacionCEMixin():
    def validacion(self):
        porcentaje_total = sum(self.porcentaje)
        if porcentaje_total > 100:
            error_message = "La suma de las ponderaciones de los CR's en el módulo supera el 100%."
            messages.error(self.request, error_message)

class  PonderacionCEUDMixin():
    def validacion(self):
        porcentaje_total = sum(self.porcentaje)
        if porcentaje_total > 100:
            error_message = "La suma de las ponderaciones de los CR's en el módulo supera el 100%."
            messages.error(self.request, error_message)

class OrderingMixin():
    def get_queryset(self):
        model = self.model
        ordenar = self.request.GET.get('ordenar', 'desc')

        if ordenar == 'asc':
            return model.objects.all().order_by('id')
        elif ordenar == 'desc':
            return model.objects.all().order_by('-id')
        else:
            return model.objects.all().order_by('id')