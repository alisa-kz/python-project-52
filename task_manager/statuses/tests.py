import json

from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.users.models import User


class TestStatus(TestCase):
    fixtures = ["users.json", "statuses.json"]

    def test_create_status(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        with open("task_manager/fixtures/status_data.json", "r") as f:
            data = json.load(f)
            self.client.post(reverse("create_status"), data[0])
            self.assertTrue(
                Status.objects.filter(name=data[0]["name"]).exists()
                )

    def test_update_status(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        status = Status.objects.get(name="MyStatus")
        with open("task_manager/fixtures/status_data.json", "r") as f:
            data = json.load(f)
            self.client.post(reverse(
                "update_status", args=[status.pk]), data[1]
                )
            status.refresh_from_db()
            self.assertEqual(status.name, data[1]["name"])

    def test_delete_status(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        status = Status.objects.get(name="MyStatus")
        self.client.post(reverse("delete_status", args=[status.pk]))
        self.assertFalse(Status.objects.filter(name="MyStatus").exists())
