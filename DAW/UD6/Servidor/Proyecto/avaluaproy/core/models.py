from django.db import models

# Create your models here.

#UD6.3.a BEGIN
#UD6.3.b BEGIN
#UD6.4.e BEGIN
class Modulo(models.Model):
    codigo = models.CharField(max_length = 10, verbose_name="Código", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Modulos'

class ResAprendizaje(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT, verbose_name="Módulo")
    codigo = models.CharField(max_length = 10, verbose_name="Código")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.codigo + '.' + self.descripcion[:100]
    #UD6.3.c
    class Meta:
        unique_together = ["modulo", "codigo"]
        verbose_name_plural = 'Resultados Aprendizaje'

class CritEvaluacion(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResAprendizaje, on_delete=models.PROTECT, verbose_name="Resultado de aprendizaje")
    codigo = models.CharField(max_length = 4, verbose_name="Código")
    descripcion = models.TextField(verbose_name="Descripción")
    minimo = models.BooleanField(verbose_name="Mínimo")

    def __str__(self):
        return self.resultado_aprendizaje + '.' + self.codigo + ' - ' + self.descripcion[:100]
    #UD6.3.c
    class Meta:
        unique_together = ["resultado_aprendizaje", "codigo"]
        verbose_name_plural = 'Criterios Evaluación'

#UD6.4.e END
#UD6.3.b END
#UD6.3.a END