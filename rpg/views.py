from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Character
from .permissions import IsOwner
from .serializer import AttributesSerializer, CharacterSerializer, InventorySerializer


class CharacterAPIViewSet(ModelViewSet, IsOwner):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["post", "get", "patch", "head", "options", "delete"]

    def get_object(self):
        pk = self.kwargs.get("pk", "")
        object = get_object_or_404(self.get_queryset(), id=pk)

        self.check_object_permissions(self.request, object)

        return object

    def get_permissions(self):
        if self.request.method in ["PATCH", "POST"]:
            return [IsOwner()]

        return super().get_permissions()


class AttrsAPIViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = AttributesSerializer


class InventoryAPIViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = InventorySerializer
