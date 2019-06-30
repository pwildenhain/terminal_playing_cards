"""Playground for testing module"""

from TerminalPlayingCards import card, view

MY_CARDS = [
    card.Card("2", "clubs"),
    card.Card("Q", "hearts"),
    card.Card("A", "clubs"),
    card.Card("K", "spades"),
    card.Card("2", "diamonds"),
    card.Card("J", "spades"),
]

MY_HAND = view.View(MY_CARDS)

if __name__ == "__main__":
    print(MY_HAND)
    # Implement tests for sort method(s)
    MY_HAND.sort()
    print(MY_HAND)
