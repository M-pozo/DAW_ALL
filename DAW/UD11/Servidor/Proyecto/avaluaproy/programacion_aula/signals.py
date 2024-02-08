from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Alumno, CriterioEvalUD, CalificacionUDCE

#UD9.5 BEGIN
@receiver(post_save, sender=Alumno)
def pregenerar_calificaciones(sender, instance, **kwargs):
    criterios_evaluacion = CriterioEvalUD.objects.all()
    for criterio in criterios_evaluacion:
        CalificacionUDCE.objects.create(
            alumno=instance,
            unidad=criterio.unidad,
            crit_evaluacion=criterio.criterio_evaluacion,
            calificacion=None
        )

post_save.connect(pregenerar_calificaciones, sender=Alumno)
#UD9.5 END