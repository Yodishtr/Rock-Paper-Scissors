"""Input Data for restart game use case"""


class RGInputData:
    """Defines the input data to restart a game"""
    def __init__(self, game_id: float) -> None:
        self.game_id = game_id
