"""Input data representing the move by the human player."""

class HMInputData:
    """A move made by the human player. input is received by the controller and the HMInputData
    object is instantiated to be passed to the HMInteractor."""

    def __init__(self, row_coordinate: int, column_coordinate: int) -> None:
        self.row_coord = row_coordinate
        self.column_coord = column_coordinate
