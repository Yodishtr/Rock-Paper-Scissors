"""Controller class exclusively for the create game use case"""
from App.InterfaceAdapters.CreateGameInterface import CGPresenter
from App.UseCase_Interactors.CreateGame import CreateInteractor
from App.UseCase_Interactors.CreateGame.CGInputData import CGInputData


class CGController:
    """Defines a controller for the create game use case with methods to control data flow"""

    def __init__(self, createInteractor: CreateInteractor, createpresenter: CGPresenter) -> None:
        self.createInteractor = createInteractor
        self.createPresenter = createpresenter

    def handle_create_new(self):
        """Executes the create new game method through the interactor and relays the output data
        to the presenter."""
        board_dimension_str = input("Enter the board size (eg 3,3 or 4,4): ")
        board_dimension = tuple(int(x) for x in board_dimension_str.split(","))
        board_rows, board_columns = board_dimension[0], board_dimension[1]

        player_1_str = input("Enter first player (eg AI (type), Robot (name), X (symbol)): ")
        player_1_tup = tuple(x for x in player_1_str.split(","))
        player1_type, player1_name, player1_symbol = (player_1_tup[0], player_1_tup[1],
                                                      player_1_tup[2])

        player_2_str = input("Enter second player (eg Human, BIGSMOKE, O): ")
        player_2_tup = tuple(x for x in player_2_str.split(","))
        player2_type, player2_name, player2_symbol = (player_2_tup[0], player_2_tup[1],
                                                      player_2_tup[2])

        if player1_type.lower() != "ai" and player2_type.lower() != "ai":
            strategy = ""

        else:
            strategy = input("Enter the strategy for the AI (minimax or neural net): ")

        input_data = CGInputData(board_rows, board_columns, player1_type, player2_type,
                                 player1_name, player2_name, player1_symbol, player2_symbol,
                                 strategy)

        output_data = self.createInteractor.create_new_game(input_data)
        self.createPresenter.present(output_data)
