import random
from enum import StrEnum, unique
from typing import Iterable, Optional, Self

import immutables

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
    PURPLE = "purple"
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

    def get_dice_in_location(self, location: DiceLocation) -> tuple[DiceColour, ...]:
        return tuple(c for c in DiceColour if self.get_die_location(c) == location)

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


def first_falsy(iterable: Iterable):
    for i, j in enumerate(iterable):
        if not j:
            return i


class PlayerState:
    greens: list[bool]
    oranges: list[Optional[int]]
    purples: list[Optional[int]]

    def __init__(self):
        self.greens = [False for _ in range(11)]
        self.oranges = [None for _ in range(11)]
        self.purples = [None for _ in range(11)]

    _green_score = (1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 65)
    _green_mins = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6)
    _orange_multipliers = (1, 1, 1, 2, 1, 12, 1, 2, 1, 3)

    def record_dice(self, colour: DiceColour, value: int):
        match colour:
            case DiceColour.YELLOW:
                # TODO implement
                pass

            case DiceColour.BLUE:
                # TODO implement
                pass

            case DiceColour.GREEN:
                slot = first_falsy(self.greens)
                if not value >= self._green_mins[slot]:
                    msg = "Green value does not exceed minimum"
                    raise RuntimeError(msg)
                self.greens[slot] = True

            case DiceColour.ORANGE:
                slot = first_falsy(self.oranges)
                self.oranges[slot] = value

            case DiceColour.PURPLE:
                slot = first_falsy(self.purples)
                if slot > 0 and self.purples[slot - 1] != 6 and self.purples[slot - 1] >= value:  # noqa: PLR2004
                    msg = "Purple value is invalid"
                    raise RuntimeError(msg)
                self.purples[slot]

            case DiceColour.WHITE:
                # TODO implement
                pass

    def score(self) -> int:
        return (
            self._score_yellow()
            + self._score_blue()
            + self._score_green()
            + self._score_orange()
            + self._score_purple()
        )

    def _score_yellow(self) -> int:
        # TODO implement
        return 0

    def _score_blue(self) -> int:
        # TODO implement
        return 0

    def _score_green(self) -> int:
        # zip the boxes filled with the score for filling N boxes
        # mulitply - unticked boxes will be zeroed
        # max - get the highest ticked box
        return max(i * j for i, j in zip(self._green_score, self.greens))

    def _score_orange(self) -> int:
        # some spaces have a score multiplier
        # others multiply by 1 to keep value
        return sum(i * j for i, j in zip(self._orange_multipliers, self.oranges))

    def _score_purple(self) -> int:
        return sum(self.purples)


class GameState:
    dice: DiceState
    players: tuple[PlayerState]
    active_player: int = 0

    def __init__(self, dice: DiceState, no_players: int):
        self.dice = dice
        self.players = tuple(PlayerState() for _ in range(no_players))

    @classmethod
    def new_game(cls, no_players=4) -> Self:
        return GameState(DiceState.rolled(), no_players=no_players)

    def get_active_playerstate(self) -> PlayerState:
        return self.players[self.active_player]

    def _low_dice_to_platter(self, upper_value: int) -> None:
        for colour in DiceColour:
            dice_value, dice_location = self.dice.get_die(colour)
            if dice_location == DiceLocation.IN_PLAY and dice_value < upper_value:
                self.dice.set_die_location(colour, DiceLocation.SILVER_PLATTER)

    def pick_dice(self, colour: DiceColour) -> None:
        value, location = self.dice.get_die(colour)
        if location != DiceLocation.IN_PLAY:
            msg = "Dice must be in play to be picked"
            raise RuntimeError(msg)

        # decide which slot to put it in
        if not self.dice.get_dice_in_location(DiceLocation.SLOT_1):
            self.dice.set_die_location(colour, DiceLocation.SLOT_1)
        elif not self.dice.get_dice_in_location(DiceLocation.SLOT_2):
            self.dice.set_die_location(colour, DiceLocation.SLOT_2)
        elif not self.dice.get_dice_in_location(DiceLocation.SLOT_3):
            self.dice.set_die_location(colour, DiceLocation.SLOT_3)
        else:
            msg = "Unable to take dice, slots full"
            raise RuntimeError(msg)

        self._low_dice_to_platter(value)

        self.get_active_playerstate().record_dice(colour, value)
