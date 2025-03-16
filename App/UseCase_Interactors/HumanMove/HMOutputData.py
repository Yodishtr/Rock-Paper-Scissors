"""Output data for the move made by the human player."""

class HMOutputData:
    """Output data representing the move made by a human player. Returned by the interactor.
    """
    def __init__(self, row_coordinate: int, column_coordinate: int, move_valid: bool) -> None:
        self.row_coord = row_coordinate
        self.column_coord = column_coordinate
        self.move_validity = move_valid
