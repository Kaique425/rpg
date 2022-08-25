import factory
import factory.fuzzy

from ..models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyDecimal(5.0, 999.99)
    product_image = factory.django.ImageField()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    is_available = factory.Faker("pybool")

    class Meta:
        model = Product


class CharClass(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)

    def __str__(self):
        return self.name


class CharacterFactory(factory.django.DjangoModelFactory):
    level = factory.fuzzy.FuzzyInteger(0, 100)
    name = factory.fuzzy.FuzzyText()
    char_class = factory.RelatedFactory(CharClass, "char-class")
    constitution = factory.fuzzy.FuzzyInteger(0, 100)
    vigor = factory.fuzzy.FuzzyInteger(0, 100)
    strengh = factory.fuzzy.FuzzyInteger(0, 100)
    dexterity = factory.fuzzy.FuzzyInteger(0, 100)
    intelligence = factory.fuzzy.FuzzyInteger(0, 100)
    charisma = factory.fuzzy.FuzzyInteger(0, 100)
    right_hand = factory.RelatedFactory(CharClass, "char-class")
    left_hand = factory.RelatedFactory(CharClass, "char-class")
    inventory = models.ManyToManyField(Item, related_name="inventory")
    remain_points = models.IntegerField(default=0)
