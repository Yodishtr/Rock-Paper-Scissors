"""Interactor for AI move use case."""
from App.UseCase_Interactors.AIMove import AIMoveInputData
from App.UseCase_Interactors.AIMove.AIMoveOutputData import AIOutputData
from Entities.GameRespository import GameRepository


class AIMoveInteractor:
    """Interactor that will make the AI move based on the strategy chosen by the player for the
    AI."""

    def __init__(self, game_repo: GameRepository) -> None:
        self.game_repo = game_repo

    def execute_ai_move(self, aiInputData: AIMoveInputData):
        """Makes the ai move on the board based on the strategy chosen by the human player for
        the Ai player"""
        id_game = aiInputData.game_id
        current_game = self.game_repo.find_game(id_game)
        curr_player = current_game.current_player
        if curr_player.race.lower() == "ai":
            move_to_make = curr_player.choose_move(current_game)
            current_game.board.the_board[move_to_make] = curr_player.symbol
            updated_board = current_game.board.the_board
            ai_win_or_no = current_game.check_winning_combo()
            check_draw = current_game.board.check_board_full()
            self.game_repo.save_game(current_game)
            print("AI placed symbol:", curr_player.symbol, "at cell:", move_to_make)
            print("Board after AI move:", current_game.board.the_board)

            if ai_win_or_no == curr_player.symbol:
                return AIOutputData(move_to_make, True, False, updated_board)
            elif ai_win_or_no is None and check_draw:
                return AIOutputData(move_to_make, False, True, updated_board)
            elif ai_win_or_no is None and (not check_draw):
                return AIOutputData(move_to_make, False, False, updated_board)
