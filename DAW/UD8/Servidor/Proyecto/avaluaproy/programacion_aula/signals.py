from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Alumno, CriterioEvalUD, CalificacionUDCE

@receiver(post_save, sender=Alumno)
def pregenerar_calificaciones(sender, instance, created, **kwargs):
    if created:
        criterios_evaluacion = CriterioEvalUD.objects.filter(unidad=range(1, 9))

        for criterio in criterios_evaluacion:
            CalificacionUDCE.objects.create(
                alumno=instance,
                unidad=criterio.unidad,
                crit_evaluacion=criterio.criterio_evaluacion,
                calificacion=None
            )

# Registra la señal
post_save.connect(pregenerar_calificaciones, sender=Alumno)