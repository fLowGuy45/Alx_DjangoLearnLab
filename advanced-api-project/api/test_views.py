from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(
            username='user1',
            password='testpass123'
        )

        self.admin = User.objects.create_superuser(
            username='admin',
            password='adminpass123'
        )

        # Authenticate regular user by default
        self.client = APIClient()
        self.client.login(username='user1', password='testpass123')

        # Endpoints
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])

        # Sample book
        self.book = Book.objects.create(
            title="Python Basics",
            author="John Doe",
            publication_year=2020
        )

    # -------------------------------
    # CRUD TESTS
    # -------------------------------

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Author 1",
            "publication_year": 2022
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data["title"], "New Book")

    def test_get_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "author": "John Doe",
            "publication_year": 2021
        }

        response = self.client.put(self.detail_url(self.book.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # -------------------------------
    # FILTER, SEARCH, ORDERING TESTS
    # -------------------------------

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_by_publication_year(self):
        response = self.client.get(self.list_url, {"publication_year": 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["publication_year"], 2020)

    def test_ordering_books(self):
        Book.objects.create(
            title="A Book",
            author="Tester",
            publication_year=2010
        )
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]["title"] == "A Book")

    # -------------------------------
    # PERMISSIONS TESTS
    # -------------------------------

    def test_unauthenticated_user_cannot_create_book(self):
        client = APIClient()
        response = client.post(self.list_url, {
            "title": "Blocked Book",
            "author": "Nobody",
            "publication_year": 2023
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_admin_can_delete(self):
        # Login admin
        self.client.logout()
        self.client.login(username='admin', password='adminpass123')

        response = self.client.delete(self.detail_url(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
