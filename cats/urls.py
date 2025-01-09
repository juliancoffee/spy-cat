from django.urls import path

from . import views

app_name = "cats"

urlpatterns = [
    path("cat/", views.list, name="list"),
    # path("cat/<int:cat_id>", views.info, name="info"),
]
