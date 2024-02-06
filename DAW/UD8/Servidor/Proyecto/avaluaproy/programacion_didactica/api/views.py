from django import views
from rest_framework import mixins, viewsets, filters, views, status, response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from programacion_didactica.api.serializers import *
from programacion_didactica.models import *
from common.api.pagination import LargeResultsSetPagination, StandardResultsSetPagination, ShortResultsSetPagination


#UD10.3.a BEGIN
class UnidadListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = UnidadListSerializer
    ordering = 'nombre'
    search_fields = ['nombre']
    
    def get_queryset(self):
        return Unidad.objects.all()
    
class UnidadDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = UnidadDetailSerializer
    def get_queryset(self):
        return Unidad.objects.all()

class IEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = IEListSerializer
    ordering = 'codigo'
    ordering_fields = ['codigo', 'nombre']
    search_fields = ['codigo', 
                    'nombre',
                    "descripcion"
                    ]
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        return InstEvaluacion.objects.all()
    
class IEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = IEDetailSerializer
    def get_queryset(self):
        return InstEvaluacion.objects.all()

class PondRAListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = PondRAListSerializer
    ordering = ['resultado_aprendizaje__modulo__nombre',
                'resultado_aprendizaje__codigo']
    
    ordering_fields = ['resultado_aprendizaje__modulo__nombre',
                       'resultado_aprendizaje__codigo',
                       "resultado_aprendizaje__nombre"]
    
    search_fields = ['resultado_aprendizaje__modulo__nombre', 
                    'resultado_aprendizaje__codigo',
                    "resultado_aprendizaje__nombre",
                    ]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        modulo = self.request.query_params.get('modulo')
        if modulo:
            return PondRA.objects.filter(resultado_aprendizaje__modulo=modulo) 
        return PondRA.objects.all()
    
class PondRADetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PondRADetailSerializer
    def get_queryset(self):
        return PondRA.objects.all()

class PondCEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = PondCEListSerializer
    ordering = ['criterio_evaluacion__resultado_aprendizaje__modulo__nombre',
                'criterio_evaluacion__resultado_aprendizaje__codigo',
                'criterio_evaluacion__codigo']
    
    ordering_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo__nombre',
                       'criterio_evaluacion__resultado_aprendizaje__codigo',
                       'criterio_evaluacion__codigo',
                       'criterio_evaluacion__nombre']
    search_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo__nombre',
                     'criterio_evaluacion__resultado_aprendizaje__codigo',
                     'criterio_evaluacion__codigo',
                     'criterio_evaluacion__nombre']
    
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        resultado_aprendizaje = self.request.query_params.get('resultado_aprendizaje')
        modulo = self.request.query_params.get('modulo')
        if modulo:
            return PondCriterio.objects.filter(criterio_evaluacion__resultado_aprendizaje__modulo=modulo) 
        if resultado_aprendizaje:
            return PondCriterio.objects.filter(criterio_evaluacion__resultado_aprendizaje=resultado_aprendizaje)
        return PondCriterio.objects.all()
    
class PondCEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PondCEDetailSerializer
    def get_queryset(self):
        return PondCriterio.objects.all()

class PondCEUDListViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = PondCEUDListSerializer
    ordering = ['unidad__nombre',
                'criterio_evaluacion__resultado_aprendizaje__modulo__nombre',
                'criterio_evaluacion__resultado_aprendizaje__codigo',
                'criterio_evaluacion__codigo']
    
    ordering_fields = ['unidad__nombre',
                       'criterio_evaluacion__resultado_aprendizaje__modulo__nombre'
                       'criterio_evaluacion__resultado_aprendizaje__codigo',
                       'criterio_evaluacion__codigo',
                       'criterio_evaluacion__nombre']
    
    search_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo__nombre', 
                    'criterio_evaluacion__resultado_aprendizaje__codigo',
                    "criterio_evaluacion__resultado_aprendizaje__nombre",
                    "criterio_evaluacion__codigo",
                    "criterio_evaluacion__nombre",
                    "unidad__nombre"
                    ]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        resultado_aprendizaje = self.request.query_params.get('resultado_aprendizaje')
        modulo = self.request.query_params.get('modulo')
        criterio_evaluacion = self.request.query_params.get('criterio_evaluacion')
        unidad = self.request.query_params.get('unidad')
        if modulo:
            return PondCritUD.objects.filter(resultado_aprendizaje__modulo=modulo) 
        if resultado_aprendizaje:
            return PondCritUD.objects.filter(resultado_aprendizaje=resultado_aprendizaje)
        if criterio_evaluacion:
            return PondCritUD.objects.filter(criterio_evaluacion=criterio_evaluacion) 
        if unidad:
            return PondCritUD.objects.filter(unidad=unidad)
        return PondCritUD.objects.all()
    
class PondCEUDDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PondCEUDDetailSerializer
    def get_queryset(self):
        return PondCritUD.objects.all()
#UD10.3.a END