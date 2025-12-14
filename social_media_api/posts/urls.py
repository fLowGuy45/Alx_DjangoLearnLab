from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

from django.urls import path
from . import views



router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
path('feed/', views.feed, name='user-feed'),
    path('', include(router.urls)),
]
