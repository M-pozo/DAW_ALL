

from rest_framework import mixins, viewsets
from portfolioapp.api.serializers import CategoriaSerializer
from portfolioapp.models import Categoria

class CategoriaListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategoriaSerializer
    #pagination_class = ShortResultsSetPagination

    def get_queryset(self):
        return Categoria.objects.all()