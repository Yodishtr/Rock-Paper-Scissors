"""Output Data class for Restart Game use case"""
from Entities import Player, Symbol


class RGOutputData:
    """Defines the class for the output data"""

    def __init__(self, board_map: dict[tuple[int, int], Symbol], game_id: float) -> None:
        """Initializes a RGOutput Data objec to be used by the interface adapters"""
        self.board_map = board_map
        self.game_id = game_id
