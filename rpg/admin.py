from django.contrib import admin

from .models import Character, CharClass, GenericItem, Item, Weapon

# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name",)
    list_per_page = 12
    ordering = ("name",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ...


@admin.register(CharClass)
class CharClassAdmin(admin.ModelAdmin):
    ...


@admin.register(GenericItem)
class GenericItemAdmin(admin.ModelAdmin):
    ...


"""
@admin.register(Attributes)
class AttributesClassAdmin(admin.ModelAdmin):
    ...
"""


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    ...
