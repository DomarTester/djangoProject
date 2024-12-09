# Lokalne ulrsy dla aplikacji to dobra praktyka którą powinno się stosować
# jest to wazne aby aplikacja była samodzielna
from django.urls import path
from hello_app import views

urlpatterns = [
    path("", views.hello),
    path(
        "param/<str:name>",
        views.hello_name,  # param, bo inaczej chwytałoby wszystkie stringi,
    ),  # przykład parametryzacji. W konwenterzze nazwa argumentu z funckji (muszą być te same nazwy)
    # może być samo <name> i też zadziała, jako domyslny
    path("template/<str:name>", views.hello_template),
]
