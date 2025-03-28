"""Controller handling information flow from the interactor to the presenter and finally the
main view"""
from App.InterfaceAdapters.RestartGameInterface import RestartPresenter
from App.UseCase_Interactors.RestartGame import RGInteractor
from App.UseCase_Interactors.RestartGame.RGInputData import RGInputData


class RestartController():
    """Controller in charge of restarting the game by transferring the new board map via the output
    data to the presenter."""

    def __init__(self, restart_interactor: RGInteractor, restart_presenter: RestartPresenter,
                 game_id: float):
        self.restart_interactor = restart_interactor
        self.restart_presenter = restart_presenter
        self.game_id = game_id

    def handle_restart_game(self):
        """handles the resetting of the game"""
        restart_input_data_object = RGInputData(self.game_id)
        output_data = self.restart_interactor(restart_input_data_object)
        self.restart_presenter.present(output_data)
