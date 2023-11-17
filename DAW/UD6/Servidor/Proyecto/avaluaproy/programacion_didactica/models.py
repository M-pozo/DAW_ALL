from django.db import models

# Create your models here.

#UD6.3.a BEGIN
class Unidad(models.Model):
    codigo = models.CharField(max_length = 4, verbose_name="Código", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name="Nombre", unique=True)

class InstEvaluacion(models.Model):
    codigo = models.CharField(max_length = 4, verbose_name="Código", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name="Nombre", unique=True)
    descirpcion = models.TextField(verbose_name="Descripción")

class PondRA(models.Model):
    resultado_aprendizaje = models.ForeignKey('core.ResAprendizaje', on_delete=models.PROTECT, verbose_name="Resultados Apredizaje")
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Porcentaje")

class PondCriterio(models.Model):
    criterio_evaluacion = models.ForeignKey('core.CritEvaluacion', on_delete=models.PROTECT, verbose_name="Criterios Evaluacion")
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Porcentaje")

class PondCritUD(models.Model):
    criterio_evaluacion = models.ForeignKey('core.CritEvaluacion', on_delete=models.PROTECT, verbose_name="Criterios Evaluacion")
    unidad = models.ForeignKey(Unidad , on_delete=models.PROTECT, verbose_name="Código")
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Porcentaje")
#UD6.3.a END