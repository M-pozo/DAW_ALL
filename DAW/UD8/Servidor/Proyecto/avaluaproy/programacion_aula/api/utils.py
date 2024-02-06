from programacion_aula.models import *

def calcular_nota_total_alumno_modulo(alumno, modulo):
    calificaciones_ce = CalificacionCE.objects.filter(alumno__id=alumno, crit_evaluacion__resultado_aprendizaje__modulo__id=modulo)
    calificaciones_ra = CalificacionRA.objects.filter(alumno__id=alumno, res_aprendizaje__modulo__id=modulo)
    total_ce = sum(calificacion.calificacion * calificacion.crit_evaluacion.pondcritud_set.first().porcentaje / 100 for calificacion in calificaciones_ce)
    total_ra = sum(calificacion.calificacion * calificacion.res_aprendizaje.pondra_set.first().porcentaje / 100 for calificacion in calificaciones_ra)
    
    # Calcular la nota total sumando las notas ponderadas de CE y RA
    nota_total = total_ce + total_ra
    
    # Guardar la nota total en la base de datos
    CalificacionTotal.objects.update_or_create(alumno__id=alumno, modulo__id=modulo, defaults={'calificacion': nota_total})