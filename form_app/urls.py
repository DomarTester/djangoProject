from django.urls import path
from form_app import views

app_name = "form_app"

urlpatterns = [
    path("1/", views.form1, name="form1"),
    path("2/", views.form2, name="form2"),
    path("task-list/", views.task_list, name="task_list"),
]
