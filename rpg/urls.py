from django.urls import path

from . import views

urlpatterns = [
    path("", views.CharacterAPIViewSet.as_view(actions={"get": "list"}, name="base")),
    path(
        "<int:pk>",
        views.CharacterAPIViewSet.as_view(
            actions={"get": "retrieve", "delete": "destroy"}
        ),
        name="list_char",
    ),
    path(
        "attrs/<int:pk>",
        views.AttrsAPIViewSet.as_view(
            actions={
                "get": "retrieve",
                "patch": "partial_update",
            }
        ),
        name="char-attr",
    ),
    path(
        "inventory/<int:pk>",
        views.InventoryAPIViewSet.as_view(
            actions={
                "get": "retrieve",
                "patch": "update",
            }
        ),
        name="inventory",
    ),
]
