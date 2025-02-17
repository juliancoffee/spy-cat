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
    path("mission/<int:mission_id>", views.mission, name="mission"),
    path("mission/create/", views.create_mission, name="create_mission"),
    # targets
    path("target/<int:target_id>/", views.target, name="target"),
]
