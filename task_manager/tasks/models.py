from django.db import models
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_("Status"),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("Executor"),
        related_name="executor",
    )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="author",
    )
    labels = models.ManyToManyField(Label, verbose_name=_("Labels"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
