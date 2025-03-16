"""An abstract class that defines a game repository where the state of the game, board and players
are stored."""
from __future__ import annotations

from abc import ABC, abstractmethod

from Entities import Game


class GameRepository(ABC):
    """Represents the state of the game. Its concrete implementation can be found within the
    infrastructure layer and communicates with the interactors to manage the state of a game."""

    @abstractmethod
    def save_game(self, game: Game) -> None:
        """Stores the state of game -newly created or currently running"""
        pass

    @abstractmethod
    def find_game(self, game_id: str | int) -> Game:
        """returns a game from the repository"""
        pass

    @abstractmethod
    def delete_game(self, game_id: str | int) -> None:
        """Deletes a game from the game repository."""
