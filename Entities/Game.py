"""An entity representing the Game being played by players or player and AI on a board
of their choosing"""
from Entities.Board import Board


class Game:
    """
    Finds whether the game can still carry on or if a winning combination has been found.
    """
    def __init__(self):
        """nothing to initialize here"""

    def winning_combo(self):
        """Verifies the board for any winning combination"""
        # verify the top row
        if Board.the_board[7] == Board.the_board[8] == Board.the_board[9]:
            winner = Board.the_board[7]
            return winner

        # verify the middle row
        elif Board.the_board[4] == Board.the_board[5] == Board.the_board[6]:
            winner = Board.the_board[4]
            return winner

        # verify the bottom row
        elif Board.the_board[1] == Board.the_board[2] == Board.the_board[3]:
            winner = Board.the_board[1]
            return winner

        # verify the first column
        elif Board.the_board[7] == Board.the_board[4] == Board.the_board[1]:
            winner = Board.the_board[7]
            return winner

        # verify the second column
        elif Board.the_board[8] == Board.the_board[5] == Board.the_board[2]:
            winner = Board.the_board[8]
            return winner

        # verify the third column
        elif Board.the_board[9] == Board.the_board[6] == Board.the_board[3]:
            winner = Board.the_board[9]
            return winner

        # verify diagonal from top left to bottom right
        elif Board.the_board[7] == Board.the_board[5] == Board.the_board[3]:
            winner = Board.the_board[7]
            return winner

        # verify the diagonal from top right to bottom left
        elif Board.the_board[9] == Board.the_board[5] == Board.the_board[1]:
            winner = Board.the_board[5]
            return winner

        else:
            return None
