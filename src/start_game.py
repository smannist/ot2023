import pygame
from config import PYGAME_WIDTH, PYGAME_HEIGHT
from game_loop import GameLoop
from renderer import Renderer
from game_grid import GameGrid
from block import Block

def start_game():
    display = pygame.display.set_mode((PYGAME_WIDTH , PYGAME_HEIGHT))

    game_grid = GameGrid()
    block = Block(5,0)
    renderer = Renderer(display, game_grid)
    game_loop = GameLoop(renderer, display, block)

    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("src/music/caffeine_crazed_coin-op_kids.mp3")
    pygame.mixer.music.play(-1)

    game_loop.start()

if __name__ == "__main__":
    start_game()
