from rest_framework import serializers
from programacion_aula.models import *

#UD10.2 BEGIN
#Alumno BEGIN
class AlumnoListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = Alumno
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.nombre + " " + obj.apellido

class AlumnoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alumno
        fields = "__all__"
#Alumno FINIS
#CEUD BEGIN
class CEUDListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = CriterioEvalUD
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return "Unidad"

class CEUDDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CriterioEvalUD
        fields = "__all__"
#CEUD FINIS       
#CalificacionUDCE BEGIN
class CalUDCEListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = CalificacionUDCE
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.calificacion

class CalUDCEDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalificacionUDCE
        fields = "__all__"
#CalificacionUDCE FINIS
#CalificacionCE BEGIN
class CalCEListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = CalificacionCE
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.calificacion

class CalCEDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalificacionCE
        fields = "__all__"
#CalificacionCE FINIS
#CalificacionRA BEGIN
class CalRAListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = CalificacionRA
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.calificacion

class CalRADetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalificacionRA
        fields = "__all__"
#CalificacionRA FINIS
#CalificacionTotal BEGIN
class CalTotalListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = CalificacionTotal
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.calificacion

class CalTotalDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalificacionTotal
        fields = "__all__"
#CalificacionTotal FINIS
#UD10.2 END