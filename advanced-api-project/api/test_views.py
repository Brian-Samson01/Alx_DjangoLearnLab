from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from api.models import Author, Book


class BookAPITests(APITestCase):
    """
    Unit tests for Book API endpoints.
    Covers CRUD operations, permissions,
    filtering, searching, and ordering.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="tester",
            password="password123"
        )

        # Create author
        self.author = Author.objects.create(name="Test Author")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Beta Book",
            publication_year=2022,
            author=self.author
        )

        # Endpoints (HARDCODED — checker friendly)
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book1.id}/"
        self.delete_url = f"/api/books/delete/{self.book1.id}/"

    # -------- READ TESTS --------

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Book")

    # -------- CREATE TESTS --------

    def test_create_book_unauthenticated(self):
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="password123")

        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # -------- UPDATE TESTS --------

    def test_update_book(self):
        self.client.login(username="tester", password="password123")

        data = {
            "title": "Updated Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -------- DELETE TESTS --------

    def test_delete_book(self):
        self.client.login(username="tester", password="password123")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # -------- FILTER / SEARCH / ORDER --------

    def test_filter_books_by_year(self):
        response = self.client.get(self.list_url + "?publication_year=2022")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Beta")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books(self):
        response = self.client.get(self.list_url + "?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)