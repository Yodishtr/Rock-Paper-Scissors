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

    def __init__(self, name: str, symbol: Symbol, race: str):
        self.name = name
        if symbol.upper() == "X":
            self.symbol = Symbol(symbol)
        else:
            self.symbol = Symbol(symbol)
        self.race = race
