import pytest

from cards_proj.src.cards.api import Card


@pytest.fixture
def card_object():
    return Card(
        'something',
        'Brian',
        'todo',
        123
    )
