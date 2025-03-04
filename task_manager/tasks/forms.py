from django import forms

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.labels.models import Label
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

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_("Labels"),
        # widget=forms.SelectMultiple(),
        # required=False,
    )

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]
