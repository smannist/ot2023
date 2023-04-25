import unittest
import numpy as np
from src.game_grid import GameGrid
from src.block import Block
from src.config import BACKGROUND_COLORS

class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.game_grid = GameGrid()
        self.block = Block(5,3)
        self.placed_blocks = {}

    def test_game_grid_is_initialized_with_correct_dimensions(self):
        self.assertEqual(self.game_grid.grid.shape, (21, 11, 3))

    def test_game_grid_is_initialized_with_correct_colors(self):
        grid_colors = np.array([self.game_grid.grid[row][col] for row in range(self.game_grid.rows) for col in range(self.game_grid.columns)])
        expected_colors = np.array([BACKGROUND_COLORS["dark_grey"] if (row + col) % 2 == 0 else BACKGROUND_COLORS["light_grey"] \
                                                for row in range(self.game_grid.rows) for col in range(self.game_grid.columns)])
        self.assertTrue(np.array_equal(grid_colors, expected_colors))

    def test_valid_block_moves_are_accepted(self):
        block = Block(5, 3)
        result = self.game_grid.is_valid_move(block, self.placed_blocks)
        self.assertTrue(result)

    def test_invalid_block_moves_are_rejected(self):
        block = Block(15, 3)
        result = self.game_grid.is_valid_move(block, self.placed_blocks)
        self.assertFalse(result)

    def test_cell_colors_on_the_grid_are_reset_correcty(self):
        current_block_coordinates = self.block.shape_to_coordinates()
        previous_block_coordinates = self.block.shape_to_coordinates()

        self.block.move_down()

        current_block_coordinates = self.block.shape_to_coordinates()

        self.game_grid.reset_cell_colors(previous_block_coordinates, current_block_coordinates, self.placed_blocks)

        expected_colors = [BACKGROUND_COLORS["dark_grey"] if (coord[0] + coord[1]) % 2 == 0 else BACKGROUND_COLORS["light_grey"] for coord in previous_block_coordinates]
        actual_colors = [self.game_grid.grid[coord[1]][coord[0]] for coord in previous_block_coordinates]
        self.assertTrue(np.array_equal(expected_colors, actual_colors))
