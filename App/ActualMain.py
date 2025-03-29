"""Main class that instantiates every object required and wires everything together."""
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from App.DataAccessLayer.grepo.InMemoryRespository import InMemoryRepository
from App.InterfaceAdapters.AIMoveInterface.AIMController import AIController
from App.InterfaceAdapters.AIMoveInterface.AIMPresenter import AIPresenter
from App.InterfaceAdapters.CreateGameInterface.CGController import CGController
from App.InterfaceAdapters.CreateGameInterface.CGPresenter import CGPresenter
from App.InterfaceAdapters.HumanMoveInterface.HMController import HMController
from App.InterfaceAdapters.HumanMoveInterface.HMPresenter import HMPresenter
from App.InterfaceAdapters.MainView import MainView
from App.InterfaceAdapters.RestartGameInterface.RestartController import RestartController
from App.InterfaceAdapters.RestartGameInterface.RestartPresenter import RestartPresenter
from App.UseCase_Interactors.AIMove.AIMoveInteractor import AIMoveInteractor
from App.UseCase_Interactors.CreateGame.CreateInteractor import CreateInteractor
from App.UseCase_Interactors.HumanMove.HMInteractor import HMInteractor
from App.UseCase_Interactors.RestartGame.RGInteractor import RGInteractor

def main():
    """Game factory running the tic tac toe game"""
    # game repo
    current_repo = InMemoryRepository()

    # interactors
    create_game_interactor = CreateInteractor(current_repo)
    human_move_interactor = HMInteractor(current_repo)
    restart_interactor = RGInteractor(current_repo)
    ai_move_interactor = AIMoveInteractor(current_repo)

    # creating the main View
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    main_view = MainView(screen)

    # creating the presenters
    create_game_presenter = CGPresenter(main_view)
    ai_presenter = AIPresenter(main_view)
    human_presenter = HMPresenter(main_view)
    restart_presenter = RestartPresenter(main_view)

    # create game controller
    create_controller = CGController(create_game_interactor, create_game_presenter)
    create_controller.handle_create_new()

    current_game_id = list(current_repo.game_dictionary.keys())[-1]

    # other controllers
    ai_move_controller = AIController(ai_move_interactor, ai_presenter, current_game_id)
    human_move_controller = HMController(human_move_interactor, human_presenter, current_game_id)
    restart_game_controller = RestartController(restart_interactor, restart_presenter, current_game_id)

    # game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                human_move_controller.handle_human_move(mouse_x, mouse_y)
                current_game = current_repo.find_game(current_game_id)
                if current_game.check_winning_combo() is None and (not
                   current_game.board.check_board_full()):
                    if current_game.current_player.race.lower() == "ai":
                        ai_move_controller.handle_ai_move()

        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()
