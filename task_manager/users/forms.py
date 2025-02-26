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

    # def clean_password1(self):
    #     password1 = self.cleaned_data.get("password1")
    #     if len(password1) <= 3:
    #         raise forms.ValidationError(
    #             _("Your password must contain at least 3 characters.")
    #         )
    #     return password1

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 != password2:
    #         raise forms.ValidationError(_("Passwords must match."))
    #     return password2
