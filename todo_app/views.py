from django.shortcuts import render
from django.views import generic, View

from todo_app.models import Task


class IndexView(View):
    template_name = "todo_app/index.html"

    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all()
        context = {'task_list': task_list}
        return render(request, self.template_name, context)
