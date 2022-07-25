from . import views
from django.urls import path

app_name = "take_a_break_app"
urlpatterns = [
    path("", views.start, name="start"),
    path("still_building", views.still_building, name = "still_building"),
    path("main/guest", views.main, {"guest": True}, name = "main_guest"),
    path("main", views.main, {"guest": False}, name="main"),
    path("register", views.register_user, name = "register"),
    path("register_complete/<str:username>", views.register_complete, name = "register_complete"),
    path("recover_account", views.recover_account, name="recover_account"),
    path("add", views.add, name="add"),
]