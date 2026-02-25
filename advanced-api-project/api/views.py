from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
BookListView:
- Handles GET requests.
- Allows anyone (authenticated or not) to view all books.
"""

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
BookDetailView:
- Handles GET requests for a single book by ID.
- Publicly accessible.
"""

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
BookCreateView:
- Handles POST requests to create a new book.
- Restricted to authenticated users only.
- Automatically triggers serializer validation.
"""

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
BookUpdateView:
- Handles PUT/PATCH requests to update an existing book.
- Restricted to authenticated users.
"""

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
BookDeleteView:
- Handles DELETE requests.
- Restricted to authenticated users.
"""

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]