import unittest
import numpy as np
from src.game_grid import GameGrid
from src.block import Block
from src.config import COLORS, GAME_GRID_COLUMNS


class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.game_grid = GameGrid()
        self.block = Block(5, 3)
        self.placed_blocks = {}
        self.placed_blocks_full_row = {
            (j, 5): COLORS["T"] for j in range(GAME_GRID_COLUMNS)}

    def test_game_grid_is_initialized_with_correct_dimensions(self):
        self.assertEqual(self.game_grid.grid.shape, (21, 11, 3))

    def test_game_grid_is_initialized_with_correct_colors(self):
        grid_colors = np.array([self.game_grid.grid[row][col] for row in range(
            self.game_grid.rows) for col in range(self.game_grid.columns)])
        expected_colors = np.array([COLORS["dark_grey"] if (row + col) % 2 == 0 else COLORS["light_grey"]
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

        self.game_grid.reset_cell_colors(
            current_block_coordinates, self.placed_blocks)

        expected_colors = [COLORS["dark_grey"] if (
            coord[0] + coord[1]) % 2 == 0 else COLORS["light_grey"] for coord in previous_block_coordinates]
        actual_colors = [self.game_grid.grid[coord[1]][coord[0]]
                         for coord in previous_block_coordinates]
        self.assertTrue(np.array_equal(expected_colors, actual_colors))

    def test_cell_colors_are_updated_correctly(self):
        placed_blocks = {(2, 0): (255, 0, 0),
                         (1, 1): (0, 255, 0),
                         (2, 2): (0, 0, 255)}

        self.game_grid._update_grid(placed_blocks)

        for row in range(self.game_grid.grid.shape[0]):
            for col in range(self.game_grid.grid.shape[1]):
                if (col + row) % 2 == 0 and (col, row) not in placed_blocks:
                    assert np.all(
                        self.game_grid.grid[row][col] == COLORS["dark_grey"])
                elif (col, row) not in placed_blocks:
                    assert np.all(
                        self.game_grid.grid[row][col] == COLORS["light_grey"])
                else:
                    assert np.all(
                        self.game_grid.grid[row][col] == placed_blocks[(col, row)])

    def test_remove_full_rows_is_removed_correctly(self):
        self.game_grid._remove_row(5, self.placed_blocks_full_row)
        self.assertNotIn((5, 9), self.placed_blocks_full_row.keys())

    def test_blocks_are_moved_down_accordingly(self):
        self.game_grid._move_blocks_down(6, self.placed_blocks_full_row)
        self.assertIn((0, 6), self.placed_blocks_full_row.keys())

    def test_full_rows_are_found_correctly_for_clearing(self):
        self.assertEqual(
            len(self.game_grid._get_rows_to_clear(self.placed_blocks_full_row)), 1)

    def test_adding_new_row_to_the_top_of_the_game_grid(self):
        expected_row = np.array([COLORS["dark_grey"] if (
            col+1) % 2 == 0 else COLORS["light_grey"] for col in range(GAME_GRID_COLUMNS)])
        self.game_grid._add_new_top()
        self.assertTrue(np.array_equal(self.game_grid.grid[0], expected_row))

    def test_score_is_updated_when_rows_are_cleared(self):
        rows_to_clear = [19]
        self.game_grid._update_score(len(rows_to_clear))
        self.assertEqual(self.game_grid.score, 100)
