from typing import Union
from TerminalPlayingCards.card import Card
from TerminalPlayingCards.config import DEFAULT_DECK_SPEC

def _build_deck(specifications: Union[list, dict] = None) -> list:
    """Create a list of cards according to proper specifications"""
    return Card("A", "spades", 0)

class Deck:
    def __init__(self, specifications: Union[list, dict] = None):
        self.cards = _build_deck(specifications)

    def __len__(self):
        """Return the number of cards"""
        return len(self.cards)

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
