from tpc.gamestate import DiceColour, DiceLocation, GameState


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

        gamestate.pick_dice(DiceColour.BLUE)

        assert gamestate.dice.get_die_location(DiceColour.BLUE) == DiceLocation.SLOT_1

    def test_pick_yellow(self):
        gamestate = GameState.new_game()

        gamestate.pick_dice(DiceColour.YELLOW)

        assert gamestate.dice.get_die_location(DiceColour.YELLOW) == DiceLocation.SLOT_1

    def test_pick_green(self):
        gamestate = GameState.new_game()

        gamestate.pick_dice(DiceColour.GREEN)

        assert gamestate.dice.get_die_location(DiceColour.GREEN) == DiceLocation.SLOT_1

    def test_pick_orange(self):
        gamestate = GameState.new_game()

        gamestate.pick_dice(DiceColour.ORANGE)

        assert gamestate.dice.get_die_location(DiceColour.ORANGE) == DiceLocation.SLOT_1

    def test_pick_purple(self):
        gamestate = GameState.new_game()

        gamestate.pick_dice(DiceColour.PURPLE)

        assert gamestate.dice.get_die_location(DiceColour.PURPLE) == DiceLocation.SLOT_1

    def test_pick_white(self):
        gamestate = GameState.new_game()

        gamestate.pick_dice(DiceColour.WHITE)

        assert gamestate.dice.get_die_location(DiceColour.WHITE) == DiceLocation.SLOT_1
