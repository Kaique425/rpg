from rest_framework import serializers

from .models import Character, CharClass, Item, Weapon


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            "constitution",
            "vigor",
            "strengh",
            "dexterity",
            "intelligence",
            "charisma",
        )
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("name",)


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ("name",)


class CharClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharClass
        fields = ("name", "description")


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            "id",
            "level",
            "name",
            "attributes",
            "char_class",
            "inventory",
            "right_hand",
            "left_hand",
            "remain_points",
        )
    attributes = AttributesSerializer()
    char_class = CharClassSerializer()
    inventory = ItemSerializer(many=True)
    right_hand = WeaponSerializer()
    left_hand = WeaponSerializer()
    remain_points = serializers.IntegerField()
