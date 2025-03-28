"""Presenter that handles the display of a new board map with no symbols on it"""
from App.InterfaceAdapters import MainView
from App.UseCase_Interactors.RestartGame import RGOutputData


class RestartPresenter():
    """Presenter for the restart use case allowing us to display a new cleared board map"""
    def __init__(self, main_view: MainView) -> None:
        self.main_view = main_view

    def present(self, output_data: RGOutputData):
        """presents the output data"""
