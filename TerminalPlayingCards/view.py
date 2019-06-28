"""Create class for a View of Card objects"""
# Disable this pylint rule because of a conflict with black
# See: github.com/python/black/issues/48
# pylint: disable=bad-continuation
# Ignore concerns about docstrings, since _all_ methods with docstrings
# are picked up by sphinx-autodoc
# pylint: disable=missing-docstring

from colorama import Style
from TerminalPlayingCards.utils import convert_layers_to_string


class View:
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

    def __len__(self):
        """Return the number of cards in the View"""
        return len(self.cards)

    def __getitem__(self, key):
        """Returns the specified Card from it's index in the View"""
        return self.cards[key]

    def __iter__(self):
        """Prepare the View for iteration"""
        self._index = 0
        self._max = len(self)
        return self

    def __next__(self):
        """Cycle through the View iterable"""
        if self._index < self._max:
            card = self.cards[self._index]
            self._index += 1
            return card
        raise StopIteration

    def _merge_horizontal(self) -> list:
        """Merge all cards in the View horizontally"""
        merged_grid = []
        spacing = [Style.RESET_ALL] + [" " for _ in range(self._spacing)]

        for layer in range(7):
            merged_layer = []
            for card in self:
                card_style = [card.get_style()]
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

    @staticmethod
    def _sort_by_value(cards: list, order: str) -> list:
        """Sort cards according to value. Use selection sort"""
        unsorted_cards = cards.copy()
        sorted_cards = []
        sort_fx = min if order == "asc" else max
        for _ in cards:
            smallest_card = sort_fx(unsorted_cards)
            unsorted_cards.remove(smallest_card)
            sorted_cards.append(smallest_card)
        return sorted_cards

    @staticmethod
    def _sort_by_suit(cards: list, order: list) -> list:
        """Sort cards according to suit"""
        unsorted_cards = cards.copy()
        sorted_cards = []
        for suit in order:
            cards_by_suit = [card for card in unsorted_cards if card.suit == suit]
            # Skip empty lists for suits not in cards
            if cards_by_suit == []:
                continue
            for card in cards_by_suit:
                sorted_cards.append(card)
                unsorted_cards.remove(card)

        # Tack on any remaining cards not specified in the order
        sorted_cards = (
            sorted_cards if not unsorted_cards else sorted_cards + unsorted_cards
        )

        return sorted_cards

    def sort(
        self, sort_order: list = None, value_order: str = None, suit_order: list = None
    ) -> None:
        """Sort the cards in the View"""
        # Set default arguments
        sort_order = ["value", "suit"] if not sort_order else sort_order
        suit_order = (
            ["clubs", "diamonds", "spades", "hearts", "none"]
            if not suit_order
            else suit_order
        )
        value_order = "asc" if not value_order else value_order

        for sort_option in sort_order:
            sort_fx = getattr(self, f"_sort_by_{sort_option}")
            order_params = locals().get(f"{sort_option}_order")
            self.cards = sort_fx(self.cards, order_params)
