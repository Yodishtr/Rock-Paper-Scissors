"""An entity representing the player being a human."""
from Entities import Symbol
from Entities.Player import Player


class HumanPlayer(Player):
    """A Player object being a human playing the game. """

    def __init__(self, name: str, symbol: Symbol):
        Player.__init__(name, symbol)
        self.type = "human"
