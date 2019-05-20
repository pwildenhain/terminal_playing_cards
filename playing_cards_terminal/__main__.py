from playing_cards_terminal import cards, cards_config

suits = cards_config.SUIT_SYMBOL_DICT.keys()
# faces = card_config.CARD_FACE_DICT.keys()
faces = ["A"]
# Going to need a hand_grid variable for printing out the entire hand
# Will be interesting to think about how to combine cards, will have
# to switch to BACK.BLACK, add spacing (allow user to specify? allow to be negative?)
# and then will have to concatenate card layers with each other, before __str__ method
full_deck = [(face, suit) for face in faces for suit in suits]

if __name__ == "__main__":
    for face, suit in full_deck:
        print(cards.Card(face, suit))
