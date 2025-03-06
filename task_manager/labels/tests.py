from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label


class TestLabel(TestCase):

    def test_create_label(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        label_data = {
            "name": "MyLabel",
        }
        self.client.post(reverse("create_label"), label_data)
        self.assertTrue(Label.objects.filter(name=label_data["name"]).exists())

    def test_update_label(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        label_data = {
            "name": "MyLabel",
        }
        self.client.post(reverse("create_label"), label_data)
        label = Label.objects.get(name="MyLabel")
        update_data = {
            "name": "NewLabel",
        }
        self.client.post(reverse("update_label", args="1"), update_data)
        label.refresh_from_db()
        self.assertEqual(label.name, update_data["name"])

    def test_delete_label(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        label_data = {
            "name": "MyLabel",
        }
        self.client.post(reverse("create_label"), label_data)
        label = Label.objects.get(name="MyLabel")
        self.client.post(reverse("delete_label", args=[label.pk]))
        self.assertFalse(Label.objects.filter(name="MyLabel").exists())
