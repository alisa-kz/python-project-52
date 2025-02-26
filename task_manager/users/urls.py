from django.urls import path

from task_manager.users.views import UserListView, UserCreateView

urlpatterns = [
    path("", UserListView.as_view()),
    path("create/", UserCreateView.as_view()),
]
