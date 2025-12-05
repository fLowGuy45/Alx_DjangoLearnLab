# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthTests(TestCase):
    def test_register_login_logout_flow(self):
        # Register
        resp = self.client.post(reverse('blog:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'ComplexPass!123',
            'password2': 'ComplexPass!123'
        })
        self.assertEqual(resp.status_code, 302)  # redirected after register

        # Login
        resp = self.client.post(reverse('blog:login'), {
            'username': 'testuser',
            'password': 'ComplexPass!123'
        })
        self.assertEqual(resp.status_code, 302)  # login redirects

        # Profile access
        self.client.login(username='testuser', password='ComplexPass!123')
        resp = self.client.get(reverse('blog:profile'))
        self.assertEqual(resp.status_code, 200)
