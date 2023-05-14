import pygame
from config import TETRIS_WIDTH, TETRIS_HEIGHT, COLORS, CENTER_X, CENTER_Y, FONT_PATH


class Renderer:
    """A class responsible for rendering the game state on the pygame display.

    Attributes:
        display (pygame.Surface): Pygame display object
        game_grid (object): Game grid object for handling rendering based on state changes
    """

    def __init__(self, display, game_grid):
        """Class constructor which creates a single renderer class.

        Args:
            display (pygame.Surface): The display surface where the game will be rendered
            game_grid (object): The game grid to be rendered
        """
        self.display = display
        self.game_grid = game_grid

    def render_base(self, display, next_block, score):
        """Renders the base components of the game window, i.e grid, next_block, and score displays

        Args:
            display (pygame.Surface): The display surface where the game will be rendered
            next_block (object): The next block to come out
            score (int): The current score earned by the player
        """
        self._render_background()
        self._render_full_board(display)
        self._render_next_block(display, next_block)
        self._render_score(display, score)

    def _render_background(self):
        """Renders the background of the game on the display surface
        """
        self.display.fill((COLORS["cyan"]))

    def _render_full_board(self, display):
        """Renders full tetris grid on the game display surface

        Args:
            display (pygame.Surface): The display surface where the full grid will be rendered on
        """
        self._render_grid(display, CENTER_X, CENTER_Y)
        self._render_grid_border(display, CENTER_X, CENTER_Y)

    def _render_grid(self, display, center_x, center_y, block_size=30):
        """Renders only tetris grid on the game display surface

        Args:
            display (pygame.Surface): The display surface where the grid will be rendered on
            center_x (int): The x-coordinate of the center of the grid
            center_y (int): The y-coordinate of the center of the grid
            block_size (int): The size of each grid block, default 30
        """
        for row in range(self.game_grid.grid.shape[0]):
            for col in range(self.game_grid.grid.shape[1]):

                grid_rect = pygame.Rect(center_x + col * block_size,
                                        center_y + row * block_size,
                                        block_size,
                                        block_size)

                pygame.draw.rect(
                    display, self.game_grid.grid[row][col], grid_rect)

    def _render_grid_border(self, display, center_x, center_y, border_width=5):
        """Renders only border of tetris grid on the game display surface

        Args:
            display (pygame.Surface): The display surface where the border will be rendered on
            center_x (int): The x-coordinate of the center of the grid
            center_y (int): The y-coordinate of the center of the grid
            border_width (int): The width of the border, default 5
        """
        border_rect = pygame.Rect(center_x - border_width,
                                  center_y - border_width,
                                  TETRIS_WIDTH + 30 + border_width,
                                  TETRIS_HEIGHT + 40)

        pygame.draw.rect(display, COLORS["black"], border_rect, border_width)

    def _render_next_block(self, display, block, block_size=30):
        """Renders next block window on the game display surface

        Args:
            display (pygame.Surface): The display surface where the window will be rendered on
            block (object): Next upcoming block object
            block_size (int): The size of each square of the block, default 30
        """
        font = self._get_font()
        text = self._set_text("Next block", font)

        _, text_height = font.size("Next block")

        self._draw_block_shape(display,
                               block,
                               block_size,
                               CENTER_X + TETRIS_WIDTH + 40,
                               CENTER_Y + TETRIS_HEIGHT/2 + text_height - 40)

        display.blit(text, (CENTER_X + TETRIS_WIDTH + 50,
                            CENTER_Y + TETRIS_HEIGHT/2 - 80))

    def _render_score(self, display, score):
        """Renders score text on the game display surface

        Args:
            display (pygame.Surface): The display surface where the text will be rendered on
            score (int): Total score earned by the player
        """
        font = self._get_font()

        score_text = self._set_text("Score", font)
        v_text = self._set_text(str(score), font)

        s_text_width, s_text_height = font.size("Score")
        v_text_width, v_text_height = font.size(str(score))

        display.blit(score_text, (CENTER_X + TETRIS_WIDTH - 480,
                                  CENTER_Y + TETRIS_HEIGHT/2 - 55 - s_text_height))

        display.blit(v_text, (CENTER_X + TETRIS_WIDTH - 480 + s_text_width/2 - v_text_width/2,
                              CENTER_Y + TETRIS_HEIGHT/2 - 40 + s_text_height/2 - v_text_height/2))

    def render_game_over_txt(self, display):
        """Renders game over text on the game display surface

        Args:
            display (pygame.Surface): The display surface where the text will be rendered on
        """
        font = self._get_font(game_over=True)
        text = self._set_text("Game Over", font)
        t_width, t_height = font.size("Game Over")

        display.blit(text, (CENTER_X + TETRIS_WIDTH/2 - t_width/2,
                            CENTER_Y + TETRIS_HEIGHT/2 - t_height/2))

    def render_highscores(self, display, highscores):
        """Renders highscore text on the game display surface

        Args:
            display (pygame.Surface): The display surface where the text will be rendered on
            highscore (list): Top 5 highscores earned by players
        """
        font = self._get_font()
        text = self._set_text("Highscores", font)
        t_width, t_height = font.size("Highscores")

        display.blit(text, (CENTER_X + TETRIS_WIDTH/2 - t_width/2,
                            CENTER_Y + TETRIS_HEIGHT/2 - t_height/2 + 60))

        x_pos = CENTER_X + TETRIS_WIDTH/2 - 50
        y_pos = CENTER_Y + TETRIS_HEIGHT/2 + 100

        highscore_text_offset = 0

        for _, score_dict in enumerate(highscores):
            score_text = self._set_text(str(score_dict["score"]), font)
            display.blit(score_text, (x_pos+25, y_pos + highscore_text_offset))
            highscore_text_offset += 22

    def _draw_block_shape(self, display, block, block_size, dx, dy):
        """Responsible for drawing the image of the next block

        Args:
            display (pygame.Surface): The display surface where the image will be rendered on
            block (object): Next block
            block_size (int): The size of each square of the block
            dx (int): x-position where the block will be draw on
            dy (int): y-position where the block will be draw on
        """
        for i, row in enumerate(block.shape):
            for j, column in enumerate(row):
                if column == 1:
                    shape_rect = pygame.Rect(dx + j*block_size + 38,
                                             dy + i*block_size - 40,
                                             block_size, block_size)
                    pygame.draw.rect(display, block.color, shape_rect, 0)

    def _set_text(self, text, font):
        """ Renders the provided text with the selected font

        Args:
            text (str): The text to be rendered
            font (pygame.font.Font): The font to be used for rendering the text

        Returns:
            pygame.Surface: The rendered text as a pygame surface
        """
        return font.render(text, 1, COLORS["black"])

    def _get_font(self, game_over=False):
        """Retrieves the font to be used in the game, for game over text, a larger font size is used

        Args:
            game_over (bool): A flag indicating whether the game is over

        Returns:
            pygame.font.Font: The font to be used in the game

        Raises:
            FileNotFoundError: If the font file is not found, default to Roboto
        """
        try:
            if not game_over:
                font = pygame.font.Font(FONT_PATH, 18)
            else:
                font = pygame.font.Font(FONT_PATH, 40)
        except FileNotFoundError:
            font = pygame.font.SysFont("Roboto", 30)
        return font
