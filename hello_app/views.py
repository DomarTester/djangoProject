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
        request, "hello.html", context={"name": name}
    )  # tutaj zamiast "name" może być "x" ale w tedy w szablonie odwołujemy się do "x"
