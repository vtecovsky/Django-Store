from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.forms import UserRegistrationForm
from users.models import User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse("users:registration")

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store - Регистрация")
        self.assertEqual(response.context_data["form"], UserRegistrationForm())

    def test_user_registration_post_success(self):
        data = {
            "first_name": "Some_name",
            "last_name": "Some_surname",
            "username": "some_username",
            "email": "some_email@mail.ru",
            "password1": "Some_password1",
            "password2": "Some_password1",
        }

        response = self.client.post(self.path, data)

        username = data["username"]

        self.assertTrue(User.objects.filter(username=username).exists())
