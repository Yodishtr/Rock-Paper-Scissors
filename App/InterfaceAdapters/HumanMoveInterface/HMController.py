"""Controller for human player's move based on user input"""
from App.InterfaceAdapters.HumanMoveInterface import HMPresenter
from App.UseCase_Interactors.HumanMove import HMInputData, HMInteractor


class HMController:
    """Controller object monitoring the human input to make its move on the board"""

    def __init__(self, human_interactor: HMInteractor, human_presenter: HMPresenter,
                 game_id: float) -> None:
        self.interactor = human_interactor
        self.presenter = human_presenter
        self.game_id = game_id

    def handle_human_move(self, mouse_x, mouse_y) -> None:
        """Executes the human move based on the input received from the UI."""
        user_input = self._convert_to_board(mouse_x, mouse_y)
        input_data = HMInputData.HMInputData(user_input[0], user_input[1], self.game_id)
        output_data = self.interactor.human_make_move(input_data)
        self.presenter.present(output_data)

    def _convert_to_board(self, mouse_x, mouse_y) -> tuple[int, int]:
        """Converts mouse input into the board map coordinates"""
        row_coordinate = (mouse_x // 100) + 1
        column_coordinate = (mouse_y // 100) + 1

        return (row_coordinate, column_coordinate)
