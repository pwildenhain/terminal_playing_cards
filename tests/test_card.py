"""Test the Card class"""

import pytest
from TerminalPlayingCards.card import Card


def test_card_str_value():
    """Ensure the proper string value of given the card"""
    ace_spades = Card("A", "spades")
    ace_spades_string = (
        "\x1b[47m\x1b[30m\n"
        "A          \n"
        "♠          \n"
        "           \n"
        "     ♠     \n"
        "           \n"
        "          ♠\n"
        "          A"
    )
    queen_hearts = Card("Q", "hearts")
    queen_hearts_string = (
        "\x1b[47m\x1b[31m\n"
        "Q          \n"
        "♥          \n"
        "           \n"
        "     ♛     \n"
        "           \n"
        "          ♥\n"
        "          Q"
    )
    ten_clubs = Card("10", "clubs")
    ten_clubs_string = (
        "\x1b[47m\x1b[30m\n"
        "10 ♣     ♣  \n"
        "♣    ♣      \n"
        "  ♣     ♣   \n"
        "            \n"
        "  ♣     ♣   \n"
        "     ♣    ♣ \n"
        "  ♣     ♣ 10"
    )
    joker = Card("JK", "none")
    joker_string = (
        "\x1b[47m\x1b[30m\n"
        "JK          \n"
        "            \n"
        "            \n"
        "     👹      \n"
        "            \n"
        "            \n"
        "          JK"
    )
    assert str(ace_spades) == ace_spades_string
    assert str(queen_hearts) == queen_hearts_string
    assert str(ten_clubs) == ten_clubs_string
    assert str(joker) == joker_string


def test_hidden_card_str_value():
    """Make sure that a hidden prints differently"""
    hidden_string = (
        "\x1b[37m\x1b[100m\n"
        "||       ||\n"
        "||       ||\n"
        "||    🚲  ||\n"
        "||       ||\n"
        "||    🚲  ||\n"
        "||       ||\n"
        "||       ||"
    )
    ace_diamonds = Card("A", "diamonds", hidden=True)
    ten_spades = Card("10", "spades", hidden=True)
    queen_hearts = Card("Q", "hearts", hidden=True)
    joker = Card("JK", "none", hidden=True)

    assert str(ace_diamonds) == hidden_string
    assert str(ten_spades) == hidden_string
    assert str(queen_hearts) == hidden_string
    assert str(joker) == hidden_string


def test_card_value_equality():
    """
    Same cards values are equal and different cards values are not equal.
    Cards values are equal to a number.
    """
    five_diamonds_1 = Card("5", "diamonds", value=5)
    five_diamonds_2 = Card("5", "diamonds", value=5)
    six_diamonds = Card("6", "diamonds", value=6)
    assert five_diamonds_1 == five_diamonds_2
    assert five_diamonds_2 == 5
    assert five_diamonds_1 != six_diamonds
    assert six_diamonds != 5


def test_card_value_inequality():
    """Cards values can be compared against one another and numbers"""
    queen_clubs = Card("Q", "clubs", value=12)
    jack_hearts = Card("J", "hearts", value=11)
    jack_spades = Card("J", "spades", value=11)
    ten_diamonds = Card("10", "diamonds", value=10)
    assert queen_clubs > jack_hearts
    assert jack_hearts < 12
    assert jack_hearts >= jack_spades
    assert jack_spades <= 11
    assert jack_spades <= jack_hearts
    assert jack_hearts <= 11
    assert ten_diamonds < jack_hearts
    assert jack_hearts > 10


def test_simple_arithmetic_with_cards():
    """Add, subtract, multiply, and divide cards by each other and numbers"""
    two_clubs = Card("2", "clubs", value=2)
    king_spades = Card("K", "spades", value=10)
    assert two_clubs + king_spades == 12
    assert sum([two_clubs, king_spades]) == 12
    assert two_clubs + 2 == 4
    assert 4 + two_clubs == 6
    assert king_spades - two_clubs == 8
    assert 10 - king_spades == 0
    assert king_spades - 10 == 0


def test_card_property_getters():
    """Face and suit properties are able to be gotten"""
    six_diamonds = Card("6", "diamonds", 6)
    assert six_diamonds.face == "6"
    assert six_diamonds.suit == "diamonds"


def test_getting_a_card_layer():
    """Card object is properly indexed by __getitem__"""
    ten_hearts = Card("10", "hearts")
    actual_third_layer = ten_hearts[2]
    expected_third_layer = [" ", " ", "♥", " ", " ", " ", " ", " ", "♥", " ", " ", " "]
    assert actual_third_layer == expected_third_layer


def test_card_creation_case_insensitive():
    queen_clubs = Card("q", "CLUBS")
    assert queen_clubs.suit == "clubs"
    assert queen_clubs.face == "Q"


def test_card_throws_good_error_message():
    """Alert the user that the face/suit they asked for does not exist"""
    with pytest.raises(NotImplementedError):
        Card("fake face", "spades")
    with pytest.raises(NotImplementedError):
        Card("A", "fake suit")
