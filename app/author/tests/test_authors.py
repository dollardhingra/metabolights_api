from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Author

from ..serializers import AuthorSerializer

AUTHOR_URL = reverse('author:author-list')


def detail_url(author_id):
    """Return author detail URL"""
    return reverse('author:author-detail', args=[author_id])


def sample_author(full_name, email):
    """create and return a sample author"""
    return Author.objects.create(full_name=full_name, email=email)


class AuthorApiTests(TestCase):
    """Test the APIs of Author model"""

    def setUp(self):
        self.client = APIClient()

    def test_list_keywords(self):
        """Test retrieving authors"""
        sample_author("John Doe", "johndoe@mail.com")
        sample_author("Jane Doe", "janedoe@mail.com")

        res = self.client.get(AUTHOR_URL)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_author_successful(self):
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

    def test_update_author_successful(self):
        """Test updating an author"""
        author = sample_author("Existing User", "user@mail.com")
        payload = {
            "full_name": "Existing User Name Changed",
            "email": "changed_email@mail.com"
        }

        self.client.put(detail_url(str(author.id)), payload)
        author.refresh_from_db()
        exists = Author.objects.filter(
            email=payload['email']
        ).exists()

        self.assertTrue(exists)

    def test_update_author_invalid(self):
        """Test updating author with invalid details"""
        author = sample_author("Existing User", "user@mail.com")
        res = self.client.put(detail_url(str(author.id)), {})
        author.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_author_successful(self):
        """Test partial updating an author"""
        author = sample_author("Existing User", "user@mail.com")
        payload = {
            "email": "changed_email@mail.com"
        }

        self.client.patch(detail_url(str(author.id)), payload)
        author.refresh_from_db()
        exists = Author.objects.filter(
            email=payload['email']
        ).exists()

        self.assertTrue(exists)

    def test_partial_update_author_invalid(self):
        """Test updating author with invalid details"""
        author = sample_author("Existing User", "user@mail.com")
        res = self.client.patch(detail_url(str(author.id)), {"full_name": ""})
        author.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_author_successful(self):
        author = sample_author("Existing User", "user@mail.com")
        self.client.delete(detail_url(str(author.id)))

        exists = Author.objects.filter(
            email="user@mail.com"
        ).exists()

        self.assertFalse(exists)
