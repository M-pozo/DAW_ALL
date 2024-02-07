from programacion_aula.models import *
from programacion_didactica.models import *
from programacion_aula.models import *

def CalcularNota(alumno_id):
    # Obtener todas las calificaciones del alumno
    calificaciones_udce = CalificacionUDCE.objects.filter(alumno_id=alumno_id)
    calificaciones_ce = CalificacionCE.objects.filter(alumno_id=alumno_id)
    calificaciones_ra = CalificacionRA.objects.filter(alumno_id=alumno_id)

    # Calcular la calificación total por unidad de competencia (UDCE)
    calificacion_udce_total = sum(calificacion.calificacion for calificacion in calificaciones_udce)

    # Calcular la calificación total por criterio de evaluación (CE)
    calificacion_ce_total = sum(calificacion.calificacion for calificacion in calificaciones_ce)

    # Calcular la calificación total por resultado de aprendizaje (RA)
    calificacion_ra_total = sum(calificacion.calificacion for calificacion in calificaciones_ra)

    # Calcular la calificación total final (posiblemente aplicando ponderaciones)
    calificacion_total_final = calificacion_udce_total + calificacion_ce_total + calificacion_ra_total

    return calificacion_total_final