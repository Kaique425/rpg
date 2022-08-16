from django.urls import path

from . import views

urlpatterns = [
    path("list", views.character_list, name="list_char"),
    path("<int:pk>", views.character_detail, name="cha_detail"),
    path("attrs/<int:pk>", views.character_attributes, name="char-attr"),
    path("inventory/<int:pk>", views.list_inventory, name="inventory"),
    path("update/attrs/<int:pk>", views.edit_attributes, name="update-attrs")
]
