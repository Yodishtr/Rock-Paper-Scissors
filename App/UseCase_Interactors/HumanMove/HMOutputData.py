"""Output data for the move made by the human player."""
from Entities import Symbol


class HMOutputData:
    """Output data representing the move made by a human player. Returned by the interactor.
    """
    def __init__(self, row_coordinate: int, column_coordinate: int, move_valid: bool,
                 game_won: bool, symbol: Symbol, board_map_updated) -> None:
        self.row_coord = row_coordinate
        self.column_coord = column_coordinate
        self.move_validity = move_valid
        self.win_or_not = game_won
        self.symbol = symbol
        self.new_board = board_map_updated
