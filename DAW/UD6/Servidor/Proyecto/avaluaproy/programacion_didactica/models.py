from django.db import models

# Create your models here.

#UD6.3.a BEGIN
#UD6.3.b BEGIN
#UD6.4.e BEGIN
class Unidad(models.Model):
    codigo = models.CharField(max_length = 4, verbose_name="Código", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.codigo + ' - ' + self.nombre
    
    class Meta:
        verbose_name_plural = 'Unidad'
    
class InstEvaluacion(models.Model):
    codigo = models.CharField(max_length = 4, verbose_name="Código", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name="Nombre", unique=True)
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.codigo + ' - ' + self.nombre
    
    class Meta:
        verbose_name_plural = 'Instrumentos Evaluación'

class PondRA(models.Model):
    resultado_aprendizaje = models.ForeignKey('core.ResAprendizaje', on_delete=models.PROTECT, verbose_name="Resultados Apredizaje")
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Porcentaje")

    def __str__(self):
        return str(self.resultado_aprendizaje) + ' - ' + str(self.porcentaje)
    
    class Meta:
        verbose_name_plural = 'Ponderación RA'

class PondCriterio(models.Model):
    criterio_evaluacion = models.ForeignKey('core.CritEvaluacion', on_delete=models.PROTECT, verbose_name="Criterios Evaluacion")
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Porcentaje")

    def __str__(self):
        return str(self.criterio_evaluacion) + ' - ' + str(self.porcentaje)
    
    class Meta:
        verbose_name_plural = 'Ponderación Criterios'

class PondCritUD(models.Model):
    criterio_evaluacion = models.ForeignKey('core.CritEvaluacion', on_delete=models.PROTECT, verbose_name="Criterios Evaluacion")
    unidad = models.ForeignKey(Unidad , on_delete=models.PROTECT, verbose_name="Unidad")
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Porcentaje")

    def __str__(self):
        return str(self.unidad) + ' - ' + str(self.criterio_evaluacion) + ' - (' + str(self.porcentaje) + ')'
    #UD6.3.c
    class Meta:
        unique_together = ["criterio_evaluacion", "unidad"]
        verbose_name_plural = 'Ponderación Criterios Unidad'

#UD6.4.e END
#UD6.3.b END
#UD6.3.a END