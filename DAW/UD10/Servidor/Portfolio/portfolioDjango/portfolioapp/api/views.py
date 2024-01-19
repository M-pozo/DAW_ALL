

from rest_framework import mixins, viewsets
from portfolioapp.api.serializers import CategoriaSerializer, ProyectoDetailSerializer
from portfolioapp.models import Categoria, Proyecto

class CategoriaListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategoriaSerializer
    #pagination_class = ShortResultsSetPagination

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
    queryset = Proyecto.objects.all()

class ProyectoCRUDViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = ProyectoDetailSerializer
    queryset = Proyecto.objects.all()