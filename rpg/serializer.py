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
        )
        read_only_fields = ()

    id = serializers.IntegerField(read_only=False)


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("inventory", "id")

    def update(self, instance, validated_data):
        inventory = validated_data.pop("inventory")
        items_ids = [item["id"] for item in inventory]
        print(items_ids)
        instance.inventory.clear()
        for id in items_ids:
            item = Item.objects.filter(id=id).first()
            instance.inventory.add(item)
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
