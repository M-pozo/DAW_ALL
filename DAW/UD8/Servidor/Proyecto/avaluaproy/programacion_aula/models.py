from django.db import models
from common.models import Persona, Localizacion
from programacion_didactica.models import Unidad
from core.models import CritEvaluacion, ResAprendizaje, Modulo
# Create your models here.

#UD9.4 BEGIN
class Alumno(Persona, Localizacion):
    pass

class CriterioEvalUD(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=False, blank=False)
    criterio_evaluacion = models.ForeignKey(CritEvaluacion, on_delete=models.PROTECT, null=False, blank=False)


class CalificacionUDCE(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False, blank=False)
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=False, blank=False)
    crit_evaluacion = models.ForeignKey(CritEvaluacion, on_delete=models.PROTECT, null=False, blank=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class CalificacionCE(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False, blank=False)
    crit_evaluacion = models.ForeignKey(CritEvaluacion, on_delete=models.PROTECT, null=False, blank=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class CalificacionRA(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False, blank=False)
    res_aprendizaje = models.ForeignKey(ResAprendizaje, on_delete=models.PROTECT, null=False, blank=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class CalificacionTotal(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False, blank=False)
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT, null=False, blank=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

#UD9.4 END