"""Interactor handling the logic for the move made by a human player."""
from App.UseCase_Interactors.HumanMove import HMInputData, HMOutputData
from Entities.GameRespository import GameRepository


class HMInteractor:
    """Interactor that determines the move made by the human player. checks its validity and makes
    the move if valid or prints a message and asks for new input if not valid."""

    def __init__(self, input_data: HMInputData, game_repo: GameRepository) -> None:
        self.row = input_data.row_coord
        self.column = input_data.column_coord
        self.game_id = input_data.game_id
        self.game_repo = game_repo

    def human_make_move(self) -> HMOutputData | None:
        """Checks if the move is valid and if it is does it. If not it prints an error message
        and asks player for input again"""
        game_playing = self.game_repo.find_game(self.game_id)
        is_move_valid = game_playing.board.check_valid_move(self.row, self.column)
        board_full = game_playing.board.check_board_full()
        if is_move_valid and not board_full:
            curr_player = game_playing.current_player
            curr_player_symbol = curr_player.symbol
            game_playing.board.the_board[(self.row, self.column)] = curr_player_symbol
            win_or_not = game_playing.check_winning_combo()
            if win_or_not:
                output_object = HMOutputData.HMOutputData(self.row, self.column, is_move_valid,
                                                          win_or_not)
                self.game_repo.save_game(game_playing)
                return output_object

        else:
            print("Move is invalid: Enter a valid move within board size")
            output_object = HMOutputData.HMOutputData(self.row, self.column, is_move_valid, False)
            return output_object
