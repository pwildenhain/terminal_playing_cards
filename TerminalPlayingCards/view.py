"""Create class for a View of Card objects"""
# Disable this pylint rule because of a conflict with black
# See: github.com/python/black/issues/48
# pylint: disable=bad-continuation
# Ignore concerns about docstrings, since _all_ methods with docstrings
# are picked up by sphinx-autodoc
# pylint: disable=missing-docstring

from colorama import Style
from TerminalPlayingCards.deck import Deck
from TerminalPlayingCards.utils import convert_layers_to_string


class View(Deck):
    """View one or more playing cards in the terminal"""

    def __init__(self, cards: list, orientation: str = "horizontal", spacing: int = 2):
        self.cards = cards
        self._orientation = None
        self.orientation = orientation
        self._spacing = None
        self.spacing = spacing
        # Attributes for __iter__ method
        self._index = None
        self._max = None

    @property
    def orientation(self):
        """Get the orientation of the View"""
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        if orientation in ["horizontal", "vertical"]:
            self._orientation = orientation
        else:
            raise NotImplementedError(
                f"The View class cannot place cards {orientation}ly"
            )

    @property
    def spacing(self):
        "Get the amount of spacing between cards in the View"
        return self._spacing

    @spacing.setter
    def spacing(self, spacing):
        if spacing > 0:
            self._spacing = spacing
        else:
            raise NotImplementedError(
                "The View class cannot have spacing less than zero"
            )

    def _merge_horizontal(self) -> list:
        """Merge all cards in the View horizontally"""
        merged_grid = []
        spacing = [Style.RESET_ALL] + [" " for _ in range(self._spacing)]

        for layer in range(7):
            merged_layer = []
            for card in self:
                # pylint: disable=protected-access
                card_style = [card._get_style()]
                # pylint: enable=protected-access
                card_layer = card_style + card[layer] + spacing
                merged_layer += card_layer
            merged_grid.append(merged_layer)

        return merged_grid

    def _merge_vertical(self) -> list:
        """Merge all cards in the View vertically"""
        raise NotImplementedError(
            "Vertical orientation is not implemented for the View class"
        )

    def __str__(self):
        """Make the view look like a collection of playing cards"""
        merge_fx = getattr(self, f"_merge_{self._orientation}")
        # Merge playing cards in desired direction
        merged_cards = merge_fx()
        return convert_layers_to_string(merged_cards)
