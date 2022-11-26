from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    data = {"email": 'axperojan@gmail.com',
            "username": "user",
            "password": "user"}

    url = reverse('user:user-register')

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        account_data = self.data
        response = self.client.post(self.url, account_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_already_exists(self):
        """
        Ensure we can't have duplicate usernames and emails.
        """
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_adding_wrong_user_data(self):
        account_data = {
                "email": 'email',
                "username": "user1",
                "password": "user1"}
        response = self.client.post(self.url, account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)