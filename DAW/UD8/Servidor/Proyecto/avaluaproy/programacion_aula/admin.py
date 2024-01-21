from django.contrib import admin

# Register your models here.
from .models import Alumno, CriterioEvalUD, CalificacionUDCE, CalificacionCE, CalificacionRA, CalificacionTotal

class AlumnoAdmin(admin.ModelAdmin):
    list_display = list_display_links =('nombre', 'apellido', 'ciudad', 'codigo_postal', 'direccion')
    search_fields = ['nombre', 'apellido', 'ciudad']

class CriterioEvalUDAdmin(admin.ModelAdmin):
    list_display = list_display_links =('unidad', 'criterio_evaluacion')
    search_fields = ['unidad', 'criterio_evaluacion']

class CalificacionUDCEAdmin(admin.ModelAdmin):
    list_display = list_display_links =('alumno', 'unidad', 'crit_evaluacion', 'calificacion')
    search_fields = ['alumno', 'unidad', 'crit_evaluacion', 'calificacion']

class CalificacionCEAdmin(admin.ModelAdmin):
    list_display = list_display_links =('alumno', 'crit_evaluacion', 'calificacion')
    search_fields = ['alumno', 'crit_evaluacion', 'calificacion']

class CalificacionRAAdmin(admin.ModelAdmin):
    list_display = list_display_links =('alumno', 'res_aprendizaje', 'calificacion')
    search_fields = ['alumno', 'res_aprendizaje', 'calificacion']

class CalificacionTotalAdmin(admin.ModelAdmin):
    list_display = list_display_links =('alumno', 'modulo', 'calificacion')
    search_fields = ['alumno', 'modulo', 'calificacion']

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(CriterioEvalUD, CriterioEvalUDAdmin)
admin.site.register(CalificacionUDCE, CalificacionUDCEAdmin)
admin.site.register(CalificacionCE, CalificacionCEAdmin)
admin.site.register(CalificacionRA, CalificacionRAAdmin)
admin.site.register(CalificacionTotal, CalificacionTotalAdmin)