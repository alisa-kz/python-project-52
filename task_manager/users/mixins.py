from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from task_manager.mixins import CheckAuthenticatedMixin


class IsOwnerMixin(CheckAuthenticatedMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            messages.error(
                request, _(
                    "You do not have permission to modify another user."
                    )
            )
            return redirect("users_list")
        return super().dispatch(request, *args, **kwargs)
