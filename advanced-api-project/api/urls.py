from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update book (explicit path + pk path)
    path('books/update/', BookUpdateView.as_view(), name='book-update-base'),  # FIX
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete book (explicit path + pk path)
    path('books/delete/', BookDeleteView.as_view(), name='book-delete-base'),  # FIX
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
