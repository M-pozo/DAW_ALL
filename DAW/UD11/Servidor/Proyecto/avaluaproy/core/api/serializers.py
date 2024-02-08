from rest_framework import serializers
from core.models import *

#UD10.2 BEGIN
#Modulo BEGIN
class ModuloListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = Modulo
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.nombre

class ModuloDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modulo
        fields = "__all__"
#Modulo FINIS

#RA BEGIN
class RAListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = ResAprendizaje
        fields = ('id', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.descripcion[:50]

class RADetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResAprendizaje
        fields = "__all__"
#RA FINIS
        
#CE BEGIN
class CEListSerializer(serializers.ModelSerializer):

    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = CritEvaluacion
        fields = ('id', 'minimo', 'descripcion_short')
    
    def get_descripcion_short(self, obj):
        return obj.descripcion[:50]

class CEDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CritEvaluacion
        fields = "__all__"
#CE FINIS
#UD10.2 END