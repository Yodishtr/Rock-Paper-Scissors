"""Interactor for creating a new game of Tic Tac Toe."""
from App.UseCase_Interactors.CreateGame import CGInputData, CGOutputData
from Entities import Game
from Entities.Board import Board
from Entities.GameRespository import GameRepository
from Entities.AIplayer import AIPlayer
from Entities.Player import Player


class CreateInteractor:
    """Interactor for creating a new game."""

    def __init__(self, game_repo: GameRepository) -> None:
        """holds the input data and creates a new game accordingly"""
        self.game_repo = game_repo

    def create_new_game(self, input_data: CGInputData) -> CGOutputData:
        """Creates a new game from the input data. Transforms and returns basic data to output data
        """

        new_board = Board(input_data.board_row, input_data.board_column)
        board_dict_map = new_board.the_board
        player1_tup = (input_data.player1type, input_data.player1name, input_data.player1symbol)
        player2_tup = (input_data.player2type, input_data.player2name, input_data.player2symbol)

        if player1_tup[0].lower() == "ai":
            player1 = AIPlayer(player1_tup[1], player1_tup[2], player1_tup[0], input_data.strategy)
            player2 = Player(player2_tup[1], player2_tup[2], player2_tup[0])
        elif player2_tup[0].lower() == "ai":
            player1 = Player(player1_tup[1], player1_tup[2], player1_tup[0])
            player2 = AIPlayer(player2_tup[1], player2_tup[2], player2_tup[0], input_data.strategy)
        else:
            player1 = Player(player1_tup[1], player1_tup[2], player1_tup[0])
            player2 = Player(player2_tup[1], player2_tup[2], player2_tup[0])

        new_game = Game.Game(player1, player2, new_board)
        id_game_created = new_game.game_id
        final_output_data = CGOutputData.CGOutputData(board_dict_map, player1_tup[1],
                                                      player2_tup[1], player1_tup[0],
                                                      player2_tup[0], player1_tup[2],
                                                      player2_tup[2], id_game_created)
        self.game_repo.save_game(new_game)

        return final_output_data
