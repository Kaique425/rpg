from audioop import reverse

from django.contrib.auth.models import User
from django.urls import reverse


class RpgMixin:
    def create_user(self):
        user_data = {
            "username": "test_user",
            "password": "test_password",
        }
        user = User(username=user_data["username"])
        user.set_password(user_data["password"])
        user.save()

        return user_data

    def get_acess_token(self):
        user = self.create_user()
        response = self.client.post(reverse("character:token_obtain_pair"), data=user)
        return response.data
