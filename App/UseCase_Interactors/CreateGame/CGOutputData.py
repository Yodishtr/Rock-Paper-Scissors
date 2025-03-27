"""An output data class to represent the info from interactor back to the interface layer"""
from typing import Dict, Tuple

from Entities import Symbol


class CGOutputData:
    """Output data from interactor."""

    def __init__(self, board_map: Dict[Tuple[int, int], Symbol], player1name: str, player2name: str,
                 player1type: str, player2type: str, player1sym: Symbol, player2sym: Symbol,
                 game_id: float) -> None:
        self.board_map = board_map
        self.player1name = player1name
        self.player1Sym = player1sym
        self.player2name = player2name
        self.player2Sym = player2sym
        self.player1type = player1type
        self.player2type = player2type
        self.game_id = game_id
