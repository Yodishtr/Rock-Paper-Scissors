"""Interactor for AI move use case."""
from App.UseCase_Interactors.AIMove import AIMoveInputData
from Entities.GameRespository import GameRepository


class AIMoveInteractor:
    """Interactor that will make the AI move based on the strategy chosen by the player for the
    AI."""

    def __init__(self, aiInputData: AIMoveInputData, game_repo: GameRepository) -> None:
        self.game_repo = game_repo
        self.game_id = aiInputData.game_id

    def execute_ai_move(self) -> None:
        """Makes the ai move on the board based on the strategy chosen by the human player for
        the Ai player"""
        current_game = self.game_repo.find_game(self.game_id)
        curr_player = current_game.current_player
        if curr_player.race.lower() == "ai":
            move_to_make = curr_player.choose_move(current_game)
            current_game.board.the_board[move_to_make] = curr_player.symbol
            self.game_repo.save_game(current_game)
            print("Ai made its move")
        else:
            print("wrong order of methods. it should be the humans turn")
