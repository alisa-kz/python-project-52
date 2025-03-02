from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from task_manager.users.models import User
from task_manager.users.forms import AddUserForm, UpdateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.urls import reverse


class IsOwnerMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request, _('You are not logged in! Please log in.')
                )
            return redirect(reverse('login'))
        else:
            messages.error(
                self.request, _(
                    "You do not have permission to modify another user."
                    )
            )
            return redirect("users_list")


class UserListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    form_class = AddUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        messages.success(
            request, _("The user has been successfully registered")
            )
        return super().post(request, *args, **kwargs)


class UserUpdateView(IsOwnerMixin, UpdateView):
    form_class = UpdateUserForm
    model = User
    template_name = "users/update.html"
    success_url = reverse_lazy("users_list")

    def post(self, request, *args, **kwargs):
        messages.success(request, _("User successfully updated"))
        return super().post(request, *args, **kwargs)


class UserDeleteView(IsOwnerMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users_list")

    def post(self, request, *args, **kwargs):
        messages.success(request, _("User successfully deleted"))
        return super().post(request, *args, **kwargs)
