import pygame
from game_loop import GameLoop
from renderer import Renderer

dimensions = {"width": 800,
              "height": 800}

def start_game():
    display = pygame.display.set_mode((dimensions["width"], dimensions["height"]))

    renderer = Renderer(display)
    game_loop = GameLoop(renderer)

    pygame.init()

    game_loop.start()

if __name__ == "__main__":
    start_game()
