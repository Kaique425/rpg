import factory
import factory.fuzzy
from pytest_factoryboy import register

from ..models import Character, CharClass, Item, Weapon


class WeaponFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Weapon

    name = factory.fuzzy.FuzzyText()

    def __str__(self):
        return self.name


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.fuzzy.FuzzyText()

    def __str__(self):
        return self.name


class CharClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CharClass

    name = factory.fuzzy.FuzzyText()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)

    def __str__(self):
        return self.name


class CharacterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Character

    level = factory.fuzzy.FuzzyInteger(0, 100)
    name = factory.fuzzy.FuzzyText()
    constitution = factory.fuzzy.FuzzyInteger(0, 100)
    vigor = factory.fuzzy.FuzzyInteger(0, 100)
    strengh = factory.fuzzy.FuzzyInteger(0, 100)
    dexterity = factory.fuzzy.FuzzyInteger(0, 100)
    intelligence = factory.fuzzy.FuzzyInteger(0, 100)
    remain_points = factory.fuzzy.FuzzyInteger(0, 100)
    charisma = factory.fuzzy.FuzzyInteger(0, 100)
    char_class = factory.SubFactory(CharClassFactory)
    right_hand = factory.SubFactory(WeaponFactory)
    left_hand = factory.SubFactory(WeaponFactory)


def perform_instance_creation(qtd=1, factory=CharacterFactory):
    if qtd == 1:
        return factory()
    instances = [factory() for n in range(0, qtd)]

    return instances
