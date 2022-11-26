from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TaskTestCase(APITestCase):
    url = reverse("api:tasks")
    data = {
        "title": "hac utel",
        "description": "borsh",
    }

    def setUp(self):
        self.user_data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password": "123456",
            "is_staff": "true"
        }

        self.register_url = reverse("user:user-register")

        self.client.post(self.register_url, self.user_data)  # user created

        auth_url = reverse("user:login")  # for example :"users:token_obtain_pair"
        self.access_token = self.client.post(auth_url, {
            "email": self.user_data.get("email"),
            "password": self.user_data.get("password")
        }).data.get("access")  # get access_token for authorization
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_task_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_adding_task(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_wrong_data(self):
        self.data['title'] = ' '
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)