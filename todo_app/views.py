from django.shortcuts import render
from django.views import generic, View


class IndexView(View):
    template_name = "todo_app/index.html"
