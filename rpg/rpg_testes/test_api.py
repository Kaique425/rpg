from unittest.mock import patch

import pytest
from django.urls import reverse
from rest_framework import test
from rpg.rpg_testes.rpg_factory import perform_instance_creation


@pytest.mark.django_db
class RpgAPItest(test.APITestCase):
    @patch("rpg.views.PaginationClass.page_size", new=3)
    def test_character_list_return_status_code_200(self):
        api_url = reverse("character:character-list")
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)

    @patch("rpg.views.PaginationClass.page_size", new=5)
    def test_character_list_loads_correct_number_of_chars(self):
        char = perform_instance_creation(qtd=10)
        url = reverse("character:character-list") + "?page=2"
        response = self.client.get(url)
        character_counter = len(response.data.get("results"))
        self.assertEqual(character_counter, 5)
