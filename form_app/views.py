from django.http import HttpResponse
from django.shortcuts import render, redirect

TASKS = []


def form1(request):
    data = request.GET
    task = data.get("task")
    if task:
        TASKS.append(task)
    return render(request, "form_app/form1.html")


def form2(request):
    if request.method == "GET":
        return render(request, "form_app/form2.html")
    elif request.method == "POST":
        data = request.POST
        task = data.get("task")
        if task:
            TASKS.append(task)
            return redirect("form_app:form2")
        return render(request, "form_app/form2.html")
    else:
        return HttpResponse(status=405)


def task_list(request):
    return render(request, "form_app/list.html", context={"tasks": TASKS})
