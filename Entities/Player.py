"""An entity representing a Player in the game."""
from Entities.Board import Board
from Entities.Symbol import Symbol


class Player:
    """
    A player who is able to play the game.
    Attributes:
        name: the name of the player
        symbol: the symbol of the player
    """
    name: str
    symbol: Symbol

    def __init__(self, name: str, symbol: Symbol ):
        self.name = name
        self.symbol = symbol

    #make a use case for making moves by a human player and ai player
