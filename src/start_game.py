import pygame
from game_loop import GameLoop
from renderer import Renderer
from game_grid import GameGrid

PYGAME_WIDTH = 800
PYGAME_HEIGHT = 900

TETRIS_WIDTH = 300
TETRIS_HEIGHT = 600

GAME_GRID_ROWS = 21
GAME_GRID_COLUMNS = 11

def start_game():
    display = pygame.display.set_mode((PYGAME_WIDTH , PYGAME_HEIGHT))

    game_grid = GameGrid(GAME_GRID_ROWS, GAME_GRID_COLUMNS)
    renderer = Renderer(display, PYGAME_WIDTH, PYGAME_HEIGHT, TETRIS_WIDTH, TETRIS_HEIGHT, game_grid)
    game_loop = GameLoop(renderer, display)

    pygame.init()

    game_loop.start()

if __name__ == "__main__":
    start_game()
