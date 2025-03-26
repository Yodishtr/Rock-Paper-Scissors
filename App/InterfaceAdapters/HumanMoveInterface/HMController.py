"""Controller for human player's move based on user input"""
from App.InterfaceAdapters.HumanMoveInterface import HMPresenter
from App.UseCase_Interactors.HumanMove import HMInteractor


class HMController:
    """Controller object monitoring the human input to make its move on the board"""

    def __init__(self, human_interactor: HMInteractor, human_presenter: HMPresenter) -> None:
        self.interactor = human_interactor
        self.presenter = human_presenter

    def handle_human_move(self, ):
