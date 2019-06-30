# Ignore concerns about docstrings, since _all_ methods with docstrings
# are picked up by sphinx-autodoc
# pylint: disable=missing-docstring
from colorama import Fore, Back

# Objects for the card module
SUIT_SYMBOL_DICT = {
    "diamonds": {"symbol": "♦", "style": Back.WHITE + Fore.RED},
    "hearts": {"symbol": "♥", "style": Back.WHITE + Fore.RED},
    "clubs": {"symbol": "♣", "style": Back.WHITE + Fore.BLACK},
    "spades": {"symbol": "♠", "style": Back.WHITE + Fore.BLACK},
    "none": {"symbol": " ", "style": Back.WHITE + Fore.BLACK},
}

CARD_FACE_DICT = {
    "A": {"coords": [(3, 5)]},
    "2": {"coords": [(0, 2), (6, 8)]},
    "3": {"coords": [(0, 5), (3, 5), (6, 5)]},
    "4": {"coords": [(0, 2), (0, 8), (6, 2), (6, 8)]},
    "5": {"coords": [(0, 2), (0, 8), (3, 5), (6, 2), (6, 8)]},
    "6": {"coords": [(0, 3), (3, 3), (6, 3), (0, 7), (3, 7), (6, 7)]},
    "7": {"coords": [(0, 3), (3, 3), (6, 3), (1, 5), (0, 7), (3, 7), (6, 7)]},
    "8": {"coords": [(0, 3), (3, 3), (6, 3), (1, 5), (5, 5), (0, 7), (3, 7), (6, 7)]},
    "9": {
        "coords": [
            (0, 2),
            (2, 2),
            (4, 2),
            (6, 2),
            (3, 5),
            (0, 8),
            (2, 8),
            (4, 8),
            (6, 8),
        ]
    },
    "10": {
        "coords": [
            (0, 2),
            (2, 2),
            (4, 2),
            (6, 2),
            (1, 5),
            (5, 5),
            (0, 8),
            (2, 8),
            (4, 8),
            (6, 8),
        ]
    },
    "J": {"picture": "⚔"},
    "Q": {"picture": "♛"},
    "K": {"picture": "♚"},
    "JK": {"picture": "👹"},
}

CARD_BACK_STYLE = Fore.WHITE + Back.LIGHTBLACK_EX
# Objects for the deck module
DEFAULT_DECK_SPEC = {
    "A": {"suit": {"clubs": 1, "diamonds": 1, "spades": 1, "hearts": 1}},
    "2": {"suit": {"clubs": 2, "diamonds": 2, "spades": 2, "hearts": 2}},
    "3": {"suit": {"clubs": 3, "diamonds": 3, "spades": 3, "hearts": 3}},
    "4": {"suit": {"clubs": 4, "diamonds": 4, "spades": 4, "hearts": 4}},
    "5": {"suit": {"clubs": 5, "diamonds": 5, "spades": 5, "hearts": 5}},
    "6": {"suit": {"clubs": 6, "diamonds": 6, "spades": 6, "hearts": 6}},
    "7": {"suit": {"clubs": 7, "diamonds": 7, "spades": 7, "hearts": 7}},
    "8": {"suit": {"clubs": 8, "diamonds": 8, "spades": 8, "hearts": 8}},
    "9": {"suit": {"clubs": 9, "diamonds": 9, "spades": 9, "hearts": 9}},
    "10": {"suit": {"clubs": 10, "diamonds": 10, "spades": 10, "hearts": 10}},
    "J": {"suit": {"clubs": 11, "diamonds": 11, "spades": 11, "hearts": 11}},
    "Q": {"suit": {"clubs": 12, "diamonds": 12, "spades": 12, "hearts": 12}},
    "K": {"suit": {"clubs": 13, "diamonds": 13, "spades": 13, "hearts": 13}},
}
