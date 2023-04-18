import pygame
from config import TETRIS_WIDTH, TETRIS_HEIGHT, BACKGROUND_COLORS, CENTER_X, CENTER_Y

class Renderer:
    def __init__(self, display, game_grid):
        self.display = display
        self.game_grid = game_grid

    def render_all(self, display):
        self._render_background()
        self._render_full_board(display)

    def _render_background(self):
        self.display.fill((BACKGROUND_COLORS["cyan"]))

    def _render_full_board(self, display):
        self._render_grid(display, CENTER_X, CENTER_Y)
        self._render_grid_border(display, CENTER_X, CENTER_Y)

    def _render_grid(self, display, center_x, center_y, block_size=30):
        for row in range(self.game_grid.grid.shape[0]):
            for col in range(self.game_grid.grid.shape[1]):

                grid_rectangle = pygame.Rect(center_x + col * block_size, \
                                             center_y + row * block_size, \
                                             block_size, block_size)

                pygame.draw.rect(display, self.game_grid.grid[row][col], grid_rectangle)

    def _render_grid_border(self, display, center_x, center_y, border_width=5):

        border_rectangle = pygame.Rect(center_x - border_width, \
                                       center_y - border_width, \
                                       TETRIS_WIDTH + 30 + border_width, \
                                       TETRIS_HEIGHT + 40)

        pygame.draw.rect(display, BACKGROUND_COLORS["black"], border_rectangle, border_width)
