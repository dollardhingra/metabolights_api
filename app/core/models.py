from django.db import models
import uuid
import os

from study.validators import FileValidator


def get_studyfile_path(instance, filename):
    """Generate file path for new study file"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/studyfiles/', filename)


class Keyword(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"


class Study(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.ManyToManyField(Keyword)
    publications = models.ManyToManyField(Publication, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {str(self.author)}"


class StudyFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_studyfile_path, validators=[FileValidator()])
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    size_kb = models.FloatField()

    def __str__(self):
        return f"{self.title}"




