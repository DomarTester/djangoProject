from django.shortcuts import render

TASKS = []


def form1(request):
    data = request.GET
    task = data.get("task")
    if task:
        TASKS.append(task)
    return render(request, "form_app/form1.html")
