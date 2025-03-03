from django import forms
from task_manager.users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class AddUserForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(),
        help_text=_("Your password must contain at least 3 characters."),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(),
        help_text=_("To confirm, please enter your password again."),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        ]


class UpdateUserForm(AddUserForm):

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username

