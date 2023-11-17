from django.contrib import admin

# Register your models here.
from .models import Modulo, ResAprendizaje, CritEvaluacion

class ModuloAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('nombre', )
    search_fields = ['nombre']

class ResAprendizajeAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('titulo', 'descripcion', 'year')

class CritEvaluacionAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('nombre', )
    search_fields = ['nombre']

admin.site.register(Modulo, ModuloAdmin)
admin.site.register(ResAprendizaje, ResAprendizajeAdmin)
admin.site.register(CritEvaluacion, CritEvaluacionAdmin)