from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # <--- This imports views from the current app
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

app_name = 'blog'

urlpatterns = [
    # User auth URLs
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),

    # Blog CRUD URLs (singular 'post')
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('', views.PostListView.as_view(), name='post-list'),  # optional: home page lists posts

    # Comment URLs
path('post/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

]
