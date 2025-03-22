import json

from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.users.models import User


class TestLabel(TestCase):
    fixtures = ["users.json", "labels.json"]

    def test_create_label(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        with open("task_manager/fixtures/label_data.json", "r") as f:
            data = json.load(f)
            self.client.post(reverse("create_label"), data[0])
            self.assertTrue(
                Label.objects.filter(name=data[0]["name"]).exists()
                )

    def test_update_label(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        label = Label.objects.get(name="MyLabel")
        with open("task_manager/fixtures/label_data.json", "r") as f:
            data = json.load(f)
            self.client.post(reverse("update_label", args=[label.pk]), data[1])
            label.refresh_from_db()
            self.assertEqual(label.name, data[1]["name"])

    def test_delete_label(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        label = Label.objects.get(name="MyLabel")
        self.client.post(reverse("delete_label", args=[label.pk]))
        self.assertFalse(Label.objects.filter(name="MyLabel").exists())
