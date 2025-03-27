"""Presenter class exclusively for use by the create game use case"""
from App.InterfaceAdapters import MainView
from App.UseCase_Interactors.CreateGame import CGOutputData


class CGPresenter:
    """Defines a presenter for the create game use case and methods to process output data"""

    def __init__(self, output_data: CGOutputData, mainView: MainView) -> None:
        """initializes a presenter object that allows flow of information to the view object"""
        self.output_data = output_data
        self.main_view = mainView

    def present(self) -> None:
        """processes the output data from the interactor to the view object for UI."""
        board_game_map = self.output_data.board_map
        player1_name = self.output_data.player1name
        player2_name = self.output_data.player2name
        player1_symbol = self.output_data.player1Sym
        player2_symbol = self.output_data.player2Sym
        player1_type = self.output_data.player1type
        player2_type = self.output_data.player2type
        self.main_view.render_board_and_players(board_game_map, player1_name, player2_name,
                                                player1_symbol, player2_symbol, player1_type,
                                                player2_type)
