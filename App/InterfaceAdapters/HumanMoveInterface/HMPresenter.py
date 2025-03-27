"""Presenter for the human move class."""
from App.InterfaceAdapters import MainView
from App.UseCase_Interactors.HumanMove import HMOutputData


class HMPresenter():
    """Initializes a presenter object for the human move use case"""

    def __init__(self, output_data: HMOutputData, main_view: MainView) -> None:
        """initializes the human presenter object"""
        self.human_output_data = output_data
        self.main_view = main_view

    def present(self):
        """Allows flow of information from controller to main view"""
        move_valid = self.human_output_data.move_validity
        game_state = self.human_output_data.win_or_not
        player_symbol = self.human_output_data.symbol
        updated_board_map = self.human_output_data.new_board
        if move_valid:
            row_coord = self.human_output_data.row_coord
            column_coord = self.human_output_data.column_coord
            self.main_view.display_human_move(row_coord, column_coord, game_state, player_symbol,
                                              updated_board_map)
        else:
            row_coord = None
            column_coord = None
            self.main_view.display_human_move(row_coord, column_coord, game_state, player_symbol,
                                              None)
