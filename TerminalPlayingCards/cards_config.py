""""All global configuration options for a the Card class"""

from colorama import Fore, Back

SUIT_SYMBOL_DICT = {
    "diamonds": {"symbol": "\u2666", "style": Back.WHITE + Fore.RED},
    "hearts": {"symbol": "\u2665", "style": Back.WHITE + Fore.RED},
    "clubs": {"symbol": "\u2663", "style": Back.WHITE + Fore.BLACK},
    "spades": {"symbol": "\u2660", "style": Back.WHITE + Fore.BLACK},
}

CARD_FACE_DICT = {
    "A": {"value": 11, "coords": [(2, 3)]},
    "2": {"value": 2, "coords": [(0, 3), (4, 3)]},
    "3": {"value": 3, "coords": [(0, 3), (2, 3), (4, 3)]},
    "4": {"value": 4, "coords": [()]},
    "5": {"value": 5, "coords": [()]},
    "6": {"value": 6, "coords": [()]},
    "7": {"value": 7, "coords": [()]},
    "8": {"value": 8, "coords": [()]},
    "9": {"value": 9, "coords": [()]},
    "10": {"value": 10, "coords": [()]},
    "J": {"value": 10, "picture": "\u2694"},
    "Q": {"value": 10, "picture": "\u265B"},
    "K": {"value": 10, "picture": "\u265A"},
}
