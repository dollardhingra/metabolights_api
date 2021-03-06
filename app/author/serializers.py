from rest_framework import serializers

from core.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'email')
