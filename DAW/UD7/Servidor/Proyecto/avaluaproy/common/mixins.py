from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

#UD7.2.c
#UD7.2.d BEGIN
class BaseCreateUpdateMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        model_name = self.model.__name__
        url_mapping = {
            'Modelo': 'modulo_delete',
            'ResAprendizaje': 'ra_delete',
            'CritEvaluacion': 'ce_delete',
            'Unidad': 'unidad_delete',
            'InstEvaluacion': 'ie_delete',
            'PondRA': 'pond_ra_delete',
            'PondCriterio': 'pond_ce_delete',
            'PondCritUD': 'pond_ce_ud_delete',
        }
        url_name = url_mapping.get(model_name, 'default_delete')
        if self.object:
            context['titulo_actualizacion'] = f"Actualizar {model_name}"
            context['url_borrado'] = reverse_lazy(f'{url_name}', args=[self.object.pk])
        else:
            context['titulo_creacion'] = f"Crear {model_name}"
            context['url_borrado'] = None

        return context
#UD7.2.d END

#UD7.2.e BEGIN
class BaseConfirmDeleteMixin():
    template_name = 'common/base_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.model.__name__
        url_mapping = {
            'Modelo': 'modulo_list',
            'ResAprendizaje': 'ra_list',
            'CritEvaluacion': 'ce_list',
            'Unidad': 'unidad_list',
            'InstEvaluacion': 'ie_list',
            'PondRA': 'pond_ra_list',
            'PondCriterio': 'pond_ce_list',
            'PondCritUD': 'pond_ce_ud_list',
        }
        url_name = url_mapping.get(model_name, 'default_list')
        context['titulo'] = "Delete confirm"
        context['mensaje_confirmacion'] = "Usted esta seguro que desea eliminar"
        context['url_cancelado'] = reverse_lazy(f'{url_name}')
        return context
#UD7.2.e END

#UD7.2.f BEGIN
class DeleteViewMixin():
    def delete(self, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
        except:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse('home'))
#UD7.2.f END

#UD7.2.j BEGIN
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
#UD7.2.j END

#UD7.4.a BEGIN

#UD7.4.a BEGIN
