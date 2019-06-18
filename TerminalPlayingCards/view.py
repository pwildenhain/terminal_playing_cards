"""Create class for a View of Card objects"""

from TerminalPlayingCards.card import Card
from TerminalPlayingCards.utils import convert_layers_to_string
from colorama import Style

class View():
    """View one or more playing cards in the terminal"""
    def __init__(self, cards: list):
        self.cards = cards

    def __len__(self) -> int:
        """Return the number of cards in the View"""
        return len(self.cards)
    
    def _merge_right(self, padding: int = 2) -> list:
        """Merge all cards in the View to the right of each other"""
        merged_grid = []
        padding = [Style.RESET_ALL] + [" " for _ in range(padding)]
        
        for layer in range(7):
            merged_layer = []
            for card in range(len(self.cards)):
                card_style = [self.cards[card]._get_style()]
                card_layer = card_style + self.cards[card][layer] + padding
                merged_layer += card_layer
            merged_grid.append(merged_layer)

        return merged_grid

    def _merge_left(self, padding: int = 2) -> list:
        """Merge all cards in the View to the left of each other"""
        pass

    def _merge_up(self, padding: int = 2) -> list:
        """Merge all cards in the View over each other"""
        pass

    def _merge_down(self, padding: int = 2) -> list:
        """Merge all cards in the View on top of each other"""
        pass

    def _merge(self, direction: str, padding: int = 2) -> list:
        """Merge all the card in the View in the desired direction"""
        pass

    def __str__(self):
        """Make the view look like a collection of playing cards"""
        merged_cards = self._merge_right()
        return convert_layers_to_string(merged_cards)

    def sort(self, category: str = "value", order: str = "asc") -> None:
        """Sort the cards in the View according value, suit, or both"""
        pass