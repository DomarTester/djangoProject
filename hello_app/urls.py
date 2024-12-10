# Lokalne ulrsy dla aplikacji to dobra praktyka którą powinno się stosować
# jest to wazne aby aplikacja była samodzielna
from django.urls import path
from hello_app import views

app_name = "hello_app"  # tworzymy "szufladkę" tak jak dla staticów i templatek (bo urle i ich nazwy tez trafiają do jednego worka)

urlpatterns = [
    path("", views.hello),
    path(
        "param/<str:name>/",  # param, bo inaczej chwytałoby wszystkie stringi i inne urle by nie działaly, bo parametr ma być stringiem
        views.hello_name,  # przykład parametryzacji. W konwenterze nazwa argumentu z funckji (muszą być te same nazwy)
    ),  # może być samo <name> i też zadziała, jako domyslny
    path("template/<str:name>/", views.hello_template),
    path("is-it-monday/", views.is_it_monday, name="is_it_monday"),
    path("dtl/", views.dtl, name="dtl"),
    path("first/", views.first_view, name="first"),
    path("second/", views.second_view, name="second"),
    path("third/<str:param>/", views.third_view, name="third"),
    path("child1", views.child1_view, name="child1"),
    path("child2", views.child2_view, name="child2"),
]
