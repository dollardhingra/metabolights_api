from rest_framework import serializers

from core.models import Keyword


class KeywordSerializer(serializers.ModelSerializer):
    """
    Serializer for Keyword model
    """
    class Meta:
        model = Keyword
        fields = ('id', 'title')
        read_only_fields = ('id',)
