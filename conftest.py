import pytest

from rpg.rpg_tests.rpg_factory import CharacterFactory


@pytest.fixture
def character_teste():
    return CharacterFactory.create()
