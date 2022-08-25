import pytest
from conftest import character_teste
from django.urls import reverse
from rest_framework import test

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class RpgAPItest(test.APITestCase):
    def test_character_list_return_status_code_200(self):
        api_url = reverse("character:character-list")
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)

    def test_character_list_loads_correct_number_of_chars(self):
        url = reverse("character:character-list")
        response = self.client.get(url)
        counter = response.data.get("count")
        print(counter)
        self.assertEqual(counter, 0)
        self.assertEqual(character_teste.id, 1)
