import unittest
import numpy as np
from src.game_grid import GameGrid

class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.game_grid = GameGrid(10, 20)

    def test_game_grid_is_initialized_with_correct_dimensions(self):
        self.assertEqual(self.game_grid.grid.shape, (10, 20))

    def test_game_grid_is_initialized_with_only_zeroes(self):
        self.assertTrue((self.game_grid.grid == np.zeros((10, 20))).all())
