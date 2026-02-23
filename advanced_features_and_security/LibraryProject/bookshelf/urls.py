from django.urls import path
from . import views

urlpatterns = [
    path("books/view/", views.view_books, name="view_books"),
    path("books/create/", views.create_book, name="create_book"),
    path("books/edit/", views.edit_book, name="edit_book"),
    path("books/delete/", views.delete_book, name="delete_book"),
]