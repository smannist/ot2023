import unittest
import pygame
from block import Block
from renderer import Renderer
from game_loop import GameLoop
from game_grid import GameGrid
from config import PYGAME_HEIGHT, PYGAME_WIDTH

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.display = pygame.display.set_mode((PYGAME_WIDTH , PYGAME_HEIGHT))
        self.block = Block(5,3)
        self.game_grid = GameGrid()
        self.renderer = Renderer(self.display, self.game_grid)
        self.game_loop = GameLoop(self.renderer, self.display, self.block)
