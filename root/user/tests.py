from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User


class UsetTests(APITestCase):
    user_data = {
            "email": "user@gmail.com",
            "username": "user",
            "password": "user"
        }

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse("user:user-register")
        data = self.user_data
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


