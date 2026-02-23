from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import BookSearchForm
# Create your views here.
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    return HttpResponse("List of books")


@permission_required("bookshelf.can_view", raise_exception=True)
def view_books(request):
    return HttpResponse("You can view books")


@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    return HttpResponse("You can create a book")


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request):
    return HttpResponse("You can edit a book")


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request):
    return HttpResponse("You can delete a book")



"""
Security Note:
All database queries use Django ORM to prevent SQL injection.
User input is validated using Django Forms.
"""

def secure_book_search(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        title = form.cleaned_data["title"]
        books = Book.objects.filter(title__icontains=title)

    return render(request, "bookshelf/book_list.html", {
        "form": form,
        "books": books
    })

def add_csp_header(response):
    response["Content-Security-Policy"] = "default-src 'self'"
    return response

def book_list(request):
    response = render(request, "bookshelf/book_list.html")
    response["Content-Security-Policy"] = "default-src 'self'"
    return response

"""
Security Best Practices Implemented:

- DEBUG set to False for production safety
- XSS protection via SECURE_BROWSER_XSS_FILTER
- Clickjacking protection using X_FRAME_OPTIONS
- CSRF protection via CSRF tokens in forms
- Secure cookies enforced with HTTPS
- SQL Injection prevented using Django ORM
- Content Security Policy applied to responses
"""



"""
Permissions and Groups Setup:

Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Permissions are defined in Book model Meta class
and enforced using @permission_required decorators.
"""