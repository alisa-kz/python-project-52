from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.users.models import User
from task_manager.users.forms import AddUserForm
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


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
