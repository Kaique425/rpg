import pytest

from rpg.rpg_testes.rpg_factory import CharacterFactory


@pytest.fixture()
def character():
    char = CharacterFactory()
    return char
