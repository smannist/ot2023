import pygame
from config import PYGAME_WIDTH, PYGAME_HEIGHT, BLOCK_START_X, BLOCK_START_Y
from game_loop import GameLoop
from renderer import Renderer
from game_grid import GameGrid
from block import Block
from database.initialize_database import initialize_database
from services.highscore_service import HighscoreService


def start_game():
    """Responsible for setting up pygame and starting the game loop
    """
    display = pygame.display.set_mode((PYGAME_WIDTH, PYGAME_HEIGHT))

    highscore_service = HighscoreService()
    game_grid = GameGrid()
    block = Block(BLOCK_START_X, BLOCK_START_Y)
    renderer = Renderer(display, game_grid)
    game_loop = GameLoop(renderer, display, block, highscore_service)

    pygame.init()
    pygame.display.set_caption("Tetris")

    pygame.mixer.init()
    pygame.mixer.music.load("src/music/caffeine_crazed_coin-op_kids.mp3")
    pygame.mixer.music.play(-1)

    initialize_database()

    game_loop.start()


if __name__ == "__main__":
    start_game()
