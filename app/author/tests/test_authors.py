from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Author

from ..serializers import AuthorSerializer

AUTHOR_URL = reverse('author:author-list')


class AuthorApiTests(TestCase):
    """Test the APIs of Author model"""

    def setUp(self):
        self.client = APIClient()

    def test_list_keywords(self):
        """Test retrieving authors"""
        Author.objects.create(full_name="John Doe", email="johndoe@mail.com")
        Author.objects.create(full_name="Jane Doe", email="janedoe@mail.com")

        res = self.client.get(AUTHOR_URL)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_authors_create_successful(self):
        """Test that author is created successfully"""
        payload = {"full_name": "James Bond", "email": "james@bond.com"}
        self.client.post(AUTHOR_URL, payload)
        exists = Author.objects.filter(
            email=payload['email']
        ).exists()
        self.assertTrue(exists)

    def test_create_author_invalid(self):
        """Test creating a new author with invalid payload"""
        payload = {'full_name': '', 'email': ''}
        res = self.client.post(AUTHOR_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

