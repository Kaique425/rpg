from django.urls import path

from . import views

urlpatterns = [
    path("list", views.character_detail, name="list_char"),
]
