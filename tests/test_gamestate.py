from tpc.gamestate import DiceLocation, DiceColour, GameState


class TestGameState:
    def test_roll(self):
        gamestate = GameState.new_game()

        for colour in (DiceColour.BLUE, DiceColour.YELLOW, DiceColour.GREEN, DiceColour.ORANGE, DiceColour.WHITE):
            assert gamestate.dice.get_die_value(colour) > 0
            assert gamestate.dice.get_die_value(colour) < 7
            assert gamestate.dice.get_die(colour)[0] > 0
            assert gamestate.dice.get_die(colour)[0] < 7

            assert gamestate.dice.get_die_location(colour) == DiceLocation.IN_PLAY
            assert gamestate.dice.get_die(colour)[1] == DiceLocation.IN_PLAY

    def test_pick_blue(self):
        gamestate = GameState.new_game()

        gamestate = gamestate.pick_blue()

        assert gamestate.dice.get_die_location(DiceColour.BLUE) == DiceLocation.SLOT_1