"""Controller to handle ai use case interactor"""
from App.InterfaceAdapters.AIMoveInterface.AIMPresenter import AIPresenter
from App.UseCase_Interactors.AIMove import AIMoveInteractor
from App.UseCase_Interactors.AIMove.AIMoveInputData import AIMoveInputData


class AIController():
    """Controller object to handle the move made by the AI."""

    def __init__(self, ai_interactor: AIMoveInteractor, ai_presenter: AIPresenter,
                 game_id: float) -> None:
        self.ai_interactor = ai_interactor
        self.ai_presenter = ai_presenter
        self.id_game = game_id

    def handle_ai_move(self):
        """Receives the move made by the ai and calls the presenter with the output data"""
        input_data = AIMoveInputData(self.id_game)
        output_data = self.ai_interactor.execute_ai_move(input_data)
