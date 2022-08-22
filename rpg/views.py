from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Character
from .serializer import AttributesSerializer, CharacterSerializer, InventorySerializer


class CharacterAPIViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = PageNumberPagination
    permission_classes = [
        IsAuthenticated,
    ]


class AttrsAPIViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = AttributesSerializer


class InventoryAPIViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = InventorySerializer


@api_view(("GET",))
def character_list(request):
    characters = Character.objects.chars()
    serializer = CharacterSerializer(characters, many=True)

    return Response(serializer.data)


@api_view(
    http_method_names=[
        "GET",
    ]
)
def character_detail(request, pk):
    character = Character.objects.filter(id=pk).first()
    serializer = CharacterSerializer(instance=character, many=False)
    return Response(serializer.data)


@api_view(
    http_method_names=[
        "GET",
    ]
)
def character_attributes(request, pk):
    character = Character.objects.filter(id=pk).first()
    serializer = AttributesSerializer(instance=character, many=False)
    return Response(serializer.data)


@api_view(http_method_names=("GET",))
def list_inventory(request, pk):
    character = Character.objects.filter(id=pk).first()
    serializer = InventorySerializer(instance=character, many=False)
    return Response(serializer.data)
