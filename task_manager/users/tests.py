import json

from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User


class TestUser(TestCase):
    fixtures = ["users.json"]

    def test_create_user(self):
        with open('task_manager/fixtures/user_data.json', 'r') as f:
            data = json.load(f)
            self.client.post(reverse('create_user'), data[0])
            self.assertTrue(
                User.objects.filter(username=data[0]["username"]).exists()
                )

    def test_update_user(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        with open("task_manager/fixtures/user_data.json", "r") as f:
            data = json.load(f)
            self.client.post(reverse("update_user", args=[user.pk]), data[1])
            user.refresh_from_db()
            self.assertEqual(user.last_name, data[1]["last_name"])

    def test_delete_user(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        self.client.post(reverse("delete_user", args=[user.pk]))
        self.assertFalse(User.objects.filter(username="TomSm").exists())
