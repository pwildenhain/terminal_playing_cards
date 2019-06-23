"""Test the View class"""

import pytest
from TerminalPlayingCards.view import View


@pytest.fixture
def two_card_view():
    """List of two Card objects"""
    from TerminalPlayingCards.card import Card

    cards = [Card("A", "clubs", 0), Card("Q", "hearts", 0)]
    return View(cards)


@pytest.fixture
def five_card_view():
    from TerminalPlayingCards.card import Card

    cards = [
        Card("2", "clubs", value=2),
        Card("Q", "hearts", value=12),
        Card("A", "clubs", value=1),
        Card("K", "spades", value=13),
        Card("2", "diamonds", value=2),
        Card("J", "spades", value=11),
    ]
    return View(cards)


@pytest.fixture
def five_card_view_sorted():
    from TerminalPlayingCards.card import Card

    cards = [
        Card("A", "clubs", value=1),
        Card("2", "clubs", value=2),
        Card("2", "diamonds", value=2),
        Card("J", "spades", value=11),
        Card("K", "spades", value=13),
        Card("Q", "hearts", value=12),
    ]
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


def test_view_default_sort(five_card_view, five_card_view_sorted):
    five_card_view.sort()
    for card in range(5):
        assert five_card_view[card] == five_card_view_sorted[card]
        assert five_card_view[card].suit == five_card_view_sorted[card].suit


def test_view_sort_by_value(five_card_view, five_card_view_sorted):
    five_card_view.sort(sort_order=["value"], value_order="desc")
    five_card_view_sorted.sort(sort_order=["value"], value_order="desc")
    for card in range(5):
        assert five_card_view[card] == five_card_view_sorted[card]


def test_view_sort_by_suit(five_card_view, five_card_view_sorted):
    suit_order = ["hearts", "spades", "diamonds", "clubs"]
    five_card_view.sort(sort_order=["suit"], suit_order=suit_order)
    five_card_view_sorted.sort(sort_order=["suit"], suit_order=suit_order)
    for card in range(5):
        assert five_card_view[card].suit == five_card_view_sorted[card].suit


def test_view_sort_by_only_two_suit(five_card_view, five_card_view_sorted):
    suit_order = ["diamonds", "spades"]
    five_card_view.sort(sort_order=["suit"], suit_order=suit_order)
    five_card_view_sorted.sort(sort_order=["suit"], suit_order=suit_order)
    for card in range(5):
        if five_card_view[card].suit in ["diamonds", "spades"]:
            assert five_card_view[card].suit == five_card_view_sorted[card].suit
        else:
            continue
