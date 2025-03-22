from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from task_manager.mixins import CheckAuthenticatedMixin


class IsOwnerMixin(CheckAuthenticatedMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            messages.error(request, _("Only the author can delete a task."))
            return redirect("tasks_list")
        return super().dispatch(request, *args, **kwargs)
