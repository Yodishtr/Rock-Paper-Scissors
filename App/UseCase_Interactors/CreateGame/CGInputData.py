"""Input Data class representing user input for creating a new game."""


class CGInputData:
    """An input data class representing the information from interface layer on the game to be
    created"""

    def __init__(self, board_row: int, board_column: int, player1type: str, player2type: str,
                 player1name: str, player2name: str, player1sym: str, player2sym: str,
                 strategy: str) -> None:
        self.board_row = board_row
        self.board_column = board_column
        self.player1type = player1type
        self.player2type = player2type
        if self.player1type.lower() == "human":
            self.player1name = player1name
        else:
            self.player1name = "AI"
        if self.player2type.lower() == "human":
            self.player2name = player2name
        else:
            self.player2name = "AI"
        self.player1symbol = player1sym
        self.player2symbol = player2sym
        self.strategy = strategy
