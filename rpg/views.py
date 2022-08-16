from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Character
from .serializer import AttributesSerializer, CharacterSerializer, InventorySerializer


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
    
    
    
@api_view(http_method_names=("POST","GET"))
def edit_attributes(request, pk):
    character = Character.objects.filter(id=pk).first()
    serializer = AttributesSerializer(instance=character, data=request.data)
    if request.method == "POST":
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == "GET":
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
