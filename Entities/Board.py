"""An entity representing the board on which the game will be played"""
from typing import Dict, Tuple


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
    the_board: Dict[int, str]


    def __init__(self, rows: int, columns: int):
        """Initializes the board with the dimensions rows and columns"""
        self.rows = rows
        self.columns = columns
        self.size_border = (rows, columns)
        self.the_board = dict()
        board_size = self.rows * self.columns
        for num in range(1, board_size + 1):
            self.the_board[num] = ""
