from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Character, Item
from .permissions import IsOwner
from .serializer import AttributesSerializer, CharacterSerializer, ItemSerializer


class PaginationClass(PageNumberPagination):
    page_size = 3


class CharacterAPIViewSet(ModelViewSet, IsOwner):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = PaginationClass
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


class ItemAPIViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(["GET"])
def inventory(request, pk):
    items = get_list_or_404(Item, character=pk)
    qs = Item.objects.filter(character=pk)
    print(items)
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)
