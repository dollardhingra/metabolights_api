from django.db import models


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
    file = models.FileField()
    study = models.ForeignKey(Study, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"



