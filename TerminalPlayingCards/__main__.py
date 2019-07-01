"""Playground for testing module"""

from TerminalPlayingCards import deck, view

MY_DECK = deck.Deck()

MY_HAND = view.View([MY_DECK.pop() for _ in range(5)])

if __name__ == "__main__":
    print(MY_HAND)
