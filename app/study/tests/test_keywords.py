from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Keyword

from ..serializers import KeywordSerializer

KEYWORD_URL = reverse('study:keyword-list')


def detail_url(keyword_id):
    """Return keyword detail URL"""
    return reverse('study:keyword-detail', args=[keyword_id])


def sample_keyword(title):
    """create and return a sample keyword"""
    return Keyword.objects.create(title=title)


class KeywordApiTests(TestCase):
    """Test the APIs of Keyword model"""

    def setUp(self):
        self.client = APIClient()

    def test_list_keywords(self):
        """Test retrieving keywords"""
        sample_keyword("keyword1")
        sample_keyword("keyword2")

        res = self.client.get(KEYWORD_URL)

        keywords = Keyword.objects.all()
        serializer = KeywordSerializer(keywords, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_keyword_successful(self):
        """Test that keyword is created successfully"""
        payload = {"title": "new keyword"}
        self.client.post(KEYWORD_URL, payload)
        exists = Keyword.objects.filter(
            title=payload['title']
        ).exists()
        self.assertTrue(exists)

    def test_create_keyword_invalid(self):
        """Test creating a new keyword with invalid payload"""
        payload = {'title': ''}
        res = self.client.post(KEYWORD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_keyword_successful(self):
        """Test updating a keyword"""
        keyword = sample_keyword("old keyword")
        payload = {"title": "new keyword"}

        self.client.put(detail_url(str(keyword.id)), payload)
        keyword.refresh_from_db()
        exists = Keyword.objects.filter(
            title=payload['title']
        ).exists()

        self.assertTrue(exists)

    def test_update_keyword_invalid(self):
        """Test updating keyword with invalid details"""
        keyword = sample_keyword("old keyword")
        res = self.client.put(detail_url(str(keyword.id)), {})
        keyword.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_keyword_successful(self):
        """Test partial updating an keyword"""
        keyword = sample_keyword("old keyword")
        payload = {"title": "new keyword"}

        self.client.patch(detail_url(str(keyword.id)), payload)
        keyword.refresh_from_db()
        exists = Keyword.objects.filter(
            title=payload['title']
        ).exists()

        self.assertTrue(exists)

    def test_delete_keyword_successful(self):
        keyword = sample_keyword("existing keyword")
        self.client.delete(detail_url(str(keyword.id)))

        exists = Keyword.objects.filter(
            title="existing keyword"
        ).exists()

        self.assertFalse(exists)
