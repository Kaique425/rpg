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
    prefix="characters",
    viewset=views.CharacterAPIViewSet,
    basename="character",
)

items_router = SimpleRouter()

items_router.register(
    prefix="items",
    viewset=views.ItemAPIViewSet,
    basename="items",
)

weapon_router = SimpleRouter()
weapon_router.register(
    prefix="weapons",
    viewset=views.WeaponViewSet,
    basename="weapon",
)
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
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(weapon_router.urls)),
    path("", include(items_router.urls)),
    path("", include(character_router.urls)),
]
