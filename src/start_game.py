import pygame
from config import PYGAME_WIDTH, PYGAME_HEIGHT
from game_loop import GameLoop
from renderer import Renderer
from game_grid import GameGrid

def start_game():
    display = pygame.display.set_mode((PYGAME_WIDTH , PYGAME_HEIGHT))

    game_grid = GameGrid()
    renderer = Renderer(display, game_grid)
    game_loop = GameLoop(renderer, display)

    pygame.init()

    game_loop.start()

if __name__ == "__main__":
    start_game()
