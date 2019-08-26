"""Create class for a View of Card objects"""
# Disable this pylint rule because of a conflict with black
# See: github.com/python/black/issues/48
# pylint: disable=bad-continuation
# Ignore concerns about docstrings, since _all_ methods with docstrings
# are picked up by sphinx-autodoc
# pylint: disable=missing-docstring

from colorama import Style, Fore
from terminal_playing_cards.deck import Deck
from terminal_playing_cards.utils import convert_layers_to_string


class View(Deck):
    """View one or more playing cards in the terminal"""
    # No need to initialize Deck when View is created. Only looking to inherit
    # methods, not attributes
    # pylint: disable=super-init-not-called
    def __init__(self, cards: list, orientation: str = "horizontal", spacing: int = 2):
        self.cards = cards
        self._orientation = None
        self.orientation = orientation
        self._spacing = None
        self.spacing = spacing
    # pylint: enable=super-init-not-called

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
        if spacing > -11:
            self._spacing = spacing
        else:
            raise NotImplementedError(
                "The View class cannot have spacing less than -10"
            )

    def _merge_horizontal(self) -> list:
        """Merge all cards in the View horizontally"""
        merged_grid = []
        positive_spacing = [" " for _ in range(self._spacing)]

        for layer in range(7):
            merged_layer = []
            card_position = 0
            for card in self:
                prev_card = (
                    self[card_position - 1] if card_position != 0 else DummyCard()
                )
                # pylint: disable=protected-access
                card_style = [card._get_style()]
                # pylint: enable=protected-access
                card_layer = card_style + card[layer] + [Style.RESET_ALL]
                if self._spacing >= 0:
                    merged_layer += card_layer + positive_spacing
                else:
                    border = [Fore.BLACK, "|"] if card_position != 0 else []
                    prev_face_is_len_two = (
                        len(prev_card.face) == 2 and not prev_card.hidden
                    )
                    on_last_layer = layer == 6
                    negative_spacing = (
                        self._spacing
                        if not (prev_face_is_len_two)
                        or (prev_face_is_len_two and on_last_layer)
                        else self._spacing - 1
                    )
                    merged_layer = merged_layer[:negative_spacing] + border + card_layer
                    card_position += 1
            merged_grid.append(merged_layer)

        return merged_grid

    def _merge_vertical(self) -> list:
        """Merge all cards in the View vertically"""
        raise NotImplementedError(
            "Vertical orientation currently not implemented for the View class"
        )

    def __str__(self):
        """Make the view look like a collection of playing cards"""
        merge_fx = getattr(self, f"_merge_{self._orientation}")
        # Merge playing cards in desired direction
        merged_cards = merge_fx()
        return convert_layers_to_string(merged_cards)


# Dummy object used by View to determine how to merge cards
# pylint: disable=too-few-public-methods
class DummyCard:
    def __init__(self):
        self.face = " "
        self.hidden = False
# pylint: enable=too-few-public-methods
