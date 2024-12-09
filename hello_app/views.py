from django.shortcuts import render
from django.shortcuts import HttpResponse


def hello(request):  # request to tylko konwencja (może być nawet 'dupa')
    return HttpResponse(
        "Hello World!"
    )  # Widoki nie mogą zwracać byle czego – mają zwracać obekt klasy HttpResponse
