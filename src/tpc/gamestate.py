import random
from enum import StrEnum, unique
from typing import Self

"""
Each dice has a currently rolled value, and a location.
Locations are are in play, on the silver platter, or in slots 1-3 of the current players board
"""


@unique
class DiceColour(StrEnum):
    BLUE = "blue"
    YELLOW = "yellow"
    GREEN = "green"
    ORANGE = "orange"
    WHITE = "white"


@unique
class DiceLocation(StrEnum):
    IN_PLAY = "in play"
    SILVER_PLATTER = "silver platter"
    SLOT_1 = "slot 1"
    SLOT_2 = "slot 2"
    SLOT_3 = "slot 3"


class DiceState:
    dice = dict[DiceColour, tuple[int, DiceLocation]]

    def __init__(self, dice: dict[DiceColour, tuple[int, DiceLocation]]):
        self.dice = dict(dice)

    def get_die(self, colour: DiceColour) -> tuple[int, DiceLocation]:
        return self.dice[colour]

    def get_die_value(self, colour: DiceColour) -> int:
        return self.dice[colour][0]

    def get_die_location(self, colour: DiceColour) -> DiceLocation:
        return self.dice[colour][1]

    def set_die(self, colour: DiceColour, value: int, location: DiceLocation) -> None:
        if value < 0 or value > 6:  # noqa: PLR2004
            msg = "Value must be 1-6 inclusive"
            raise ValueError(msg)
        self.dice[colour] = (value, location)

    def set_die_location(self, colour: DiceColour, location: DiceLocation) -> None:
        self.dice[colour] = (self.get_die_value(colour), location)

    @classmethod
    def rolled(cls) -> Self:
        return cls({*((c, (random.randint(1, 6), DiceLocation.IN_PLAY)) for c in DiceColour)})


class GameState:
    dice: DiceState

    def __init__(self, dice: DiceState):
        self.dice = dice

    @classmethod
    def new_game(cls) -> Self:
        return GameState(DiceState.rolled())

    def _low_dice_to_platter(self, upper_value: int) -> None:
        for colour in DiceColour:
            dice_value, dice_location = self.dice.get_die(colour)
            if dice_location == DiceLocation.IN_PLAY and dice_value < upper_value:
                self.dice.set_die_location(colour, DiceLocation.SILVER_PLATTER)

    def pick_dice(self, colour: DiceColour) -> None:
        if self.dice.get_die_location(colour) != DiceLocation.IN_PLAY:
            msg = "Dice must be in play to be picked"
            raise RuntimeError(msg)

        self.dice.set_die_location(colour, DiceLocation.SLOT_1)

        self._low_dice_to_platter(self.dice.get_die_value(colour))

        # TODO mark on player sheet
