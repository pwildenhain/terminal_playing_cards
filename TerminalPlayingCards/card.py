"""Create class for representing and printing a playing card"""
# Ignore concerns about docstrings, since _all_ methods with docstrings
# are picked up by sphinx-autodoc
# pylint: disable=missing-docstring
# pylint: disable=bad-continuation
from functools import total_ordering
from colorama import init
from TerminalPlayingCards.utils import convert_layers_to_string
from TerminalPlayingCards.config import (
    SUIT_SYMBOL_DICT,
    CARD_FACE_DICT,
    CARD_BACK_STYLE,
)

# Change the color back to default after each print
# Prevents user input from being colored
init(autoreset=True)


@total_ordering
class Card:
    """A playing card in a standard deck"""

    def __init__(
        self,
        face: str,
        suit: str,
        value: int = 0,
        hidden: bool = False,
        picture: bool = True,
    ):
        self._face = None
        self.face = face
        self._suit = None
        self.suit = suit
        self.value = value
        self.hidden = hidden
        self.picture = picture
        self.symbol = SUIT_SYMBOL_DICT.get(suit.lower()).get("symbol")

    @property
    def face(self):
        """Get face property of the Card"""
        return self._face

    @face.setter
    def face(self, value):
        value = value.upper()
        if value in CARD_FACE_DICT.keys():
            self._face = value
        else:
            raise NotImplementedError(f"'{value}' is not a valid face for a Card")

    @property
    def suit(self):
        """Get suit property of the Card"""
        return self._suit

    @suit.setter
    def suit(self, value):
        value = value.lower()
        if value in SUIT_SYMBOL_DICT.keys():
            self._suit = value
        else:
            raise NotImplementedError(f"'{value}' is not a valid suit for a Card")

    def _create_card_grid(self) -> list:
        """Create standard empty grid template for all playing cards"""
        card_grid = [[" " for _ in range(11)] for _ in range(7)]
        # Add extra space if the face is two characters instead of one
        if len(self.face) > 1 and not self.hidden:
            for layer in range(1, 6):
                card_grid[layer].append(" ")

        return card_grid

    def _populate_corners_and_center(self, card_grid: list) -> list:
        """Populate the corner with face and suit and the center with a picture for face cards"""
        card_grid[0][0] = self.face
        card_grid[1][0] = self.symbol
        if self.picture:
            card_grid[3][5] = CARD_FACE_DICT.get(self.face).get("picture", " ")
        card_grid[5][10] = self.symbol
        card_grid[6][10] = self.face
        return card_grid

    @staticmethod
    def _populate_back_of_card(card_grid: list) -> list:
        """Populate the card grid with a design for the back of the card"""
        for layer in range(7):
            for position in [0, 1, 9, 10]:
                card_grid[layer][position] = "|"

        card_grid[2][6] = "🚲"
        card_grid[4][6] = "🚲"

        return card_grid

    def _plan_card_grid(self) -> list:
        """Fill out the card grid according to given symbol coordinates"""
        card_grid = self._create_card_grid()

        if self.hidden:
            return self._populate_back_of_card(card_grid)

        card_grid = self._populate_corners_and_center(card_grid)
        symbol_coords = CARD_FACE_DICT.get(self.face).get("coords")

        if not symbol_coords:
            return card_grid

        for layer, position in symbol_coords:
            card_grid[layer][position] = self.symbol

        return card_grid

    def get_style(self) -> str:
        """Retrive the colorama codes for a card style"""
        return (
            SUIT_SYMBOL_DICT.get(self.suit).get("style")
            if not self.hidden
            else CARD_BACK_STYLE
        )

    def __str__(self):
        """Make the card look like an actual playing card"""
        card_grid_plan = self._plan_card_grid()
        card_str = convert_layers_to_string(card_grid_plan)

        return self.get_style() + card_str

    def __repr__(self):
        """Return code used to create the Card instance"""
        return f"Card('{self.face}', '{self.suit}', value={self.value}, hidden={self.hidden}, picture={self.picture})"

    def __getitem__(self, key):
        """Returns the specified layer of the Card from indexing"""
        return self._plan_card_grid()[key]

    def __eq__(self, other):
        """Compare value equality against another Card or number"""
        try:
            result = self.value == other.value
        except AttributeError:
            result = self.value == other
        return result

    def __lt__(self, other):
        """Compare value inequality against another Card or number"""
        try:
            result = self.value < other.value
        except AttributeError:
            result = self.value < other
        return result

    def __add__(self, other):
        """Add the value of Card with the value of another Card or number"""
        try:
            result = self.value + other.value
        except AttributeError:
            result = self.value + other
        return result

    def __radd__(self, other):
        """Add the value of Card with the value of another Card or number"""
        try:
            result = other.value + self.value
        except AttributeError:
            result = other + self.value
        return result

    def __sub__(self, other):
        """Subtract the value of Card with the value of another Card or number"""
        try:
            result = self.value - other.value
        except AttributeError:
            result = self.value - other
        return result

    def __rsub__(self, other):
        """Subtract the value of Card with the value of another Card or number"""
        try:
            result = other.value - self.value
        except AttributeError:
            result = other - self.value
        return result
