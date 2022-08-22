from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

rpg_router = SimpleRouter()
rpg_router.register(
    prefix="",
    viewset=views.CharacterAPIViewSet,
)


print(rpg_router.urls)

"""    path(
        "",
        views.CharacterAPIViewSet.as_view(
            actions={"get": "list", "post": "create"}, name="base"
        ),
    ),
    path(
        "<int:pk>",
        views.CharacterAPIViewSet.as_view(
            actions={"get": "retrieve", "delete": "destroy"}
        ),
        name="list_char",
    ),"""

urlpatterns = [
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
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(rpg_router.urls)),
]
