from rest_framework import serializers

from .models import Character, CharClass, GenericItem, Item, Weapon


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


class GenericItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = GenericItem
        fields = (
            "id",
            "name",
            "description",
        )


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    generic_item = GenericItemSerializer(read_only=True)

    class Meta:
        model = Item
        fields = (
            "generic_item",
            "id",
            "quantity",
            "character",
        )


"""    def update(self, instance, validated_data):
        print(validated_data)

        return instance"""


class WeaponSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Weapon
        fields = ("name", "id")


class CharClassSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = CharClass
        fields = ("id", "name", "description")


class CharacterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

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

    char_class = CharClassSerializer(read_only=True)
    right_hand = WeaponSerializer()
    left_hand = WeaponSerializer()
    remain_points = serializers.IntegerField()

    def update(self, instance, validated_data):
        right_hand = validated_data.get("right_hand")
        left_hand = validated_data.get("left_hand")
        teste1 = Weapon.objects.filter(id=right_hand["id"]).first()
        teste2 = Weapon.objects.filter(id=left_hand["id"]).first()
        instance.right_hand = teste1
        instance.left_hand = teste2
        instance.save()
        return instance
