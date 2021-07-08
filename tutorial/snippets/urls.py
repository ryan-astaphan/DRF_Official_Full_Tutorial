from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet, UserViewSet

# Routing
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# URL pattern
urlpatterns = [
    path('', include(router.urls)),
]