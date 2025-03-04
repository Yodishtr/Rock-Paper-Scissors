"""An entity representing the Game being played by players or player and AI on a board
of their choosing"""
from Entities.Board import Board
from Entities.Player import Player
from Entities.Symbol import Symbol


class Game:
    """
    Finds whether the game can still carry on or if a winning combination has been found.
    """
    def __init__(self, player1: Player, player2: Player, board: Board) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_turn = 0

    def check_winning_combo(self) -> Symbol | None:
        # check rows for same symbol
        winning_length = self.board.rows
        for row in range(1, self.board.rows + 1):
            first_row_symbol = self.board.the_board[(row, 1)]
            count_rows = 1
            for col in range(2, self.board.rows + 1):
                if self.board.the_board[(row, col)] is None:
                    return None
                elif first_row_symbol == self.board.the_board[(row, col)]:
                    count_rows += 1

            if count_rows == winning_length:
                return first_row_symbol
            else:
                continue


        # check columns for same symbol
        for col in range(1, self.board.columns + 1):
            first_col_symbol = self.board.the_board[(1, col)]
            count_columns = 1
            for row in range(2, self.board.rows + 1):
                if self.board.the_board[(row, col)] is None:
                    return None
                elif first_col_symbol == self.board.the_board[(row, col)]:
                    count_columns += 1

            if count_columns == winning_length:
                return first_col_symbol
            else:
                continue

        # check left diagonal (from top left of board to bottom right)
        arr_of_tuples = []
        for i in range(2, self.board.rows + 1):
            arr_of_tuples.append((i, i))

        first_diag_symbol = self.board.the_board[(1, 1)]
        count_left_diag = 1
        for tups in arr_of_tuples:
            if self.board.the_board[tups] == first_diag_symbol:
                count_left_diag += 1
            elif self.board.the_board[tups] is None:
                return None

        if count_left_diag == winning_length:
            return first_diag_symbol


        # check right diagonal (from top right to bottom left)
        arr2_of_tuples = []
        sum_coordinates = self.board.rows + 1
        for i in range(1, self.board.rows + 1):
            current_row = sum_coordinates - i
            arr2_of_tuples.append((current_row, i))

        first_diag_symbol2 = self.board.the_board[arr2_of_tuples[0]]
        count_right_diag = 1
        for i in range(1, len(arr2_of_tuples)):
            if self.board.the_board[arr2_of_tuples[i]] is None:
                return None
            elif self.board.the_board[arr2_of_tuples[i]] == first_diag_symbol2:
                count_right_diag += 1

        if count_right_diag == winning_length:
            return first_diag_symbol2

        else:
            return None
