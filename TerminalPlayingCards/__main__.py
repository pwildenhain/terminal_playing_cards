"""Playground for testing module, this file will eventually be deleted"""

from TerminalPlayingCards import cards, config

# SUITS = config.SUIT_SYMBOL_DICT.keys()
FACES = config.CARD_FACE_DICT.keys()
SUITS = ["hearts"]
# FACES = ["A"]

# Going to need a hand_grid variable for printing out the entire hand
# Will be interesting to think about how to combine cards, will have
# to switch to BACK.BLACK, add spacing (allow user to specify? allow to be negative?)
# and then will have to concatenate card layers with each other, before __str__ method
FULL_DECK = [(face, suit, 0) for face in FACES for suit in SUITS]

if __name__ == "__main__":
    for face, suit, value in FULL_DECK:
        print(cards.Card(face, suit, value))
