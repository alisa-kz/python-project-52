from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.utils.translation import gettext as _

from task_manager.mixins import CheckAuthenticatedMixin
from task_manager.tasks.forms import AddTaskForm
from task_manager.tasks.models import Task


class IsOwnerMixin(CheckAuthenticatedMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            messages.error(request, _("Only the author can delete a task."))
            return redirect("tasks_list")
        return super().dispatch(request, *args, **kwargs)


class TaskListView(CheckAuthenticatedMixin, ListView):
    model = Task
    fields = "__all__"
    template_name = "tasks/list.html"
    context_object_name = "tasks"


class TaskCreateView(CheckAuthenticatedMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "description", "status", "executor"]
    success_url = reverse_lazy("tasks_list")
    success_message = _("The task has been created")


class TaskUpdateView(CheckAuthenticatedMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ["name", "description", "status", "executor"]
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks_list")
    success_message = _("The task has been successfully changed")


class TaskDeleteView(CheckAuthenticatedMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks_list")
    success_message = _("The task has been successfully deleted")


class TaskDetailView(CheckAuthenticatedMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
