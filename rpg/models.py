from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CharacterManager(models.Manager):
    def chars(self):
        return (
            self.filter()
            .order_by("id")
            .select_related("char_class", "right_hand", "left_hand")
            .prefetch_related("inventory")
        )


class CharClass(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Item(models.Model):
    character = models.ForeignKey("rpg.Character", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=64)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(20)], null=True
    )

    def __str__(self):
        return self.name


class Character(models.Model):
    class Meta:
        ordering = [
            "id",
        ]

    level = models.IntegerField(default=1)
    objects = CharacterManager()
    name = models.CharField(max_length=64)
    char_class = models.ForeignKey(
        CharClass, null=True, related_name="charclass", on_delete=models.SET_NULL
    )
    constitution = models.IntegerField(default=0)
    vigor = models.IntegerField(default=0)
    strengh = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    right_hand = models.ForeignKey(
        Weapon, related_name="rightweapon", null=True, on_delete=models.SET_NULL
    )
    left_hand = models.ForeignKey(
        Weapon, related_name="leftweapon", null=True, on_delete=models.SET_NULL
    )
    remain_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
