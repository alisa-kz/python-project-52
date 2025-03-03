from django import forms

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User
from django.utils.translation import gettext as _


class AddTaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_("Status"),
    )

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label=_("Executor"),
    )

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor"]
