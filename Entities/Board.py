"""An entity representing the board on which the game will be played"""
from typing import Dict, Tuple

from Entities.Symbol import Symbol


class Board:
    """
    A board on which the game is played. Board sizes vary from 3x3 to 5x5.
    More improvements will come.
    Attributes:
        rows: the number of rows on the board
        columns: the number of columns on the board
        size_border: the border size of the board which would help the rendering.
    """
    rows: int
    columns: int
    size_border: Tuple[int, int]
    the_board: Dict[tuple[int, int], Symbol | None]


    def __init__(self, rows: int, columns: int) -> None:
        """Initializes the board with the dimensions rows and columns"""
        self.rows = rows
        self.columns = columns
        self.the_board = dict()
        for row in range(1, self.rows + 1):
            for col in range(1, self.columns + 1):
                self.the_board[(row, col)] = None

    def check_valid_move(self, row_coordinate: int, column_coordinate: int) -> bool:
        """Checks whether a player has made a valid move"""
        current_move = (row_coordinate, column_coordinate)
        if self.the_board[current_move] is None:
            return True
        else:
            return False

    def check_board_full(self) -> bool:
        """Checks whether the board is currently full or not"""
        for value in self.the_board.values():
            if value is None:
                return False
        return True
