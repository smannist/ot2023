import pygame

# colors are temporary until I find a color scheme that looks nice
colors = {"black": (0,0,0),
          "cyan": (204,255,255),
          "dark_grey": (80,80,80),
          "light_grey": (128,128,128)}

class Renderer:
    def __init__(self, display, p_width, p_height, t_width, t_height, game_grid):
        self.display = display
        self.pygame_width = p_width
        self.pygame_height = p_height
        self.tetris_width = t_width
        self.tetris_height = t_height
        self.game_grid = game_grid
        self.grid = game_grid.grid

    def render_background(self):
        self.display.fill((colors["cyan"]))

    def render_board(self, surface):
        dx = (self.pygame_width - self.tetris_width) // 2   
        dy = (self.pygame_height - self.tetris_height) // 2
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
        border_rect = pygame.Rect(dx - border_width, dy - border_width, self.tetris_width + 30 + border_width, self.tetris_height + 40)
        pygame.draw.rect(surface, colors["black"], border_rect, border_width)
