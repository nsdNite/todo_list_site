from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View

from todo_app.forms import TaskForm
from todo_app.models import Task, Tag


class IndexView(View):
    template_name = "todo_app/index.html"

    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all()
        context = {'task_list': task_list}
        return render(request, self.template_name, context)


class TagListView(View):
    template_name = "todo_app/tag_list.html"

    def get(self, request, *args, **kwargs):
        tag_list = Tag.objects.all()
        context = {'tag_list': tag_list}
        return render(request, self.template_name, context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:index")
