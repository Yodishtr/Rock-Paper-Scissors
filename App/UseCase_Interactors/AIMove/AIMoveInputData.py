"""Input Data class for the Ai player making a move"""


class AIMoveInputData:
    """Handles input from Ai engine to make the required move by the AI."""

    def __init__(self, game_id: float) -> None:
        self.game_id = game_id
