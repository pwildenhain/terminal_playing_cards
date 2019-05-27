"""Playground for testing module, this file will eventually be deleted"""

from TerminalPlayingCards import card, config
from colorama import init, Fore, Back

# Back.LIGHTBLACK_EX

# SUITS = config.SUIT_SYMBOL_DICT.keys()
# FACES = config.CARD_FACE_DICT.keys()
SUITS = ["none"]
FACES = ["JK"]

# Going to need a hand_grid variable for printing out the entire hand
# Will be interesting to think about how to combine cards, will have
# to switch to BACK.BLACK, add spacing (allow user to specify? allow to be negative?)
# and then will have to concatenate card layers with each other, before __str__ method
FULL_DECK = [(face, suit, 0) for face in FACES for suit in SUITS]

if __name__ == "__main__":
    # for face, suit, value in FULL_DECK:
    #    print(card.Card(face, suit, value))
    string = (
        "||       ||\n"
        "||       ||\n"
        "||   🚲   ||\n"
        "||       ||\n"
        "||   🚲   ||\n"
        "||       ||\n"
        "||       ||"
    )

    print(Fore.WHITE + Back.LIGHTBLACK_EX + string)
