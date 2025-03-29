"""An entity representing the game AI against which a player can play against."""
from typing import Tuple

from Entities import Board, Game, Symbol
from Entities.Player import Player


class AIPlayer(Player):
    """Player object representing the Computer AI."""

    def __init__(self, name: str, symbol: Symbol, race: str, strategy: str) -> None:
        Player.__init__(name, symbol, race)
        self.strategy = strategy

    def choose_move(self, game: Game) -> Tuple[int, int]:
        """calls the appropriate method based on strategy chosen by the human player."""
        if self.strategy.lower() == "minimax":
            move = self.minimax_strategy(game)
            return move

        # else:
            # self.neural_net_strategy(game)

    def minimax_strategy(self, game: Game) -> Tuple[int, int]:
        """Minimax algorithm used to make the ai's move optimally."""
        is_maximizing_player = True
        game_board = game.board.the_board
        best_val = -1000
        best_move = (-1, -1)
        for coordinate in game_board:
            game_board[coordinate] = self.symbol
            move_val = self._minimax(game, is_maximizing_player)
            game_board[coordinate] = None
            if move_val > best_val:
                best_move = coordinate
                best_val = move_val
        return best_move

    def _minimax(self, game: Game, is_max_player: bool) -> int:
        """the minimax algorithm. returns int if there is a winner, otherwise returns
        the best move"""
        winning_symbol = game.check_winning_combo()
        if winning_symbol == self.symbol:
            return 10
        if (winning_symbol != self.symbol) and (winning_symbol is not None):
            return -10
        if (game.board.check_board_full()):
            return 0

        if (is_max_player):
            best_max = -1000
            board = game.board.the_board
            for coordinates in board:
                if board[coordinates] is None:
                    board[coordinates] = self.symbol
                    best_max = max(best_max, self._minimax(game, not(is_max_player)))
                    board[coordinates] = None
            return best_max
        else:
            best_min = 1000
            board = game.board.the_board
            if game.player1.race.lower() != "Ai":
                other_player_symbol = game.player1.symbol
            else:
                other_player_symbol = game.player2.symbol
            for coordinates in board:
                if board[coordinates] is None:
                    board[coordinates] = other_player_symbol
                    best_min = min(best_min, self._minimax(game, not(is_max_player)))
                    board[coordinates] = None
            return best_min

    # def neural_net_strategy(self, game: Game):
        # implement a neural network
