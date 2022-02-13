import tempfile
import os
from unittest.mock import patch

from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Study

from .test_keywords import sample_keyword
from ..serializers import StudySerializer
from author.tests.test_authors import sample_author

from core.models import get_studyfile_path

STUDY_URL = reverse('study:study-list')


def detail_url(study_id):
    """Return study detail URL"""
    return reverse('study:study-detail', args=[study_id])


STUDYFILE_URL = reverse('study:studyfile-list')


def sample_study(title, abstract):
    """create and return a sample study"""
    author = sample_author("John Adam", "johnadam@mail.com")
    study = Study.objects.create(
        title=title,
        abstract=abstract,
        author=author
    )
    study.keywords.add(sample_keyword("keyword1"))
    return study


class StudyApiTests(TestCase):
    """Test the APIs of Study model"""

    def setUp(self):
        self.client = APIClient()

    def test_list_studies(self):
        """Test retrieving studies"""
        sample_study("Biology Study", "this is an abstract")

        res = self.client.get(STUDY_URL)

        studies = Study.objects.all()
        serializer = StudySerializer(studies, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_study_empty_publication_successful(self):
        """Test that study is created successfully"""

        keyword1 = sample_keyword("keyword1")
        payload = {
            "title": "Biology Study",
            "abstract": "this is an abstract",
            "keywords": [keyword1.pk],
            "author": sample_author("John Doe", "johndoe@mail.com").pk
        }
        self.client.post(STUDY_URL, payload)
        exists = Study.objects.filter(
            title=payload['title']
        ).exists()
        self.assertTrue(exists)

    def test_create_study_invalid(self):
        """Test creating a new study with invalid payload"""
        payload = {
            "title": "Biology Study",
            "abstract": "this is an abstract",
            "keywords": [],
            "author": None
        }  # keywords and author are required

        res = self.client.post(STUDY_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_study_successful(self):
        """Test updating an study"""
        study = sample_study("Biology Study", "this is an abstract")
        payload = {
            "title": "Change study name",
            "abstract": "changed abstract",
            "author": sample_author("new author", "author@mail.com").pk,
            "keywords": [
                sample_keyword("new keyword").pk,
                sample_keyword("new keyword2").pk
            ]
        }

        self.client.put(detail_url(str(study.id)), payload)
        study.refresh_from_db()
        exists = Study.objects.filter(
            title=payload['title']
        ).exists()

        self.assertTrue(exists)

    def test_update_study_invalid(self):
        """Test updating study with invalid details"""
        study = sample_study("Biology Study", "this is an abstract")
        res = self.client.put(detail_url(str(study.id)),
                              {"title": "Change study name"}
                              )
        study.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_study_successful(self):
        """Test partial updating an study"""
        study = sample_study("Existing User", "user@mail.com")
        payload = {
            "title": "Change study name"
        }

        self.client.patch(detail_url(str(study.id)), payload)
        study.refresh_from_db()
        exists = Study.objects.filter(
            title=payload['title']
        ).exists()

        self.assertTrue(exists)

    def test_delete_study_successful(self):
        study = sample_study("Deleted Title", "some abstract")
        self.client.delete(detail_url(str(study.id)))

        exists = Study.objects.filter(
            title="Deleted Title"
        ).exists()

        self.assertFalse(exists)

    @patch('uuid.uuid4')
    def test_rstudyfile_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = get_studyfile_path(None, 'file.csv')

        exp_path = f'uploads/studyfiles/{uuid}.csv'
        self.assertEqual(file_path, exp_path)
