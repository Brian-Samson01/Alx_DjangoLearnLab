from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic import ListView, DetailView


# Create your views here.
# Fuction-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'