from urllib import response
from django import views
from rest_framework import mixins, viewsets, filters, status
from rest_framework.exceptions import ValidationError
from portfolioapp.api.serializers import CategoriaSerializer, ProyectoDetailSerializer
from portfolioapp.models import Categoria, Proyecto
from portfolioapp.api.pagination import LargeResultsSetPagination, StandardResultsSetPagination, ShortResultsSetPagination

class CategoriaListViewSet(mixins.ListModelMixin, 
                        viewsets.GenericViewSet):
    model = Categoria
    serializer_class = CategoriaSerializer
    pagination_class = ShortResultsSetPagination

    def get_queryset(self):
        return Categoria.objects.all()
    
class CategoriaCRUDViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class CategoriaCreateRetriveUpdateViewSet(mixins.CreateModelMixin,
                                        mixins.RetrieveModelMixin,
                                        mixins.UpdateModelMixin,
                                        viewsets.GenericViewSet):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.all()

class ProyectoListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProyectoDetailSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering = 'fecha_creacion'
    ordering_fields = ['fecha_creacion', 'titulo']
    search_fields = ['titulo', 'descripcion', 'categorias__nombre']

    def get_queryset(self):
        year_from = self.request.query_params.get('year_from')
        if year_from:
            return Proyecto.objects.filter(year_gte=year_from)
        return Proyecto.objects.all()

class ProyectoCRUDViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = ProyectoDetailSerializer
    queryset = Proyecto.objects.all()

    def validate_update_create(self, serializer):
        year = serializer.validated_data.get('year')
        fecha_cracion = serializer.validated_data.get('fecha_creacion')

        if year != fecha_cracion.year:
            raise ValidationError(
                {'non_field_errors': "El año ha de coincidir con el dela fecha de creación"}
            )
        
    def perform_create(self, serializer):
        self.validate_update_create(serializer)
        serializer.save()

    def perform_update(self, serializer):
        self.validate_update_create(serializer)
        serializer.save()
    
class CapitalizeCategoriaView(views.APIView):
    def get(self, request, format=None):
        categorias = Categoria.objects.all()
        for categoria in categorias:
            categoria.nombre = categoria.nombre.capitalize()
            categoria.save()
        return response.Response(status=status.HTTP_200_OK)