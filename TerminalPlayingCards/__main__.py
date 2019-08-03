"""Playground for testing module"""

from TerminalPlayingCards import deck, view

MY_DECK = deck.Deck()

MY_DECK.sort(sort_order=["suit"])

SUITED_VIEWS = [
    view.View([MY_DECK.pop() for _ in range(13)], spacing=-5) for _ in range(4)
]

if __name__ == "__main__":
    for suit_view in SUITED_VIEWS:
        print(suit_view)
