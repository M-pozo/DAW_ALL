from django.contrib import admin

# Register your models here.
#UD6.4.b BEGIN
#UD6.4.f BEGIN
from .models import Modulo, ResAprendizaje, CritEvaluacion

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre')
    list_display_link = ('codigo', 'nombre')
    search_fields = ['codigo', 'nombre']
    readonly_fields = ['id']
    ordering = ['codigo']

class ResAprendizajeAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('codigo', 'modulo', 'descripcion')
    list_filter = ['modulo']
    search_fields = ['codigo', 'descripcion']
    preserve_filters = True
    ordering = ['codigo']

class CritEvaluacionAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('resultado_aprendizaje', 'codigo', 'descripcion', 'minimo')
    list_filter = ('resultado_aprendizaje', 'minimo')
    search_fields = ['codigo', 'resultado_aprendizaje', 'descripcion']
    preserve_filters = True
    ordering = ['resultado_aprendizaje__codigo', 'codigo']

#UD6.4.f END
admin.site.register(Modulo, ModuloAdmin)
admin.site.register(ResAprendizaje, ResAprendizajeAdmin)
admin.site.register(CritEvaluacion, CritEvaluacionAdmin)
#UD6.4.b END