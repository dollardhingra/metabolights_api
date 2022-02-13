from core.models import (
    Keyword, Study, Publication, StudyFile
)
from rest_framework import viewsets, mixins

from .serializers import (
    KeywordSerializer,
    StudySerializer,
    StudyDetailSerializer,
    PublicationSerializer,
    StudyFileSerializer,
    StudyFileDetailSerializer
)


class KeywordViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """Manage Keywords in the DB"""

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class PublicationViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """Manage publication in the DB"""

    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class StudyViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """manage study in the DB"""

    queryset = Study.objects.all()
    serializer_class = StudySerializer

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "retrieve":
            return StudyDetailSerializer

        return self.serializer_class


class StudyFileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """manage studyfile in the DB"""

    queryset = StudyFile.objects.all()
    serializer_class = StudyFileSerializer

    def get_queryset(self):
        study = self.request.query_params.get("study")
        queryset = self.queryset
        if study:
            queryset = queryset.filter(study=study)

        return queryset

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "retrieve":
            return StudyFileDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """create a new keyword"""

        studyfile = self.get_object()
        size_kb = float(studyfile.file.size)/1024.0
        serializer.save(size_kb=size_kb)

    def perform_update(self, serializer):
        studyfile = self.get_object()

        size_kb = float(studyfile.file.size)/1024.0
        serializer.save(size_kb=size_kb)
