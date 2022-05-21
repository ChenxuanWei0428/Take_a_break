from . import views
from django.urls import path

app_name = "take_a_break_app"
urlpatterns = [
    path("", views.start, name="take_a_break_start"),
    path("still_building", views.still_building, name = "still_building"),
    path("main", views.main, name = "main"),
    path("register", views.register, name = "register")
]