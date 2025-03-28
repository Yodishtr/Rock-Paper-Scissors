"""Presenter class exclusively for use by the create game use case"""
from App.InterfaceAdapters import MainView
from App.UseCase_Interactors.CreateGame import CGOutputData


class CGPresenter:
    """Defines a presenter for the create game use case and methods to process output data"""

    def __init__(self, mainView: MainView) -> None:
        """initializes a presenter object that allows flow of information to the view object"""
        self.main_view = mainView

    def present(self, output_data: CGOutputData) -> None:
        """processes the output data from the interactor to the view object for UI."""
        board_game_map = output_data.board_map
        player1_name = output_data.player1name
        player2_name = output_data.player2name
        player1_symbol = output_data.player1Sym
        player2_symbol = output_data.player2Sym
        player1_type = output_data.player1type
        player2_type = output_data.player2type
        self.main_view.render_board_and_players(board_game_map, player1_name, player2_name,
                                                player1_symbol, player2_symbol, player1_type,
                                                player2_type)
