"""A symbol entity representing the symbol assigned to a player playing the game."""
import enum


class Symbol(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"
