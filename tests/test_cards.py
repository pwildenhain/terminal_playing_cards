"""Test the Card and Deck classes"""

from TerminalPlayingCards.cards import Card


def test_card_str_value():
    """Ensure the string value given the card"""
    ace_spades = Card("A", "spades", value=0)
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
    queen_hearts = Card("Q", "hearts", value=0)
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
    ten_clubs = Card("10", "clubs", value=0)
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
    assert str(ace_spades) == ace_spades_string
    assert str(queen_hearts) == queen_hearts_string
    assert str(ten_clubs) == ten_clubs_string


def test_card_value_equality():
    """Same cards values are equal and different cards values are not equal"""
    five_diamonds_1 = Card("5", "diamonds", value=5)
    five_diamonds_2 = Card("5", "diamonds", value=5)
    six_diamonds = Card("6", "diamonds", value=6)
    assert five_diamonds_1 == five_diamonds_2
    assert five_diamonds_1 != six_diamonds


def test_card_value_inequality():
    """Cards values can be compared against one another"""
    queen_clubs = Card("Q", "clubs", value=12)
    jack_hearts = Card("J", "hearts", value=11)
    jack_spades = Card("J", "spades", value=11)
    ten_diamonds = Card("10", "diamonds", value=10)
    assert queen_clubs > jack_hearts
    assert jack_hearts >= jack_spades
    assert jack_spades <= jack_hearts
    assert ten_diamonds < jack_hearts


def test_same_is_true_for_same_card():
    """Cards with same face and suit are equal. Value has nothing to do with it"""
    seven_spades_1 = Card("7", "spades", value=0)
    seven_spades_2 = Card("7", "spades", value=1)
    seven_hearts = Card("7", "hearts", value=0)
    assert seven_spades_1.same(seven_spades_2)
    assert not seven_spades_1.same(seven_hearts)


def test_simple_arithmetic_with_cards():
    two_clubs = Card("2", "clubs", value=2)
    king_spades = Card("K", "clubs", value=10)
    assert two_clubs + king_spades == 12
    assert king_spades - two_clubs == 8
    assert two_clubs * king_spades == 20
    assert king_spades / two_clubs == 5
