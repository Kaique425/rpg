import factory
import factory.fuzzy

from ..models import Character


class Weapon(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    def __str__(self):
        return self.name


class Item(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    def __str__(self):
        return self.name


class CharClass(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)

    def __str__(self):
        return self.name


class CharacterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Character

    level = factory.fuzzy.FuzzyInteger(0, 100)
    name = factory.fuzzy.FuzzyText()
    char_class = factory.RelatedFactory(CharClass, "char-class")
    constitution = factory.fuzzy.FuzzyInteger(0, 100)
    vigor = factory.fuzzy.FuzzyInteger(0, 100)
    strengh = factory.fuzzy.FuzzyInteger(0, 100)
    dexterity = factory.fuzzy.FuzzyInteger(0, 100)
    intelligence = factory.fuzzy.FuzzyInteger(0, 100)
    charisma = factory.fuzzy.FuzzyInteger(0, 100)
    right_hand = factory.RelatedFactory(Weapon, "weapon")
    left_hand = factory.RelatedFactory(Weapon, "weapon")
    inventory = factory.RelatedFactory(Item, "item")
    remain_points = factory.fuzzy.FuzzyInteger(0, 100)
