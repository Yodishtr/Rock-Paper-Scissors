"""Interactor for Restarting Game use case"""
from App.UseCase_Interactors.RestartGame import RGInputData, RGOutputData
from Entities.GameRespository import GameRepository


class RGInteractor:
    """Defines the interactor for restarting a game with the same players and associated methods
    to do so."""
    def __init__(self, input_data: RGInputData, game_repo: GameRepository) -> None:
        """Initializes the Restart game interactor"""
        self.input_data = input_data
        self.game_repo = game_repo

    def execute_restart(self) -> RGOutputData:
        curr_game_id = self.input_data.game_id
        curr_game = self.game_repo.find_game(curr_game_id)
        curr_game.restart()
        self.game_repo.save_game(curr_game)
        output_data = RGOutputData.RGOutputData(curr_game.board.the_board, curr_game.current_player)
        return output_data
