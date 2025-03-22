"""Interactor for AI move use case."""
from App.UseCase_Interactors.AIMove import AIMoveInputData
from App.UseCase_Interactors.AIMove.AIMoveOutputData import AIOutputData
from Entities.GameRespository import GameRepository


class AIMoveInteractor:
    """Interactor that will make the AI move based on the strategy chosen by the player for the
    AI."""

    def __init__(self, aiInputData: AIMoveInputData, game_repo: GameRepository) -> None:
        self.game_repo = game_repo
        self.game_id = aiInputData.game_id

    def execute_ai_move(self) -> AIOutputData | None:
        """Makes the ai move on the board based on the strategy chosen by the human player for
        the Ai player"""
        current_game = self.game_repo.find_game(self.game_id)
        curr_player = current_game.current_player
        if curr_player.race.lower() == "ai":
            move_to_make = curr_player.choose_move(current_game)
            current_game.board.the_board[move_to_make] = curr_player.symbol
            ai_win_or_no = current_game.check_winning_combo()
            check_draw = current_game.board.check_board_full()
            self.game_repo.save_game(current_game)
            if ai_win_or_no == curr_player.symbol:
                return AIOutputData(move_to_make, True, False)
            elif ai_win_or_no is None and check_draw:
                return AIOutputData(move_to_make, False, True)
            elif ai_win_or_no is None and (not check_draw):
                return AIOutputData(move_to_make, False, False)
