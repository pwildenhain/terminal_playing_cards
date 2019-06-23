"""Create class for a View of Card objects"""

from colorama import Style
from TerminalPlayingCards.utils import convert_layers_to_string


class View:
    """View one or more playing cards in the terminal"""

    def __init__(
        self, cards: list, merge_direction: str = "right", merge_padding: int = 2
    ):
        self.cards = cards
        self._merge_direction = None
        self.merge_direction = merge_direction
        self._merge_padding = None
        self.merge_padding = merge_padding

    @property
    def merge_direction(self):
        """Get the merge direction of the View"""
        return self._merge_direction

    @merge_direction.setter
    def merge_direction(self, direction: str):
        if direction in ["right", "left", "up", "down"]:
            self._merge_direction = direction
        else:
            raise NotImplementedError(f"The View class cannot merge cards {direction}")

    @property
    def merge_padding(self):
        "Get the amount of padding between cards in the View"
        return self._merge_padding

    @merge_padding.setter
    def merge_padding(self, padding: int):
        if padding > 0:
            self._merge_padding = padding
        else:
            raise NotImplementedError(
                "The View class cannot have merge padding less than zero"
            )

    def __len__(self) -> int:
        """Return the number of cards in the View"""
        return len(self.cards)

    def __getitem__(self, key: int) -> list:
        """Returns the specified Card from it's index in the View"""
        return self.cards[key]

    def __iter__(self):
        """Prepare the View for iteration"""
        self.index = 0
        self.max = len(self)
        return self

    def __next__(self):
        """Cycle through the View iterable"""
        if self.index < self.max:
            card = self.cards[self.index]
            self.index += 1
            return card
        else:
            raise StopIteration

    def _merge_right(self) -> list:
        """Merge all cards in the View to the right of each other"""
        merged_grid = []
        padding = [Style.RESET_ALL] + [" " for _ in range(self._merge_padding)]

        for layer in range(7):
            merged_layer = []
            for card in self:
                card_style = [card.get_style()]
                card_layer = card_style + card[layer] + padding
                merged_layer += card_layer
            merged_grid.append(merged_layer)

        return merged_grid

    def _merge_left(self) -> list:
        """Merge all cards in the View to the left of each other"""
        pass

    def _merge_up(self) -> list:
        """Merge all cards in the View over each other"""
        pass

    def _merge_down(self) -> list:
        """Merge all cards in the View on top of each other"""
        pass

    def __str__(self):
        """Make the view look like a collection of playing cards"""
        merge_fx = getattr(self, f"_merge_{self._merge_direction}")
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
