import pytest

from cards_proj.src.cards.api import Card


class TestCardsobject:
    def test_card_should_create_cards_object_successfully(self):
        c = Card(
            'something',
            'Brian',
            'todo',
            123
        )

        assert c.summary == 'something'
        assert c.owner == 'Brian'
        assert c.state == 'todo'
        assert c.id == 123


    def test_from_dict_should_create_valid_card_object(self):
        c1 = Card(
            'something',
            'Brian',
            'todo',
            123
        )

        card_dict = {
            'summary': 'something',
            'owner': 'Brian',
            'state': 'todo',
            'id': 123
        }

        c2 = Card.from_dict(card_dict)

        assert c1 == c2


    def test_to_dict_should_return_valid_dict(self):
        c1 = Card(
            'something',
            'Brian',
            'todo',
            123
        )

        expected_dict = {
            'summary': 'something',
            'owner': 'Brian',
            'state': 'todo',
            'id': 123
        }

        c2 = c1.to_dict()

        assert c2 == expected_dict


    # def test_equality_should_fail(self):

    #     c1 = Card(
    #         'something',
    #         'Brian',
    #         'todo',
    #         123
    #     )
    #     c2 = Card(
    #         'something',
    #         'Bob',
    #         'todo',
    #         123
    #     )

    #     with pytest.raises(AssertionError):
    #         assert c1 == c2
