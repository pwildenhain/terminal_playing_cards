"""Create a class for a deck of playing cards"""
# See terminal_playing_cards/view.py for why these are disabled
# pylint: disable=missing-docstring
# pylint: disable=bad-continuation

from typing import Union
from random import shuffle
from terminal_playing_cards.card import Card
from terminal_playing_cards.config import DEFAULT_DECK_SPEC


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
        """Translates Deck build specifications into a dictionary."""
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
        """Builds a deck of cards according to specifications."""
        return [
            Card(face, suit, value=specs_dict.get(face).get(suit), **kwargs)
            for face in specs_dict.keys()
            for suit in specs_dict.get(face).keys()
        ]

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        """Add a Deck, View or Cards to another Deck/View"""
        try:
            self.cards += other.cards
        except AttributeError:
            is_a_card = [isinstance(card, Card) for card in other]
            if all(is_a_card):
                self.cards += other
            else:
                raise NotImplementedError(
                    "Only a Deck/View, or list of Cards can be added to this class"
                )
        return self

    def __getitem__(self, key):
        return self.cards[key]

    def __iter__(self):
        self._index = 0
        self._max = len(self)
        return self

    def __next__(self):
        if self._index < self._max:
            card = self.cards[self._index]
            self._index += 1
            return card
        raise StopIteration

    def pop(self, index: int = 0) -> Card:
        """Pops a card out of the Deck.

        Works just like the list.pop() method on a collection of Cards.

        Args:
            index: The index in the list at which to pop
                out a Card. Defaults to 0

        Returns:
            A Card object
        """
        return self.cards.pop(index)

    @staticmethod
    def _sort_by_value(cards: list, order: str) -> list:
        """Sorts cards according to value. Uses selection sort"""
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
        """Sorts cards according to given suit order"""
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
        """Sort a collection of Cards.

        Sort a collection of Cards in place according to a given sort order.
        Defaults to sorting by Card value ascending and Card suit by
        clubs, diamonds, spades, and then hearts.

        Args:
            sort_order: Specify whether to sort by value, suit, or
                both. If both are provided, it will perform the sort operation
                in that order. Defaults to value then suit
            value_order: Specify how to sort by value. Available options
                are asc and desc. Defaults to asc
            suit_order: Specify how to sort by suit. Available options
                are clubs, diamonds, spades, and/or hearts. Defaults to
                clubs, diamons, spades, and then hearts.

        Returns:
            None. Sorts the collection of Cards in place.
            For example:

            from terminal_playing_cards import Card, View

            my_hand = View([
                Card("2", "hearts", value=2)
                Card("A", "spades", value=1),
            ])

            my_hand.sort()
            my_hand.sort(sort_order=["value"], value_order="desc")
        """
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

    def shuffle(self) -> None:
        """Shuffles the Cards in place."""
        shuffle(self.cards)
