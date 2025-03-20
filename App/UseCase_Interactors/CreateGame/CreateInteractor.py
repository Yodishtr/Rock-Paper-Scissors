"""Interactor for creating a new game of Tic Tac Toe."""
from App.UseCase_Interactors.CreateGame import CGInputData, CGOutputData
from Entities import Game
from Entities.Board import Board
from Entities.GameRespository import GameRepository
from Entities.Player import Player


class CreateInteractor:
    """Interactor for creating a new game."""

    def __init__(self, input_data: CGInputData, game_repo: GameRepository) -> None:
        """holds the input data and creates a new game accordingly"""
        self.rows = input_data.board_row
        self.columns = input_data.board_column
        self.player1 = (input_data.player1type, input_data.player1name, input_data.player1symbol)
        self.player2 = (input_data.player2type, input_data.player2name, input_data.player2symbol)
        self.game_repo = game_repo

    def create_new_game_output(self) -> CGOutputData:
        """Creates a new game from the input data. Transforms and returns basic data to output data
        """
        new_board = Board(self.rows, self.columns)
        board_dict_map = new_board.the_board
        final_output_data = CGOutputData.CGOutputData(board_dict_map, self.player1[1],
                                                      self.player2[1], self.player1[0],
                                                      self.player2[0], self.player1[2],
                                                      self.player2[2])
        player1 = Player(self.player1[1], self.player1[2], self.player1[0])
        player2 = Player(self.player2[1], self.player2[2], self.player2[0])
        new_game = Game.Game(player1, player2, new_board)
        self.game_repo.save_game(new_game)

        return final_output_data
