from django.forms import (
    CheckboxInput,
    ModelChoiceField,
    ModelForm,
    ModelMultipleChoiceField,
)
from django.utils.translation import gettext as _
from django_filters.filters import BooleanFilter, ModelChoiceFilter
from django_filters.filterset import FilterSet

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class AddTaskForm(ModelForm):
    status = ModelChoiceField(
        queryset=Status.objects.all(),
        label=_("Status"),
    )

    executor = ModelChoiceField(
        queryset=User.objects.all(),
        label=_("Executor"),
    )

    labels = ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_("Labels"),
    )

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]


class FilterTaskForm(FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_("Status"),
    )

    executor = ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_("Executor"),
    )

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label"),
    )

    self_tasks = BooleanFilter(
        widget=CheckboxInput,
        field_name="author",
        method="self_tasks_filter",
        label=_("Only your own tasks"),
    )

    def self_tasks_filter(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "labels", "self_tasks"]
