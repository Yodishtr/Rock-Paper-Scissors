"""Presenter class exclusively for use by the create game use case"""
from App.UseCase_Interactors.CreateGame import CGOutputData


class CGPresenter:
    """Defines a presenter for the create game use case and methods to process output data"""

    def __init__(self, output_data: CGOutputData) -> None:
        """"""
