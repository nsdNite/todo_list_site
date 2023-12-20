from django.contrib import admin
from django.urls import path

from todo_app.views import IndexView, TagListView, TaskCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("create/", TaskCreateView.as_view(), name="task-create")
]

app_name = "todo_app"
