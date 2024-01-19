from rest_framework import serializers
from portfolioapp.models import Proyecto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'nombre'
        )

class ProyectoSerializer(serializers.ModelSerializer):
    
    descripcion_short = serializers.SerializerMethodField()

    class Meta:
        model = Proyecto
        fields = (
            'id',
            'titulo',
            #'descripcion',
            'descripcion_short',
            'fecha_creacion',
            'imagen',
            #'categorias',
            'categoria_serialized'
        )

    def get_descripcion_short(self, obj):
        return obj.descripcion[:30]
    
    def get_categorias_serialized(self, obj):
        return CategoriaSerializer(obj.categorias, many=True, read_only=True).data
    
class ProyectoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = (
            'id',
            'titulo',
            'descripcion',
            'fecha_creacion',
            'year',
            'imagen',
            'categorias'
        )