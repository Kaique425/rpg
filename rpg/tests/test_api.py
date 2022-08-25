from django.urls import reverse
from rest_framework import test


class RpgAPItest(test.APITestCase):
    def test_character_list_return_status_code_200(self):
        api_url = reverse("character:character-list")
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)

    def test_character_list_loads_correct_number_of_chars(self):
        url = reverse("character:character-list")
        response = self.client.get(url)
        self.asserIn()
