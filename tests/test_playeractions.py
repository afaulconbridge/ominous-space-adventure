from tpc.gamestate import GameState
from tpc.playeractions import (
    ActiveChooseBlue,
    ActiveChooseGreen,
    ActiveChooseOrange,
    ActiveChooseWhite,
    ActiveChooseYellow,
)


class TestPlayerActions:
    def test_blue_legal(self):
        gamestate = GameState.new_game()
        assert ActiveChooseBlue.is_legal(gamestate, gamestate.get_active_playerstate())

    def test_yellow_legal(self):
        gamestate = GameState.new_game()
        assert ActiveChooseYellow.is_legal(gamestate, gamestate.get_active_playerstate())

    def test_green_legal(self):
        gamestate = GameState.new_game()
        assert ActiveChooseGreen.is_legal(gamestate, gamestate.get_active_playerstate())

    def test_orange_legal(self):
        gamestate = GameState.new_game()
        assert ActiveChooseOrange.is_legal(gamestate, gamestate.get_active_playerstate())

    def test_white_legal(self):
        gamestate = GameState.new_game()
        assert ActiveChooseWhite.is_legal(gamestate, gamestate.get_active_playerstate())
