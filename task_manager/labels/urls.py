from django.urls import path

from .views import (
    LabelCreateView,
    LabelDeleteView,
    LabelListView,
    LabelUpdateView,
)

urlpatterns = [
    path("", LabelListView.as_view(), name="labels_list"),
    path("create/", LabelCreateView.as_view(), name="create_label"),
    path("<int:pk>/update/", LabelUpdateView.as_view(), name="update_label"),
    path("<int:pk>/delete/", LabelDeleteView.as_view(), name="delete_label"),
]
