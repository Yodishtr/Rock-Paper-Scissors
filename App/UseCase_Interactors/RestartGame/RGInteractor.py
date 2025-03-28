"""Interactor for Restarting Game use case"""
from App.UseCase_Interactors.RestartGame import RGInputData, RGOutputData
from Entities.GameRespository import GameRepository


class RGInteractor:
    """Defines the interactor for restarting a game with the same players and associated methods
    to do so."""
    def __init__(self, game_repo: GameRepository) -> None:
        """Initializes the Restart game interactor"""
        self.game_repo = game_repo

    def execute_restart(self, input_data: RGInputData) -> RGOutputData:
        """restarts the game"""
        curr_game_id = input_data.game_id
        curr_game = self.game_repo.find_game(curr_game_id)
        curr_game.restart()
        self.game_repo.save_game(curr_game)
        output_data = RGOutputData.RGOutputData(curr_game.board.the_board, curr_game_id)
        return output_data
