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
        fields = (
            "id",
            "name",
            "quantity",
            "character",
        )

    id = serializers.IntegerField(read_only=True)


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("inventory", "id")

    def update(self, instance, validated_data):
        inventory = validated_data.pop("inventory")
        item_instances = [
            Item.objects.filter(id=item["id"]).first() for item in inventory
        ]
        instance.inventory.clear()
        instance.inventory.add(*item_instances)
        print(instance.inventory.all())
        instance.save()
        return instance

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
