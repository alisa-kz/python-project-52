from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.users.forms import AddUserForm, UpdateUserForm
from task_manager.users.mixins import IsOwnerMixin
from task_manager.users.models import User


class UserListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = AddUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy("login")
    success_message = _("The user has been successfully registered")


class UserUpdateView(IsOwnerMixin, SuccessMessageMixin, UpdateView):
    form_class = UpdateUserForm
    model = User
    template_name = "users/update.html"
    success_url = reverse_lazy("users_list")
    success_message = _("User successfully updated")


class UserDeleteView(IsOwnerMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users_list")
    success_message = _("User successfully deleted")
