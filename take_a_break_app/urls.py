from . import views
from django.urls import path

app_name = "take_a_break_app"
urlpatterns = [
    path("", views.start, name="start"),
    path("still_building", views.still_building, name = "still_building"),
    path("main", views.main, name = "main"),
    path("register", views.register, name = "register"),
    path("register_complete", views.register_complete, name = "register_complete"),
    path("recover_account", views.recover_account, name="recover_account")
]