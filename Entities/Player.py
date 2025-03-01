"""An entity representing a Player in the game."""
from Entities.Board import Board


class Player:
    """
    A player who is able to play the game.
    Attributes:
        name: the name of the player
        symbol: the symbol of the player
    """
    name: str
    symbol: str

    def __init__(self, name: str, symbol: str ):
        self.name = name
        self.symbol = symbol

    def make_move(self, coordinates: int):
        """
        A players move
        :param coordinates: the coordinate on the board where the player is playing their symbol.
        :return: String
        """
        playing_field = Board.rows * Board.columns
        if (coordinates > playing_field) or (coordinates < playing_field):
            return "Invalid Move"
        if Board.the_board[coordinates] != "":
            return "This position is already occupied"
        else:
            Board.the_board[coordinates] = self.symbol
            return ("Player {} played at {} coordinates".format(self.name, coordinates))
