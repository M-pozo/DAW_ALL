from rest_framework import serializers
from programacion_didactica.models import *

#UD10.2 BEGIN
#Unidad BEGIN
class UnidadListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = Unidad
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.nombre

class UnidadDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unidad
        fields = "__all__"
#Unidad FINIS
        
#IE BEGIN
class IEListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = InstEvaluacion
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.descripcion[:50]

class IEDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstEvaluacion
        fields = "__all__"
#IE FINIS

#PondRA BEGIN
class PondRAListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = PondRA
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.porcentaje

class PondRADetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondRA
        fields = "__all__"
#PondRA FINIS
        
#PondCE BEGIN
class PondCEListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = PondCriterio
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.porcentaje

class PondCEDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondCriterio
        fields = "__all__"
#PondCE FINIS
        
#PondCEUD BEGIN
class PondCEUDListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = PondCritUD
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.porcentaje

class PondCEUDDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondCritUD
        fields = "__all__"
#PondCEUD FINIS
#UD10.2 END