from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.mixins import CheckAuthenticatedMixin
from task_manager.tasks.forms import FilterTaskForm
from task_manager.tasks.mixins import IsOwnerMixin
from task_manager.tasks.models import Task


class TaskListView(CheckAuthenticatedMixin, FilterView):
    model = Task
    fields = "__all__"
    template_name = "tasks/list.html"
    context_object_name = "tasks"
    filterset_class = FilterTaskForm


class TaskCreateView(CheckAuthenticatedMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "description", "status", "executor", "labels"]
    success_url = reverse_lazy("tasks_list")
    success_message = _("The task has been created")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CheckAuthenticatedMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ["name", "description", "status", "executor", "labels"]
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks_list")
    success_message = _("The task has been successfully changed")


class TaskDeleteView(IsOwnerMixin, CheckAuthenticatedMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks_list")
    success_message = _("The task has been successfully deleted")


class TaskDetailView(CheckAuthenticatedMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
