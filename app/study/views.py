from core.models import Keyword, Study
from rest_framework import viewsets, mixins

from .serializers import KeywordSerializer, StudySerializer


class KeywordViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    """Manage Keywords in the DB"""

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class StudyViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    """manage study in the DB"""

    queryset = Study.objects.all()
    serializer_class = StudySerializer