from django.urls import path

from . import views

app_name = "cats"

urlpatterns = [
    # cats
    path("cat/", views.list_cats, name="list_cats"),
    path("cat/<int:cat_id>/", views.cat, name="cat"),
    path("cat/create/", views.create_cat, name="create_cat"),
    # missions
    path("mission/", views.list_missions, name="list_missions"),
    path("mission/create/", views.create_mission, name="create_mission"),
]
