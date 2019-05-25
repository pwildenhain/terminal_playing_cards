"""Create Card and Deck classes as well as module variables for card printing"""

from functools import total_ordering
from colorama import init
from TerminalPlayingCards.config import SUIT_SYMBOL_DICT, CARD_FACE_DICT

# Change the color back to default after each print
# Prevents user input from being colored
init(autoreset=True)


@total_ordering
class Card:
    """A playing card in a standard deck"""

    def __init__(self, face: str, suit: str, value: float):
        self.face = face
        self.suit = suit
        self.value = value
        self.symbol = SUIT_SYMBOL_DICT.get(suit).get("symbol")
        self.style = SUIT_SYMBOL_DICT.get(suit).get("style")

    def _create_card_grid(self):
        """Create standard grid template for all playing cards"""
        card_grid = [[" " for _ in range(11)] for _ in range(7)]
        # Add extra space for ten's since the face is two characters instead of one
        if self.face == "10":
            for layer in range(1, 6):
                card_grid[layer].append(" ")

        card_grid[0][0] = self.face
        card_grid[1][0] = self.symbol
        # Picture will only be added for J, Q, K
        card_grid[3][5] = CARD_FACE_DICT.get(self.face).get("picture", " ")
        card_grid[5][10] = self.symbol
        card_grid[6][10] = self.face
        return card_grid

    def _plan_card_grid(self):
        """Fill out the card grid according to given symbol coordinates"""
        card_grid = self._create_card_grid()
        symbol_coords = CARD_FACE_DICT.get(self.face).get("coords")
        if not symbol_coords:
            return card_grid

        for layer, position in symbol_coords:
            card_grid[layer][position] = self.symbol

        return card_grid

    def __str__(self):
        """Make the card look like an actual playing card"""
        card_str = ""
        card_grid_plan = self._plan_card_grid()

        for layer in range(0, 7):
            card_str += "\n" + "".join(card_grid_plan[layer])

        return self.style + card_str

    def __eq__(self, other_card):
        """Compare value equality against another Card"""
        return self.value == other_card.value

    def __lt__(self, other_card):
        """Compare value inequality against another Card"""
        return self.value < other_card.value
    
    def __add__(self, other_card):
        """Add the value of Card with the value of another Card"""
        return self.value + other_card.value
    
    def __sub__(self, other_card):
        """Subtract the value of Card with the value of another Card"""
        return self.value - other_card.value
    
    def __mul__(self, other_card):
        """Mulitply the value of Card with the value of another Card"""
        return self.value * other_card.value

    def __truediv__(self, other_card):
        """Divide the value of Card with the value of another Card"""
        return self.value / other_card.value

    def same_face(self, other_card):
        """See if a Card has the same face as another Card"""
        return self.face == other_card.face
    
    def same_suit(self, other_card):
        """See if a Card has the same suit as another Card"""
        return self.suit == other_card.suit

    def same_face_and_suit(self, other_card):
        """See if a Card has the same face and suit as another Card"""
        return self.same_face(other_card) and self.same_suit(other_card)
    
