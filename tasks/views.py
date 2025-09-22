from django.shortcuts import render

tasks = [
    {"title": "Finish homework", "done": False},
    {"title": "Buy groceries", "done": True},
]

def task_list(request):
    return render(request, "tasks/task_list.html", {"tasks": tasks})