from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import CheckAuthenticatedMixin
from task_manager.statuses.models import Status


class StatusListView(CheckAuthenticatedMixin, ListView):
    model = Status
    template_name = "statuses/list.html"
    context_object_name = "statuses"


class StatusCreateView(
    CheckAuthenticatedMixin, SuccessMessageMixin, CreateView
):
    model = Status
    template_name = "statuses/create.html"
    fields = ["name"]
    success_url = reverse_lazy("statuses_list")
    success_message = _("The status has been successfully created")


class StatusUpdateView(
    CheckAuthenticatedMixin, SuccessMessageMixin, UpdateView
):
    model = Status
    fields = ["name"]
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses_list")
    success_message = _("The status has been successfully changed")


class StatusDeleteView(
    CheckAuthenticatedMixin, SuccessMessageMixin, DeleteView
):
    model = Status
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses_list")
    success_message = _("The status has been successfully deleted")

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, _(
                    "Unable to delete a status because it is being used"
                    )
            )
            return redirect(self.success_url)
