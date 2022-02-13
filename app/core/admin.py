from django.contrib import admin
from .models import Keyword, Publication, Study, StudyFile, Author


admin.site.register(Keyword)
admin.site.register(Publication)
admin.site.register(Study)
admin.site.register(StudyFile)
admin.site.register(Author)
