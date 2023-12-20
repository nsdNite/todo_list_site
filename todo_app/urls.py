from django.contrib import admin
from django.urls import path

from todo_app.views import (
    IndexView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todo_app"
