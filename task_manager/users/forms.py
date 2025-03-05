from django.forms import CharField, PasswordInput
from task_manager.users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class AddUserForm(UserCreationForm):

    password1 = CharField(
        label=_("Password"),
        widget=PasswordInput(),
        help_text=_("Your password must contain at least 3 characters."),
    )

    password2 = CharField(
        label=_("Password confirmation"),
        widget=PasswordInput(),
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
