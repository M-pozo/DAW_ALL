from django.contrib import admin

# Register your models here.
from .models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD

class UnidadAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('nombre', )
    search_fields = ['nombre']

class InstEvaluacionAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('titulo', 'descripcion', 'year')

class PondRAAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('nombre', )
    search_fields = ['nombre']

class PondCriterioAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('nombre', )
    search_fields = ['nombre']

class PondCritUDAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('nombre', )
    search_fields = ['nombre']

admin.site.register(Unidad, UnidadAdmin)
admin.site.register(InstEvaluacion, InstEvaluacionAdmin)
admin.site.register(PondRA, PondRAAdmin)
admin.site.register(PondCriterio, PondCriterioAdmin)
admin.site.register(PondCritUD, PondCritUDAdmin)