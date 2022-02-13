from rest_framework import serializers

from core.models import Keyword, Study, Publication, StudyFile
from author.serializers import AuthorSerializer


class KeywordSerializer(serializers.ModelSerializer):
    """
    Serializer for Keyword model
    """

    class Meta:
        model = Keyword
        fields = ("id", "title")
        read_only_fields = ("id",)


class PublicationSerializer(serializers.ModelSerializer):
    """
    Serialize your Publication model
    """

    class Meta:
        model = Publication
        read_only_fields = ("id",)
        fields = (
            "id",
            "title",
            "description",
        )


class StudySerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """

    class Meta:
        model = Study
        fields = ("id", "title", "abstract", "publications", "keywords", "author")
        read_only_fields = ("id",)


class StudyDetailSerializer(StudySerializer):
    """
    Serialize study detail
    """

    keywords = KeywordSerializer(many=True, read_only=True)
    publications = PublicationSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)


class StudyFileSerializer(serializers.ModelSerializer):
    """
    Serializer for StudyFile model
    """

    class Meta:
        model = StudyFile
        fields = ('id', 'title', 'file', 'study', 'size_kb')
        read_only_fields = ("id", "size_kb")


class StudyFileDetailSerializer(StudyFileSerializer):
    """
    Serialize study detail
    """

    study = StudyDetailSerializer(read_only=True)
