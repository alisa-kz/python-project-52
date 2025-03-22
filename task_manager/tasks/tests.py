import json

from django.test import TestCase
from django.urls import reverse

from task_manager.tasks.models import Task
from task_manager.users.models import User


class TestTask(TestCase):
    fixtures = ["users.json", "tasks.json", "statuses.json", "labels.json"]

    def test_create_task(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        with open("task_manager/fixtures/task_data.json", "r") as f:
            data = json.load(f)
            self.client.post(reverse("create_task"), data[0])
            self.assertTrue(Task.objects.filter(name=data[0]["name"]).exists())

    def test_update_task(self):
        user = User.objects.get(username="TomSm")
        self.client.login(username=user.username, password="1234")
        task = Task.objects.get(name="MyTask")
        with open("task_manager/fixtures/task_data.json", "r") as f:
            data = json.load(f)
            self.client.post(reverse("update_task", args=[task.pk]), data[1])
            task.refresh_from_db()
            self.assertEqual(task.description, data[1]["description"])
