"""Create a class for a deck of playing cards"""
# pylint: disable=bad-continuation

from typing import Union
from random import shuffle
from TerminalPlayingCards.card import Card
from TerminalPlayingCards.config import DEFAULT_DECK_SPEC


class Deck:
    """Deck of playing cards"""

    def __init__(self, specifications: Union[list, dict] = None, **kwargs: bool):
        spec_dict = (
            DEFAULT_DECK_SPEC
            if not specifications
            else self._get_spec_dict(specifications)
        )
        self.cards = self._build(spec_dict, **kwargs)
        # Attributes for __iter__ method
        self._index = None
        self._max = None

    @staticmethod
    def _get_spec_dict(specifications: Union[list, dict]):
        """Translate Deck build specifications into a dictionary"""
        # Early return if they are passing custom specifications
        if isinstance(specifications, dict):
            return specifications

        spec_dict = DEFAULT_DECK_SPEC

        if "ace_high" in specifications:
            for suit in spec_dict.get("A"):
                spec_dict["A"][suit] = 14

        if "face_cards_are_ten" in specifications:
            for face_card in ["J", "Q", "K"]:
                for suit in spec_dict.get(face_card):
                    spec_dict[face_card][suit] = 10

        return spec_dict

    @staticmethod
    def _build(specs_dict: dict, **kwargs: bool):
        """Build a deck of cards according to specifications"""
        return [
            Card(face, suit, value=specs_dict.get(face).get(suit), **kwargs)
            for face in specs_dict.keys()
            for suit in specs_dict.get(face).keys()
        ]

    def __len__(self):
        """Return the number of cards"""
        return len(self.cards)

    def __add__(self, other):
        """Add a Deck to another Deck"""
        self.cards += other.cards
        return self

    def __getitem__(self, key):
        """Returns the specified Card from it's index"""
        return self.cards[key]

    def __iter__(self):
        """Prepare for iteration"""
        self._index = 0
        self._max = len(self)
        return self

    def __next__(self):
        """Cycle through the iterable"""
        if self._index < self._max:
            card = self.cards[self._index]
            self._index += 1
            return card
        raise StopIteration

    def pop(self, index: int = 0):
        """Pop a card out of the Deck"""
        return self.cards.pop(index)

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

    def shuffle(self):
        """Shuffle the Deck in place"""
        shuffle(self.cards)
