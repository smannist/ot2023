import pygame
from colors import colors
from config import PYGAME_WIDTH, PYGAME_HEIGHT, TETRIS_WIDTH, TETRIS_HEIGHT

class Renderer:
    def __init__(self, display, game_grid):
        self.display = display
        self.grid = game_grid.grid

    def render_background(self):
        self.display.fill((colors["cyan"]))

    def render_board(self, surface):
        dx = (PYGAME_WIDTH - TETRIS_WIDTH) // 2   
        dy = (PYGAME_HEIGHT - TETRIS_HEIGHT) // 2
        self.render_grid(surface, dx, dy)
        self.render_grid_border(surface, dx, dy)

    def render_grid(self, surface, dx, dy, block_size=30):
        self.render_background()

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if (i + j) % 2 == 0:
                    color = colors["dark_grey"]
                else:
                    color = colors["light_grey"]
                grid_rectangle = pygame.Rect(dx + j * block_size, dy + i * block_size, block_size, block_size)
                pygame.draw.rect(surface, color, grid_rectangle)

    def render_grid_border(self, surface, dx, dy, border_width=5):
        border_rect = pygame.Rect(dx - border_width, dy - border_width, TETRIS_WIDTH + 30 + border_width, TETRIS_HEIGHT + 40)
        pygame.draw.rect(surface, colors["black"], border_rect, border_width)
