# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # REQUIRED LINE
from .models import Book
from .serializers import BookSerializer



# ============================
#   LIST ALL BOOKS
#   (Anyone can view)
# ============================
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access


# ============================
#   RETRIEVE ONE BOOK BY ID
#   (Anyone can view)
# ============================
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access


# ============================
#   CREATE A NEW BOOK
#   (Authenticated users only)
# ============================
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom behavior:
    # Validate incoming data and return clean error messages
    def perform_create(self, serializer):
        serializer.save()


# ============================
#   UPDATE AN EXISTING BOOK
#   (Authenticated users only)
# ============================
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom update logic / hooks
    def perform_update(self, serializer):
        serializer.save()


# ============================
#   DELETE A BOOK
#   (Authenticated users only)
# ============================
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
