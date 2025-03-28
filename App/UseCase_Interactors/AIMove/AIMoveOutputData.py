"""Output data class for Ai move use case interactor"""
from typing import Tuple


class AIOutputData:
    """An object encapsulating the results of the ai making the move from the interactor"""
    def __init__(self, move_made: Tuple[int, int], ai_win_or_lose: bool, draw_or_no: bool,
                 new_board_map) -> None:
        self.move_made = move_made
        self.ai_win_or_lose = ai_win_or_lose
        self.draw_or_no = draw_or_no
        self.updated_board = new_board_map
