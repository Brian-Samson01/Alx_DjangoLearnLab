from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer

"""
BookListView:
- Supports filtering, searching, and ordering.
- Public read-only access.
- Filtering fields: title, publication_year, author
- Search fields: title, author name
- Ordering fields: title, publication_year
"""

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, searching, and ordering configuration
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


"""
BookDetailView:
- Retrieve a single book.
- Public read-only access.
"""

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


"""
BookCreateView:
- Create a new book.
- Authenticated users only.
"""

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


"""
BookUpdateView:
- Update an existing book.
- Authenticated users only.
"""

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


"""
BookDeleteView:
- Delete a book.
- Authenticated users only.
"""

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]