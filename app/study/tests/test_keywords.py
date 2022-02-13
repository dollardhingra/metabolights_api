from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Keyword

from ..serializers import KeywordSerializer


KEYWORDS_URL = reverse('study:keyword-list')


class KeywordsApiTests(TestCase):
    """Test the APIs of Keyword model"""

    def setUp(self):
        self.client = APIClient()

    def test_list_keywords(self):
        """Test retrieving keywords"""
        Keyword.objects.create(title="keyword1")
        Keyword.objects.create(title="keyword2")

        res = self.client.get(KEYWORDS_URL)

        keywords = Keyword.objects.all()
        serializer = KeywordSerializer(keywords, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_keyword_create_successful(self):
        """Test that keyword is created successfully"""
        payload = {"title": "keyword_test"}
        self.client.post(KEYWORDS_URL, payload)
        exists = Keyword.objects.filter(
            title=payload['title']
        ).exists()
        self.assertTrue(exists)

    def test_create_keyword_invalid(self):
        """Test creating a new keyword with invalid payload"""
        payload = {'title': ''}
        res = self.client.post(KEYWORDS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

