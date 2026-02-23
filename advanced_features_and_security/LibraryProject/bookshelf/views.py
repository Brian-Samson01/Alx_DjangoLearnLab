from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
# Create your views here.

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
Permissions and Groups Setup:

Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Permissions are defined in Book model Meta class
and enforced using @permission_required decorators.
"""