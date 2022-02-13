from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('keywords', views.KeywordViewSet)
router.register('publications', views.PublicationViewSet)
router.register('studyfile', views.StudyFileViewSet)
router.register('', views.StudyViewSet)


app_name = 'study'

urlpatterns = [
    path('', include(router.urls))
]


