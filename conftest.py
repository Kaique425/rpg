import pytest

from rpg.tests.factory import ProductFactory


@pytest.fixture
def product():
    return ProductFactory()
