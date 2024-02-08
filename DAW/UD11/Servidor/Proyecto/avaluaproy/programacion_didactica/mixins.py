from .models import PondRA, PondCriterio, PondCritUD
from django.db.models import Sum
from django.contrib import messages
from django.views.generic.edit import FormMixin
from rest_framework import serializers


#UD7.2.g, UD7.2.h, UD7.2.i BEGIN
#UD7.2.g
"""
class PonderacionRAMixin():

    def validate(self, data): 
        resultado_aprendizaje = data['resultado_aprendizaje']
        porcentaje = data['porcentaje']
        total_porcentaje = 0
        if resultado_aprendizaje and porcentaje:
            modulo = resultado_aprendizaje.modulo


            if self.object:
                porcentajes = PondRA.objects.filter(resultado_aprendizaje__modulo=modulo).exclude(pk=self.instance.pk).values_list('porcentaje', flat=True) or 0
            else:
                porcentajes = PondRA.objects.filter(resultado_aprendizaje__modulo=modulo).values_list('porcentaje', flat=True) or 0

            for por in porcentajes:
                total_porcentaje += por
            total_nuevo = total_porcentaje + porcentaje

            if total_nuevo > 100:
                raise serializers.ValidationError("La suma de los porcentajes de los RAs para el módulo {modulo} supera el 100%.")
            
            return data
#UD7.2.h
class PonderacionCEMixin():

    def validate(self, data):
        resultado_aprendizaje = data['criterio_evaluacion'].resultado_aprendizaje
        porcentaje = data['porcentaje']
        total_porcentaje = 0
        if resultado_aprendizaje and porcentaje:


            if self.object:
                porcentajes = PondCriterio.objects.filter(criterio_evaluacionresultado_aprendizaje=resultado_aprendizaje).exclude(pk=self.instance.pk).values_list('porcentaje', flat=True) or 0
            else:
                porcentajes = PondCriterio.objects.filter(criterio_evaluacionresultado_aprendizaje=resultado_aprendizaje).values_list('porcentaje', flat=True) or 0

            for por in porcentajes:
                total_porcentaje += por
            total_nuevo = total_porcentaje + porcentaje


            if total_nuevo > 100:
                raise serializers.ValidationError("La suma de los CE en el RA {resultado_aprendizaje} supera el 100%.")

            return data
#UD7.2.i
class PonderacionCEUDMixin():

    def validate(self, data):
        criterio_evaluacion = data['criterio_evaluacion']
        porcentaje = data['porcentaje']
        total_porcentaje = 0
        if criterio_evaluacion and porcentaje:


            if self.object:
                porcentajes = PondCritUD.objects.filter(criterio_evaluacion=criterio_evaluacion).exclude(pk=self.instance.pk).values_list('porcentaje', flat=True) or []
            else:
                porcentajes = PondCritUD.objects.filter(criterio_evaluacion=criterio_evaluacion).values_list('porcentaje', flat=True) or []

            for por in porcentajes:
                total_porcentaje += por
            total_nuevo = total_porcentaje + porcentaje


            if total_nuevo > 100:
                raise serializers.ValidationError("La suma de los CE de las unidades supera el 100%.")

            return data
#UD7.2.g, UD7.2.h, UD7.2.i END

"""