from rest_framework import serializers

from core.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'email')


# class AuthorDetailSerializer(AuthorSerializer):
#     """Serialize a recipe detail"""
#     ingredients = IngredientSerializer(many=True, read_only=True)
#     tags = TagSerializer(many=True, read_only=True)