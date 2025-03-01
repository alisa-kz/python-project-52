from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.users.models import User
from task_manager.users.forms import AddUserForm, UpdateUserForm
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.urls import reverse


class UserListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"


class UserCreateView(CreateView, SuccessMessageMixin):
    form_class = AddUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy("login")
    success_message = _("The user has been successfully registered")

    # def form_valid(self, form):
    #     messages.success(self.request, "Пользователь успешно зарегистрирован")
    #     return super().form_valid(form)


class UserUpdateView(UpdateView, SuccessMessageMixin):
    form_class = UpdateUserForm
    model = User
    template_name = "users/update.html"
    success_url = reverse_lazy("users_list")
    success_message = _("User successfully updated")


class UserDeleteView(DeleteView, SuccessMessageMixin):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users_list")
    success_message = _("User successfully deleted")
