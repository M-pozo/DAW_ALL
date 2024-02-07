from django import views
from rest_framework import mixins, viewsets, filters, views, status, response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from programacion_aula.api.serializers import *
from programacion_aula.models import *
from common.api.pagination import LargeResultsSetPagination, StandardResultsSetPagination, ShortResultsSetPagination
from programacion_aula.api.utils import *
from collections import defaultdict


#UD10.3.a BEGIN
class AlumnoListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Lista todos los Alumno por su id y una descripción 
    """
    serializer_class = AlumnoListSerializer
    ordering = ['apellido', 'nombre']
    ordering_fields = ['apellido',
                       'nombre',
                       'ciudad',
                       'codigo_postal'
                       ]
    
    search_fields = ['nombre', 
                    'apellido',
                    "direccion",
                    "codigo_postal",
                    "ciudad",
                    ]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        return Alumno.objects.all()
    
class AlumnoDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """
    Poder Actualizar, Crear y Eliminar cualquier alumno, ademas cada vez que creas un alumno nuevo crea todas la Calificaciones UDCE
    """
    serializer_class = AlumnoDetailSerializer
    def get_queryset(self):
        return Alumno.objects.all()
    #UD10.3.c
    def perform_create(self, serializer):
        instance = serializer.save()
        criterios_evaluacion = CriterioEvalUD.objects.all()
        for criterio in criterios_evaluacion:
            CalificacionUDCE.objects.create(
                alumno=instance,
                unidad=criterio.unidad,
                crit_evaluacion=criterio.criterio_evaluacion,
                calificacion=1
            )
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

class CEUDListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Lista todos los CEUD por su id y una descripción 
    """
    serializer_class = CEUDListSerializer
    ordering = ['criterio_evaluacion__resultado_aprendizaje__modulo__nombre',
                'criterio_evaluacion__resultado_aprendizaje__codigo',
                'criterio_evaluacion__codigo',
                 'unidad__nombre' ]
    ordering_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo__nombre',
                    'criterio_evaluacion__resultado_aprendizaje__codigo',
                    'criterio_evaluacion__codigo',
                    'unidad__nombre',
                    'criterio_evaluacion__descripcion']
    
    search_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo__nombre', 
                    'criterio_evaluacion__resultado_aprendizaje__codigo',
                    "criterio_evaluacion__resultado_aprendizaje__descripcion",
                    "criterio_evaluacion__codigo",
                    "criterio_evaluacion__descripcion",
                    'unidad__nombre'
                    ]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        resultado_aprendizaje = self.request.query_params.get('resultado_aprendizaje')
        modulo = self.request.query_params.get('modulo')
        criterio_evaluacion = self.request.query_params.get('criterio_evaluacion')
        unidad = self.request.query_params.get('unidad')
        if modulo:
            return CriterioEvalUD.objects.filter(criterio_evaluacion__resultado_aprendizaje__modulo=modulo) 
        if resultado_aprendizaje:
            return CriterioEvalUD.objects.filter(criterio_evaluacion__resultado_aprendizaje=resultado_aprendizaje)
        if criterio_evaluacion:
            return CriterioEvalUD.objects.filter(criterio_evaluacion=criterio_evaluacion) 
        if unidad:
            return CriterioEvalUD.objects.filter(unidad=unidad)
        return CriterioEvalUD.objects.all()
    
class CEUDDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """
    Poder Actualizar, Crear y Eliminar cualquier CEUD
    """
    serializer_class = CEUDDetailSerializer
    def get_queryset(self):
        return CriterioEvalUD.objects.all()

class CalUDCEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Lista todas las Calificaciones por UD y CE por su id y una descripción 
    """
    serializer_class = CalUDCEListSerializer
    ordering = ['unidad__nombre',
                'crit_evaluacion__resultado_aprendizaje__modulo__nombre',
                'crit_evaluacion__resultado_aprendizaje__codigo',
                'crit_evaluacion__codigo',
                'alumno__apellido',
                'alumno__nombre']
    ordering_fields = ['unidad__nombre',
                'crit_evaluacion__resultado_aprendizaje__modulo__nombre',
                'crit_evaluacion__resultado_aprendizaje__codigo',
                'crit_evaluacion__codigo',
                'alumno__apellido',
                'alumno__nombre']
    search_fields = ['crit_evaluacion__resultado_aprendizaje__modulo__nombre', 
                    'crit_evaluacion__resultado_aprendizaje__codigo',
                    "resultado_aprendizaje__descripcion",
                    "crit_evaluacion__codigo",
                    "crit_evaluacion__descripcion",
                    "alumno__nombre",
                    'alumno__apellido'
                    ]
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        resultado_aprendizaje = self.request.query_params.get('resultado_aprendizaje')
        modulo = self.request.query_params.get('modulo')
        alumno = self.request.query_params.get('alumno')
        crit_evaluacion = self.request.query_params.get('crit_evaluacion')
        unidad = self.request.query_params.get('unidad')

        if modulo:
            return CalificacionUDCE.objects.filter(crit_evaluacion__resultado_aprendizaje__modulo=modulo) 
        if resultado_aprendizaje:
            return CalificacionUDCE.objects.filter(crit_evaluacion__resultado_aprendizaje=resultado_aprendizaje)
        if alumno:
            return CalificacionUDCE.objects.filter(alumno=alumno) 
        if crit_evaluacion:
            return CalificacionUDCE.objects.filter(crit_evaluacion=crit_evaluacion)
        if unidad:
            return CalificacionUDCE.objects.filter(unidad=unidad) 
        return CalificacionUDCE.objects.all()
    
class CalUDCEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """
    Poder Actualizar, Crear y Eliminar cualquier Calificación por UDCE
    """
    serializer_class = CalUDCEDetailSerializer
    def get_queryset(self):
        return CalificacionUDCE.objects.all()

class CalCEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Lista todas las Calificaciones por CE por su id y una descripción 
    """
    serializer_class = CalCEListSerializer
    ordering = ['crit_evaluacion__resultado_aprendizaje__modulo__nombre',
                'crit_evaluacion__resultado_aprendizaje__codigo',
                'crit_evaluacion__codigo',
                'alumno__apellido',
                'alumno__nombre']
    
    ordering_fields = ['crit_evaluacion__resultado_aprendizaje__modulo__nombre',
                'crit_evaluacion__resultado_aprendizaje__codigo',
                'crit_evaluacion__codigo',
                'alumno__apellido',
                'alumno__nombre']
    
    search_fields = ['crit_evaluacion__resultado_aprendizaje__modulo__nombre', 
                    'crit_evaluacion__resultado_aprendizaje__codigo',
                    "crit_evaluacion__codigo",
                    "resultado_aprendizaje__descripcion",
                    "alumno__nombre",
                    "alumno__apellido"
                    ]
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        resultado_aprendizaje = self.request.query_params.get('resultado_aprendizaje')
        modulo = self.request.query_params.get('modulo')
        alumno = self.request.query_params.get('alumno')
        crit_evaluacion = self.request.query_params.get('crit_evaluacion')
        unidad = self.request.query_params.get('unidad')

        if modulo:
            return CalificacionCE.objects.filter(crit_evaluacion__resultado_aprendizaje__modulo=modulo) 
        if resultado_aprendizaje:
            return CalificacionCE.objects.filter(crit_evaluacion__resultado_aprendizaje=resultado_aprendizaje)
        if alumno:
            return CalificacionCE.objects.filter(alumno=alumno) 
        if crit_evaluacion:
            return CalificacionCE.objects.filter(crit_evaluacion=crit_evaluacion)
        return CalificacionCE.objects.all()
    
class CalCEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """
    Poder Actualizar, Crear y Eliminar cualquier Calificación por CE
    """
    serializer_class = CalCEDetailSerializer
    def get_queryset(self):
        return CalificacionCE.objects.all()

class CalRAListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Lista todas las Calificaciones por RA por su id y una descripción 
    """
    serializer_class = CalRAListSerializer
    ordering = ['res_aprendizaje__modulo__nombre',
                'res_aprendizaje__codigo',
                'alumno__apellido',
                'alumno__nombre',
                ]
    ordering_fields = ['res_aprendizaje__modulo__nombre'
                'res_aprendizaje__codigo',
                'alumno__apellido',
                'alumno__nombre',
                ]
    search_fields = ['res_aprendizaje__modulo__nombre'
                'res_aprendizaje__codigo',
                'res_aprendizaje__descripcion',
                'alumno__apellido',
                ]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        res_aprendizaje = self.request.query_params.get('res_aprendizaje')
        modulo = self.request.query_params.get('modulo')
        alumno = self.request.query_params.get('alumno')

        if modulo:
            return CalificacionRA.objects.filter(res_aprendizaje__modulo=modulo) 
        if res_aprendizaje:
            return CalificacionRA.objects.filter(res_aprendizaje=res_aprendizaje)
        if alumno:
            return CalificacionRA.objects.filter(alumno=alumno) 
        return CalificacionRA.objects.all()
    
class CalRADetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """
    Poder Actualizar, Crear y Eliminar cualquier Calificación por RA
    """
    serializer_class = CalRADetailSerializer
    def get_queryset(self):
        return CalificacionRA.objects.all()



class CalTotalListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Lista todas las Calificaciones Totales por su id y una descripción 
    """
    serializer_class = CalTotalListSerializer
    ordering = ['modulo__nombre',
                'alumno__apellido',
                'alumno__nombre']
    ordering_fields = ['modulo__nombre',
                'alumno__apellido',
                'alumno__nombre']
    search_fields = ['modulo__nombre',
                'alumno__apellido',
                ]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    
    def get_queryset(self):
        alumno = self.request.query_params.get('alumno')
        modulo = self.request.query_params.get('modulo')
        if modulo:
            return CalificacionTotal.objects.filter(modulo=modulo) 
        if alumno:
            return CalificacionTotal.objects.filter(alumno=alumno)
        return CalificacionTotal.objects.all()
    
class CalTotalDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """
    Poder Actualizar, Crear y Eliminar cualquier Calificación Total
    """
    serializer_class = CalTotalDetailSerializer
    def get_queryset(self):
        return CalificacionTotal.objects.all()
#UD10.3.d BEGIN    

class CalcularNotasView(views.APIView):
    """
    Calcula la nota final de cada alumno dependiendo de lo que le pases
    """
    def get(self, request):
        alumno_id = request.query_params.get('alumno__id')
        modulo_id = request.query_params.get('modulo__id')
        try:
            if alumno_id is not None:
                alumno = Alumno.objects.get(id=alumno_id)
                if modulo_id is not None:
                    CalcularNota(alumno.id, modulo_id)
                else:
                    for modulo in alumno.modulos.all():
                        CalcularNota(alumno.id, modulo.id)
            else:
                if modulo_id is not None:
                    for alumno in Alumno.objects.all():
                        CalcularNota(alumno.id, modulo_id)
                else:
                    for alumno in Alumno.objects.all():
                        for modulo in alumno.modulos.all():
                            CalcularNota(alumno.id, modulo.id)
            return response.Response(status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


#UD10.3.d END
#UD10.3.a END