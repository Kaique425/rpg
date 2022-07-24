from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Character
from .serializer import CharacterSerializer


@api_view(("GET",))
def character_detail(request):
    characters = Character.objects.chars()
    serializer = CharacterSerializer(characters, many=True)

    return Response(serializer.data)
