from django.test import TestCase
from ..models import Keyword, Author


class ModelTests(TestCase):
    def test_keyword_str(self):
        """Test the tag string representation"""
        keyword = Keyword.objects.create(title="keyword1")

        self.assertEqual(str(keyword), keyword.title)

    def test_author_str(self):
        """Test the tag string representation"""
        author = Author.objects.create(full_name="Name Lastname", email="namelastname@gmail.com")

        self.assertEqual(str(author), f"{author.full_name} ({author.email})")