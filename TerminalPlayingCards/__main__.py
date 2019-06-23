"""Playground for testing module"""

from TerminalPlayingCards import card, view

MY_CARDS = [
    card.Card("2", "clubs", value=2),
    card.Card("Q", "hearts", value=12),
    card.Card("A", "clubs", value=1),
    card.Card("K", "spades", value=13),
    card.Card("2", "diamonds", value=2),
    card.Card("J", "spades", value=11),
]

MY_HAND = view.View(MY_CARDS)

if __name__ == "__main__":
    print(MY_HAND)
    # Implement tests for sort method(s)
    MY_HAND.sort()
    print(MY_HAND)
