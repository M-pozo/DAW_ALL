from django.contrib import admin

# Register your models here.
#UD6.4.c BEGIN
#UD6.4.f BEGIN
from .models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD

class UnidadAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('codigo', 'nombre')
    search_fields = ['codigo', 'nombre']
    ordering = ['-id']

class InstEvalAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    ordering = ['codigo']

class PondRAAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('resultado_aprendizaje', 'porcentaje')
    list_filter = ['resultado_aprendizaje']
    search_fields = ['resultado_aprendizaje__codigo', 'resultado_aprendizaje__descripcion']
    preserve_filters = True
    ordering = ['resultado_aprendizaje__codigo']

class PondCritAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('criterio_evaluacion', 'porcentaje')
    list_filter = ['criterio_evaluacion__resultado_aprendizaje']
    search_fields = ['criterio_evaluacion__codigo', 'criterio_evaluacion__descripcion', 'resultado_aprendizaje__codigo', 'resultado_aprendizaje__descripcion']
    preserve_filters = True
    ordering = ['criterio_evaluacion__codigo']

class PondCritUDAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('unidad', 'criterio_evaluacion' , 'porcentaje')
    list_filter = ['criterio_evaluacion', 'unidad']
    search_fields = ['criterio_evaluacion__codigo', 'criterio_evaluacion__descripcion', 'resultado_aprendizaje__codigo', 'resultado_aprendizaje__descripcion', 'unidad__nombre']
    preserve_filters = True
    ordering = ['unidad__nombre', 'criterio_evaluacion__codigo']

#UD6.4.f END
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(InstEvaluacion, InstEvalAdmin)
admin.site.register(PondRA, PondRAAdmin)
admin.site.register(PondCriterio, PondCritAdmin)
admin.site.register(PondCritUD, PondCritUDAdmin)
#UD6.4.c END