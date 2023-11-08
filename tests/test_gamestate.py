from tpc.gamestate import GameState


class TestGameState:

    def test_roll(self):
        gamestate = GameState.new_game()

        for colour in ("blue","yellow","green","orange","white"):
            assert colour in gamestate.dice
            assert gamestate.dice[colour] > 0
            assert gamestate.dice[colour] < 7

