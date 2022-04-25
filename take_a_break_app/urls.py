from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path("", views.intro, name="Take_a_break_start"),
    path("still_building", views.still_building, name = "still_building"),
]