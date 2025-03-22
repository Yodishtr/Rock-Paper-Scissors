"""Controller class exclusively for the create game use case"""
from App.UseCase_Interactors.CreateGame import CreateInteractor


class CGController:
    """Defines a controller for the create game use case with methods to control data flow"""

    def __init__(self, createInteractor: CreateInteractor) -> None:
        self.createInteractor = createInteractor
