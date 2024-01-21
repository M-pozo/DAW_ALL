from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length = 128, null=False, verbose_name="Nombre")
    apellido = models.CharField(max_length = 256, null=False, verbose_name="Apellido")

    class Meta:
        abstract = True

class Localizacion(models.Model):
    direccion = models.CharField(max_length = 256, null=False, verbose_name="Dirección")
    codigo_postal = models.CharField(max_length = 5, null=False, verbose_name="Código postal")
    ciudad = models.CharField(max_length = 256, null=False, verbose_name="Ciudad")
    class Meta:
        abstract = True