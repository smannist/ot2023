import pygame
from config import PYGAME_WIDTH, PYGAME_HEIGHT, TETRIS_WIDTH, TETRIS_HEIGHT, BACKGROUND_COLORS

class Renderer:
    def __init__(self, display, game_grid):
        self.display = display
        self.grid = game_grid.grid

    def render_background(self):
        self.display.fill((BACKGROUND_COLORS["cyan"]))

    def render_board(self, surface):
        dx = (PYGAME_WIDTH - TETRIS_WIDTH) // 2   
        dy = (PYGAME_HEIGHT - TETRIS_HEIGHT) // 2
        self.render_grid(surface, dx, dy)
        self.render_grid_border(surface, dx, dy)

    def render_grid(self, surface, dx, dy, block_size=30):
        self.render_background()

        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                if (row + col) % 2 == 0:
                    color = BACKGROUND_COLORS["dark_grey"]
                else:
                    color = BACKGROUND_COLORS["light_grey"]
                grid_rectangle = pygame.Rect(dx + col * block_size, dy + row * block_size, block_size, block_size)
                pygame.draw.rect(surface, color, grid_rectangle)

    def render_grid_border(self, surface, dx, dy, border_width=5):
        border_rect = pygame.Rect(dx - border_width, dy - border_width, TETRIS_WIDTH + 30 + border_width, TETRIS_HEIGHT + 40)
        pygame.draw.rect(surface, BACKGROUND_COLORS["black"], border_rect, border_width)
