from core.models import Keyword
from rest_framework import viewsets, mixins

from .serializers import KeywordSerializer


class KeywordViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    """Manage Keywords in the DB"""

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

    def perform_create(self, serializer):
        """create a new keyword"""
        serializer.save()
