from django.shortcuts import render
from django.views import generic, View

from todo_app.models import Task


class IndexView(View):
    model = Task
    template_name = "todo_app/"
    context_object_name = "task_list"

