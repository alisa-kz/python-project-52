# from django.core.context_processors import request
from django.utils.translation import gettext as _


def get_context(request):
    context = {}
    context["app_name_nav"] = _("Task Manager")
    context["users_nav"] = _("Users")
    context["sign_in_nav"] = _("Sign in")
    context["sign_up_nav"] = _("Sign up")
    context["welcome"] = _("Welcome to Task Manager")
    context["description"] = _(
        """Here you can set tasks, assign performers and change their
        statuses"""
    )
    context["user_name"] = _("User name")
    context["first_name_form"] = _("First name")
    context["last_name_form"] = _("Last name")
    context["password"] = _("Password")
    context["password_confirmation"] = _("Password confirmation")
    context["full_name"] = _("Full name")
    context["date_joined"] = _("Date joined")
    context["update"] = _("Update")
    context["delete"] = _("Delete")
    context["user_name_description"] = _(
        """Required field. No more than 150 characters. Only letters,
        numbers and symbols @/./+/-/_."""
    )
    context["password_description"] = _(
        "Your password must contain at least 3 characters."
    )
    context["confirm_password_description"] = _(
        "To confirm, please enter your password again."
    )
    context["register"] = _("Register")
    context["login"] = _("Login")
    context["log_in"] = _("Log in")
    return context
