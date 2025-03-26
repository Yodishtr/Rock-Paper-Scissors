"""Concrete implementation of the game repository. Used a simple dictionary to do so but a databas
can be implemented instead later on."""
from Entities import Game
from Entities.GameRespository import GameRepository


class InMemoryRepository(GameRepository):
    """The game repository to store the game being played."""

    def __init__(self) -> None:
        """Initializes the in game dictionary."""
        self.game_dictionary = {}

    def save_game(self, game: Game) -> None:
        game_id = game.game_id
        self.game_dictionary[game_id] = game

    def find_game(self, game_id: float) -> Game:
        return self.game_dictionary[game_id]

    def delete_game(self, game_id: int) -> None:
        del self.game_dictionary[game_id]
