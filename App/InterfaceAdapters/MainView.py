"""Main view for rendering the game board and the moves using pygame library"""
from App.InterfaceAdapters.AIMoveInterface import AIMPresenter
from App.InterfaceAdapters.CreateGameInterface import CGPresenter
from App.InterfaceAdapters.HumanMoveInterface import HMPresenter
from App.InterfaceAdapters.RestartGameInterface import RestartPresenter


class MainView():
    """View object containing all the required methods for rendering the UI."""

    def __init__(self, create_presenter: CGPresenter, human_presenter: HMPresenter,
                 ai_presenter: AIMPresenter, restart_presenter: RestartPresenter) -> None:
        self.create_new_presenter = create_presenter
        self.human_move_presenter = human_presenter
        self.ai_move_presenter = ai_presenter
        self.restart_game_presenter = restart_presenter
