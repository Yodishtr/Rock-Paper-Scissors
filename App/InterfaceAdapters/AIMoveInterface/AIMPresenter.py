"""Presenter to handle the Ai interactor use case"""
from App.InterfaceAdapters import MainView
from App.UseCase_Interactors.AIMove import AIMoveOutputData


class AIPresenter():
    """Presenter that handles information flow from ai controller to the main view"""

    def __init__(self, main_view: MainView) -> None:
        self.main_view = main_view

    def present_ai_move(self, output_data: AIMoveOutputData):
        """Transfers info from interactor via the output data to the main view"""
        move_by_ai = output_data.move_made
        ai_won_or_not = output_data.ai_win_or_lose
        draw_or_not = output_data.draw_or_no
        updated_board = output_data.updated_board
        self.main_view(ai_won_or_not, draw_or_not, updated_board)
