from django.contrib import admin
from django.urls import path

from todo_app.views import IndexView, TagListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_app"
