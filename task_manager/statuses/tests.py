from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status


class TestStatus(TestCase):

    def test_create_status(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        status_data = {
            "name": "MyStatus",
        }
        self.client.post(reverse("create_status"), status_data)
        self.assertTrue(
            Status.objects.filter(name=status_data["name"]).exists()
            )

    def test_update_status(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        status_data = {
            "name": "MyStatus",
        }
        self.client.post(reverse("create_status"), status_data)
        status = Status.objects.get(name="MyStatus")
        update_data = {
            "name": "NewStatus",
        }
        self.client.post(reverse("update_status", args="1"), update_data)
        status.refresh_from_db()
        self.assertEqual(status.name, update_data["name"])

    def test_delete_status(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        status_data = {
            "name": "MyStatus",
        }
        self.client.post(reverse("create_status"), status_data)
        status = Status.objects.get(name="MyStatus")
        self.client.post(reverse("delete_status", args=[status.pk]))
        self.assertFalse(Status.objects.filter(name="MyStatus").exists())
