
import random
from collections import UserDict
from enum import StrEnum


class DiceColour(StrEnum):
    BLUE = "blue"
    YELLOW = "yellow"
    GREEN = "green"
    ORANGE = "orange"
    WHITE = "white"


class DiceState(UserDict[DiceColour,int]):
    def __setitem__(self, key:DiceColour, value:int):
        if value < 0 or value > 6:  # noqa: PLR2004
            msg = "Value must be 1-6 inclusive"
            raise ValueError(msg)
        super().__setitem__(key, value)

    @classmethod
    def rolled(cls) -> "DiceState":
        return cls({*((c,random.randint(1,6)) for c in DiceColour)})

class GameState:
    dice : DiceState

    def __init__(self, dice:DiceState):
        self.dice = dice

    @classmethod
    def new_game(cls) -> "GameState":
        return GameState(DiceState.rolled())
