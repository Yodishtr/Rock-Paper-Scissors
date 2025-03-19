"""An entity representing the game AI against which a player can play against."""
from Entities import Symbol
from Entities.Player import Player


class AIPlayer(Player):
    """Player object representing the Computer AI."""

    def __init__(self, name: str, symbol: Symbol, strategy: str) -> None:
        self.name = name
        self.symbol = symbol
        self.strategy = strategy
        self.type = "Ai"
