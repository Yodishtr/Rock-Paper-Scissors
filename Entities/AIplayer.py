"""An entity representing the game AI against which a player can play against."""
from Entities import Board, Game, Symbol
from Entities.Player import Player


class AIPlayer(Player):
    """Player object representing the Computer AI."""

    def __init__(self, name: str, symbol: Symbol, strategy: str) -> None:
        self.name = name
        self.symbol = symbol
        self.strategy = strategy
        self.type = "Ai"

    def choose_move(self, game: Game):
        if self.strategy.lower() == "minimax":
            self.minimax_strategy(game)

        else:
            self.neural_net_strategy(game)



    def minimax_strategy(self, game: Game):
        # assigned values to end game conditions for the ai
        ai_win = 1
        ai_loss = -1
        draw = 0
        is_ai_turn = (game.current_player == self)


        check_current_state = game.check_winning_combo()
        check_board_full = game.board.check_board_full()
        if check_current_state == self.symbol:
            return 1
        elif check_board_full:
            return 0

        else:
            # implement a helper function instead






    def neural_net_strategy(self, game: Game):
        """Strategy involving a neural network"""
