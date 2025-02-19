from django.views.generic import TemplateView
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = _("Task Manager")
        context["users"] = _("Users")
        context["sign_in"] = _("Sign in")
        context["sign_up"] = _("Sign up")
        context["welcome"] = _("Welcome to Task Manager")
        context["description"] = _(
            """Here you can set tasks, assign performers and change their
            statuses"""
        )
        return context
