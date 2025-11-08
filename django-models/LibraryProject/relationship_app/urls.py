# ---------------------- relationship_app/urls.py ----------------------

from django.urls import path
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Function-based and class-based views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication routes using Django’s built-in views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
]


# ---------------------- project/urls.py ----------------------

from django.urls import path, include

urlpatterns = [
    # ... other urls
    path('relationship/', include(('relationship_app.urls', 'relationship_app'), namespace='relationship_app')),
]
