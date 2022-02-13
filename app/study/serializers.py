from rest_framework import serializers

from core.models import Keyword, Study


class KeywordSerializer(serializers.ModelSerializer):
    """
    Serializer for Keyword model
    """
    class Meta:
        model = Keyword
        fields = ('id', 'title')
        read_only_fields = ('id',)


class StudySerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """
    # keywords = KeywordSerializer(many=True)
    # publications = serializers.StringRelatedField(many=True)
    # author = AuthorSerializer()

    class Meta:
        model = Study
        fields = ('title', 'abstract', 'publications', 'keywords', 'author')
        read_only_fields = ('id',)

