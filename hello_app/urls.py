# Lokalne ulrsy dla aplikacji to dobra praktyka którą powinno się stosować
# jest to wazne aby aplikacja była samodzielna
from django.urls import path
from hello_app import views

urlpatterns = [
    path("", views.hello),
]
