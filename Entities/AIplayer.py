"""An entity representing the game AI against which a player can play against."""
from typing import Tuple

from Entities import Board, Game, Symbol
from Entities.Player import Player


class AIPlayer(Player):
    """Player object representing the Computer AI."""

    def __init__(self, name: str, symbol: Symbol, race: str, strategy: str) -> None:
        super().__init__(name, symbol, race)
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

        # Only try empty coordinates
        for coordinate in game_board:
            if game_board[coordinate] is None:
                # Temporarily place this AI's symbol
                game_board[coordinate] = self.symbol

                # Evaluate how good that move is using the minimax algorithm
                move_val = self._minimax(game, not is_maximizing_player)

                # Reset
                game_board[coordinate] = None

                # Update the best move if this is better
                if move_val > best_val:
                    best_val = move_val
                    best_move = coordinate

        return best_move

    def _minimax(self, game: Game, is_max_player: bool) -> int:
        """
        The minimax recursive function.
        Returns +10 if AI can force a win, -10 if the opponent can force a win,
        or 0 for a draw / no forced win.
        """
        # Check if the game is already won/drawn
        winning_symbol = game.check_winning_combo()
        if winning_symbol == self.symbol:
            return 10
        elif (winning_symbol is not None) and (winning_symbol != self.symbol):
            return -10
        elif game.board.check_board_full():
            return 0

        board = game.board.the_board

        if is_max_player:
            # Maximizing the AI's advantage
            best_score = -1000
            for coordinate in board:
                if board[coordinate] is None:
                    # AI places its symbol to test
                    board[coordinate] = self.symbol
                    score = self._minimax(game, not is_max_player)
                    board[coordinate] = None
                    best_score = max(best_score, score)
            return best_score

        else:
            # Minimizing the human's advantage
            best_score = 1000

            # Figure out which symbol is the opponent’s
            if game.player1.race.lower() != "ai":
                opponent_symbol = game.player1.symbol
            else:
                opponent_symbol = game.player2.symbol

            for coordinate in board:
                if board[coordinate] is None:
                    board[coordinate] = opponent_symbol
                    score = self._minimax(game, not is_max_player)
                    board[coordinate] = None
                    best_score = min(best_score, score)
            return best_score

    # def neural_net_strategy(self, game: Game):
        # implement a neural network
