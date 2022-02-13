from django.shortcuts import render
from rest_framework import viewsets, mixins
from core.models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    """Manage Keywords in the DB"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        """create a new keyword"""
        serializer.save()







