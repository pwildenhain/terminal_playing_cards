"""Playground for testing module, this file will eventually be deleted"""

from TerminalPlayingCards import card, view, config
from colorama import init, Fore, Back
from pprint import pprint

mycards = [card.Card("A", "clubs", 0), card.Card("Q", "hearts", 0)]
myhand = view.View(mycards)

if __name__ == "__main__":
    pprint(myhand._merge_right())
    pprint(str(myhand))
    print(myhand)
