from django.urls import path

from . import views

urlpatterns = [
    path("list", views.character_list, name="list_char"),
    path("<int:pk>", views.character_detail, name="cha_detail"),
]
