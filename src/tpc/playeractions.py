from tpc.gamestate import DiceColour, DiceLocation, GameState, PlayerState


class PlayerActionBase:
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        return True

    def apply(self, gamestate: GameState, playerstate: PlayerState) -> None:
        pass


class ActivePlayerAction(PlayerActionBase):
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        has_empty_slot = (
            not gamestate.dice.get_dice_in_location(DiceLocation.SLOT_1)
            or not gamestate.dice.get_dice_in_location(DiceLocation.SLOT_2)
            or not gamestate.dice.get_dice_in_location(DiceLocation.SLOT_3)
        )
        return has_empty_slot and super().is_legal(gamestate, playerstate)


class ActiveChooseBlue(ActivePlayerAction):
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        return (
            super().is_legal(gamestate, playerstate)
            and gamestate.dice.get_die_location(DiceColour.BLUE) == DiceLocation.IN_PLAY
        )


class ActiveChooseYellow(ActivePlayerAction):
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        return (
            super().is_legal(gamestate, playerstate)
            and gamestate.dice.get_die_location(DiceColour.YELLOW) == DiceLocation.IN_PLAY
        )


class ActiveChooseGreen(ActivePlayerAction):
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        return (
            super().is_legal(gamestate, playerstate)
            and gamestate.dice.get_die_location(DiceColour.GREEN) == DiceLocation.IN_PLAY
        )


class ActiveChooseOrange(ActivePlayerAction):
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        return (
            super().is_legal(gamestate, playerstate)
            and gamestate.dice.get_die_location(DiceColour.ORANGE) == DiceLocation.IN_PLAY
        )


class ActiveChooseWhite(ActivePlayerAction):
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        return (
            super().is_legal(gamestate, playerstate)
            and gamestate.dice.get_die_location(DiceColour.WHITE) == DiceLocation.IN_PLAY
        )


class PassivePlayerAction(PlayerActionBase):
    @classmethod
    def is_legal(cls, gamestate: GameState, playerstate: PlayerState) -> bool:
        active_playerstate = gamestate.players[gamestate.activate_player]
        has_empty_slot = not active_playerstate.slot_1 or not active_playerstate.slot_2 or not active_playerstate.slot_3
        return not has_empty_slot and super().is_legal(gamestate, playerstate)
