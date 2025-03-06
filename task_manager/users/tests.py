from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User


class TestUser(TestCase):

    def test_create_user(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse('create_user'), user_data)
        self.assertTrue(
            User.objects.filter(username=user_data["username"]).exists()
            )

    def test_update_user(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse('create_user'), user_data)
        user = User.objects.get(username="TomSm")
        self.client.login(username=user_data['username'], password="1234")
        update_data = {
            "first_name": "Tom",
            "last_name": "Small",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("update_user", args='1'), update_data)
        user.refresh_from_db()
        self.assertEqual(user.last_name, update_data["last_name"])

    def test_delete_user(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        self.client.post(reverse("delete_user", args=[user.pk]))
        self.assertFalse(User.objects.filter(username="TomSm").exists())
