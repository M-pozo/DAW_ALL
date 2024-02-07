from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.exceptions import ValidationError


#UD7.2.c / UD7.2.d BEGIN
class BaseCreateUpdateMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['titulo_actualizacion'] = self.titulo_actualizacion
            context['url_borrado'] = reverse_lazy(f'{self.url_borrado}', args=[self.object.pk])
        else:
            context['titulo_creacion'] = self.titulo_creacion
            context['url_borrado'] = None
        return context
#UD7.2.c / UD7.2.d END

#UD7.2.e BEGIN
class BaseDeleteMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        context['mensaje_confirmacion'] = self.mensaje_confirmacion
        return context
#UD7.2.e BEGIN

#UD7.2.f BEGIN
class DeleteViewMixin:
    def form_valid(self, request, *args, **kwargs):
        try:
            super().delete(*args, request, **kwargs)
            messages.success(self.request, f"{self.model.__name__} eliminado correctamente".format(self))
        except:
            messages.error(self.request, "Existen dependencias para el Modulo. Elimine antes dichas dependencias".format(self))
        return HttpResponseRedirect(reverse(self.success_url))
#UD7.2.f END

#UD7.2.j BEGIN
class OrderingMixin():
    def get_queryset(self):
        model = self.model
        ordenar = self.request.GET.get('ordenar', None)

        if ordenar == 'asc':
            return model.objects.all().order_by('id')
        elif ordenar == 'desc':
            return model.objects.all().order_by('-id')
        else:
            return model.objects.all().order_by('id')
#UD7.2.j END

#UD7.4.a BEGIN
class SuccessMessageCreateUpdateMixin(SuccessMessageMixin):
    def get_success_url(self):
        object = self.object
        return reverse_lazy(self.success_url, kwargs={'pk': object.id})
#UD7.4.a BEGIN
#UD8.3 BEGIN
class DecoratorsMixin():
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
#UD8.3 END

#UD10.3.c
class ProtectedDeleteMixin:
    def verificar_dependencias(self, instance):
        if ValidationError:
            raise ValidationError("No se puede realizar la operación de borrado porque existen dependencias.")
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.verificar_dependencias(instance)
        return super().destroy(request, *args, **kwargs)