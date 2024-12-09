import datetime

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.utils.html import escape


def hello(request):  # request to tylko konwencja (może być nawet 'dupa')
    return HttpResponse(
        "Hello World!"
    )  # Widoki nie mogą zwracać byle czego – mają zwracać obekt klasy HttpResponse


def hello_name(request, name):  # w urlu i tutaj musi być ta sama nazwa parametru
    name = escape(
        name
    )  # zmienia name tak by np javascript zmienił się w input i specjalne znaki zmienia na ich dpowiedniki
    return HttpResponse(f"Hello {name}!")


def hello_template(request, name):
    return render(
        request, "hello_app/hello.html", context={"name": name}
    )  # tutaj zamiast "name" może być "x" ale w tedy w szablonie odwołujemy się do "x"


def is_it_monday(requerst):
    now = datetime.datetime.now()
    is_monday = now.weekday() == 0
    return render(
        requerst, "hello_app/is_it_monday.html", context={"is_monday": is_monday}
    )


def dtl(request):
    fruits = ["apple", "orange", "pear"]

    return render(request, "hello_app/dtl.html", context={"fruits": fruits})


def first_view(request):
    return render(request, "hello_app/first.html")


def second_view(request):
    return render(request, "hello_app/second.html")


def third_view(request, param):
    return render(request, "hello_app/third.html", context={"param": param})


def child1_view(request):
    return render(request, "hello_app/child1.html")


def child2_view(request):
    return render(request, "hello_app/child2.html")
