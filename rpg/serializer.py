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


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            "inventory",
        )
        
    inventory = ItemSerializer(many=True)

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
            "char_class",
            "right_hand",
            "left_hand",
            "remain_points",
        )
    char_class = CharClassSerializer()
    right_hand = WeaponSerializer()
    left_hand = WeaponSerializer()
    remain_points = serializers.IntegerField()
