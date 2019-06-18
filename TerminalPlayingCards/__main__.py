"""Playground for testing module, this file will eventually be deleted"""

from pprint import pprint
from TerminalPlayingCards import card, view

MY_CARDS = [card.Card("A", "clubs", 0), card.Card("Q", "hearts", 0)]
MY_HAND = view.View(MY_CARDS)

if __name__ == "__main__":
    pprint(MY_HAND._merge_right())
    pprint(str(MY_HAND))
    print(MY_HAND)
