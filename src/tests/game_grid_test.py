import unittest
import numpy as np
from src.game_grid import GameGrid
from src.config import BACKGROUND_COLORS

class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.game_grid = GameGrid()

    def test_game_grid_is_initialized_with_correct_dimensions(self):
        self.assertEqual(self.game_grid.grid.shape, (21, 11, 3))

    def test_game_grid_is_initialized_with_correct_colors(self):
        grid_colors = np.array([self.game_grid.grid[row][col] for row in range(self.game_grid.rows) for col in range(self.game_grid.columns)])
        expected_colors = np.array([BACKGROUND_COLORS["dark_grey"] if (row + col) % 2 == 0 else BACKGROUND_COLORS["light_grey"] \
                                                for row in range(self.game_grid.rows) for col in range(self.game_grid.columns)])
        self.assertTrue(np.array_equal(grid_colors, expected_colors))
