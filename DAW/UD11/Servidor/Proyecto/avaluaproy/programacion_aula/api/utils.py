from programacion_aula.models import *
from programacion_didactica.models import *
from programacion_aula.models import *
from django.db.models import Sum
from rest_framework import response

#UD10.3.d BEGIN
def crear_calificaciones(alumno_id, modulo_id):
    #Obtener CalificacionUDCE por alumno
    calificaciones_udce = CalificacionUDCE.objects.filter(alumno__id=alumno_id)

    # Recorrer todas las CalificacionUDCE y crear las calificacionesCE
    for calificacion_udce in calificaciones_udce:
        CalificacionCE.objects.create(
            alumno=calificacion_udce.alumno,
            crit_evaluacion=calificacion_udce.crit_evaluacion,
            calificacion=calificacion_udce.calificacion
        )

    # Obtener CalificacionCE por alumno
    calificaciones_ce = CalificacionCE.objects.filter(alumno__id=alumno_id)

    # Recorrer todas las CalificacionCE y crear las CalificacionRA
    for calificacion_ce in calificaciones_ce:
        CalificacionRA.objects.create(
            alumno=calificacion_ce.alumno,
            res_aprendizaje=calificacion_ce.crit_evaluacion.resultado_aprendizaje,
            calificacion=calificacion_ce.calificacion
        )

    # Sumar todas las calificaciones RA 
    calificaciones_ra_sum = CalificacionRA.objects.filter(alumno__id=alumno_id).aggregate(total=Sum('calificacion'))
    if calificaciones_ra_sum['total'] != None:
        calificaciones_ra = calificaciones_ra_sum['total']/100
    else:
        calificaciones_ra = 0

    alumnos = Alumno.objects.all()
    modulos = Modulo.objects.all() 
    for alumno in alumnos:
        if alumno.id == int(alumno_id):
            for modulo in modulos:
                if modulo.id == int(modulo_id):
                    CalificacionTotal.objects.update_or_create(
                            alumno=alumno,
                            modulo=modulo,
                            calificacion=calificaciones_ra
                        )
    

    return response.Response("Calificaciones creadas exitosamente.")

#Limpia todas las calificaciones 
def eliminar_calificaciones(alumno_id):
    CalificacionCE.objects.filter(alumno_id=alumno_id).delete()
    CalificacionRA.objects.filter(alumno_id=alumno_id).delete()
    CalificacionTotal.objects.filter(alumno_id=alumno_id).delete()
#UD10.3.d END