"""Main view for rendering the game board and the moves using pygame library"""
import pygame


class MainView():
    """View object containing all the required methods for rendering the UI."""

    def __init__(self, screen) -> None:
        self.screen = screen
        self.cell_size = 100
        self.player1_info = None
        self.player2_info = None
        self.font = pygame.font.SysFont(None, 64)

    def render_board_and_players(self, board_map: dict[tuple[int, int]], player1name: str,
                                 player2name: str, player1symbol: str, player2symbol: str,
                                 player1type: str, player2type: str):
        """Renders the board with the players and their symbols"""
        white = (255, 255, 255)
        black = (0, 0, 0)
        self.screen.fill(white)

        all_coordinates = board_map.keys()
        max_row, max_column = 0, 0
        for x in all_coordinates:
            max_row = max(x[0], max_row)
            max_column = max(x[1], max_column)

        for row in range(max_row + 1):
            y = row * self.cell_size
            pygame.draw.line(self.screen, black, (0, y), (max_column * self.cell_size, y), width=2)

        for col in range(max_column + 1):
            x = col * self.cell_size
            pygame.draw.line(self.screen, black, (0, x), (max_row * self.cell_size, x), width=2)

        for (row, col), symbol in board_map.items():
            if symbol is not None:
                cell_center_x = (col - 1) * self.cell_size + self.cell_size // 2
                cell_center_y = (row - 1) * self.cell_size + self.cell_size // 2

                text_surface = self.font.render(symbol, True, (255, 0, 0))
                text_rect = text_surface.get_rect(center=(cell_center_x, cell_center_y))
                self.screen.blit(text_surface, text_rect)

        info_str = "Player1: " + player1name + " " + player1symbol + " " + player1type + " "  "|" \
                   "Player2: " + player2name + " " + player2symbol + " " + player2type
        info_surface = self.font.render(info_str, True, (0, 0, 0))
        self.screen.blit(info_surface, (10, max_row * self.cell_size + 10))

        self.player1_info = (player1name, player1type, player1symbol)
        self.player2_info = (player2name, player2type, player2symbol)

        pygame.display.flip()

    def display_human_move(self, row_coord, column_coord, game_state, symbol, board_map):
        """Displays the move made by human player on the screen"""
        if game_state:
            print("motherfucker you won")
        else:
            if row_coord and column_coord:
                self.render_board_and_players(board_map, self.player1_info[0], self.player2_info[0],
                                              self.player1_info[2], self.player2_info[2],
                                              self.player1_info[1], self.player2_info[1])
            elif (not row_coord) and (not column_coord):
                print("Invalid Move")

    def display_ai_move(self, win_or_not, draw_or_not, updated_board):
        """Displays move made by the AI"""
        if win_or_not:
            print("Ai won lmao")
        elif draw_or_not:
            print("damn you smart as the ai")
        else:
            self.render_board_and_players(updated_board, self.player1_info[0], self.player2_info[0],
                                          self.player1_info[2], self.player2_info[2],
                                          self.player1_info[1], self.player2_info[1])

    def display_restarted_board(self, cleared_board_map):
        """displays a cleared board_map"""
        self.render_board_and_players(cleared_board_map, self.player1_info[0], self.player2_info[0],
                                      self.player1_info[2], self.player2_info[2],
                                      self.player1_info[1], self.player2_info[1])
