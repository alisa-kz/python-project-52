from django.test import TestCase
from django.urls import reverse

from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User


class TestTask(TestCase):

    def test_create_task(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        self.client.post(reverse("create_status"), {"name": "MyStatus"})
        self.client.post(reverse("create_label"), {"name": "MyLabel"})
        task_data = {
            "name": "MyTask",
            "description": "SoImportantTask",
            "status": "1",
            "executor": "1",
            "labels": "1",
        }
        self.client.post(reverse("create_task"), task_data)
        self.assertTrue(Task.objects.filter(name=task_data["name"]).exists())

    def test_update_task(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        self.client.post(reverse("create_status"), {"name": "MyStatus"})
        self.client.post(reverse("create_label"), {"name": "MyLabel"})
        task_data = {
            "name": "MyTask",
            "description": "SoImportantTask",
            "status": "1",
            "executor": "1",
            "labels": "1",
        }
        self.client.post(reverse("create_task"), task_data)
        task = Task.objects.get(name="MyTask")
        update_data = {
            "name": "MyTask",
            "description": "NotSoImportantTask",
            "status": "1",
            "executor": "1",
            "labels": "1",
        }
        self.client.post(reverse("update_task", args="1"), update_data)
        task.refresh_from_db()
        self.assertEqual(task.description, update_data["description"])

    def test_delete_task(self):
        user_data = {
            "first_name": "Tom",
            "last_name": "Smith",
            "username": "TomSm",
            "password1": "1234",
            "password2": "1234",
        }
        self.client.post(reverse("create_user"), user_data)
        self.client.login(username=user_data["username"], password="1234")
        self.client.post(reverse("create_status"), {"name": "MyStatus"})
        self.client.post(reverse("create_label"), {"name": "MyLabel"})
        task_data = {
            "name": "MyTask",
            "description": "SoImportantTask",
            "status": "1",
            "executor": "1",
            "labels": "1",
        }
        self.client.post(reverse("create_task"), task_data)
        task = Task.objects.get(name="MyTask")
        self.client.post(reverse("delete_task", args=[task.pk]))
        self.assertFalse(Task.objects.filter(name="MyTask").exists())
