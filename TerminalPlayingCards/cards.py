"""Create Card and Deck classes as well as module variables for card printing"""

from colorama import init
from TerminalPlayingCards.config import SUIT_SYMBOL_DICT, CARD_FACE_DICT

# Change the color back to default after each print
# Prevents user input from being colored
init(autoreset=True)


class Card:
    """A playing card in a standard deck"""

    def __init__(self, face: str, suit: str, value: float):
        self.face = face
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
