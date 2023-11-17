from django.db import models

# Create your models here.

#UD6.3.a BEGIN
class Modulo(models.Model):
    codigo = models.CharField(max_length = 10, verbose_name="Código", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name="Nombre", unique=True)

class ResAprendizaje(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT, verbose_name="Módulo")
    codigo = models.CharField(max_length = 10, verbose_name="Código")
    descirpcion = models.TextField(verbose_name="Descripción")


class CritEvaluacion(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResAprendizaje, on_delete=models.PROTECT, verbose_name="Código")
    codigo = models.CharField(max_length = 4, verbose_name="Código")
    descirpcion = models.TextField(verbose_name="Descripción")
    minimo = models.CharField(max_length = 10, verbose_name="Código", unique=True)
#UD6.3.a END