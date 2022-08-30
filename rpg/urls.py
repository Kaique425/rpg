from django.urls import include, path, reverse
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

app_name = "character"

character_router = SimpleRouter()
character_router.register(
    prefix="",
    viewset=views.CharacterAPIViewSet,
)

items_router = SimpleRouter()
items_router.register(prefix="item", viewset=views.ItemAPIViewSet, basename="items")
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
    path("inventory/<int:pk>", views.inventory, name="inventory"),
    path("", include(items_router.urls)),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(character_router.urls)),
]
