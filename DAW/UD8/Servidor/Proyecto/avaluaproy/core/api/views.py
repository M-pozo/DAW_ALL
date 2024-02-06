from django import views
from rest_framework import mixins, viewsets, filters, views, status, response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from core.api.serializers import *
from core.models import *
from common.api.pagination import LargeResultsSetPagination, StandardResultsSetPagination, ShortResultsSetPagination

#UD10.3.a BEGIN
class ModuloListViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = ModuloListSerializer
    ordering = 'codigo'
    ordering_fields = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre']
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    def get_queryset(self):
        return Modulo.objects.all()
    
class ModuloDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = ModuloDetailSerializer
    def get_queryset(self):
        return Modulo.objects.all()
    
    def verificar_dependencias(self, instance):
        if instance.dependencias.exists():
            raise DependenciasError("No se puede realizar la operación de borrado porque existen dependencias.")
    
class RAListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = RAListSerializer
    ordering = 'codigo'
    ordering_fields = ['codigo', 'descripcion']
    search_fields = ['codigo', 'descripcion']
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)

    def get_queryset(self):
        modulo = self.request.query_params.get('modulo')
        if modulo:
            return ResAprendizaje.objects.filter(modulo=modulo)
        return ResAprendizaje.objects.all()
    
class RADetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = RADetailSerializer
    def get_queryset(self):
        return ResAprendizaje.objects.all()

class CEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = CEListSerializer
    ordering = 'codigo'
    ordering_fields = ['codigo', 'descripcion']
    search_fields = ['codigo', 
                    'descripcion',
                    "resultado_aprendizaje__codigo",
                    "resultado_aprendizaje__descripcion",
                    "modulo__codigo",
                    "modulo__nombre"
                    ]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        resultado_aprendizaje = self.request.query_params.get('resultado_aprendizaje')
        modulo = self.request.query_params.get('modulo')
        if modulo:
            return CritEvaluacion.objects.filter(resultado_aprendizaje__modulo=modulo) 
        if resultado_aprendizaje:
            return CritEvaluacion.objects.filter(resultado_aprendizaje=resultado_aprendizaje)
        return CritEvaluacion.objects.all()
    
class CEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = CEDetailSerializer
    def get_queryset(self):
        return CritEvaluacion.objects.all()
#UD10.3.a END