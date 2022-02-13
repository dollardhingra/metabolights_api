from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('keywords', views.KeywordViewSet)

app_name = 'study'

urlpatterns = [
    path('', include(router.urls))
]

