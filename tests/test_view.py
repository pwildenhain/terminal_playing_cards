"""Test the View class"""

import pytest
from TerminalPlayingCards.view import View


@pytest.fixture
def two_card_view():
    """List of two Card objects"""
    from TerminalPlayingCards.card import Card

    cards = [Card("A", "clubs", 0), Card("Q", "hearts", 0)]
    return View(cards)


def test_view_str_value(two_card_view):
    """Ensure the proper string value of the given View"""
    two_card_view_string = (
        "\n"
        "\x1b[47m\x1b[30mA          \x1b[0m  \x1b[47m\x1b[31mQ          \x1b[0m  \n"
        "\x1b[47m\x1b[30m♣          \x1b[0m  \x1b[47m\x1b[31m♥          \x1b[0m  \n"
        "\x1b[47m\x1b[30m           \x1b[0m  \x1b[47m\x1b[31m           \x1b[0m  \n"
        "\x1b[47m\x1b[30m     ♣     \x1b[0m  \x1b[47m\x1b[31m     ♛     \x1b[0m  \n"
        "\x1b[47m\x1b[30m           \x1b[0m  \x1b[47m\x1b[31m           \x1b[0m  \n"
        "\x1b[47m\x1b[30m          ♣\x1b[0m  \x1b[47m\x1b[31m          ♥\x1b[0m  \n"
        "\x1b[47m\x1b[30m          A\x1b[0m  \x1b[47m\x1b[31m          Q\x1b[0m  "
    )
    assert two_card_view_string == str(two_card_view)


def test_view_has_correct_length(two_card_view):
    """The __len__ method returns the correct number of cards in the view"""
    assert len(two_card_view) == 2


def test_view_property_getters(two_card_view):
    """View merge direction and padding can be gotten"""
    two_card_view.merge_direction = "left"
    two_card_view.merge_padding = 3
    assert two_card_view.merge_direction == "left"
    assert two_card_view.merge_padding == 3
