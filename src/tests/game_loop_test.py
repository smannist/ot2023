import unittest
import numpy as np
from unittest.mock import Mock
from game_loop import GameLoop
from config import GAME_GRID_ROWS, GAME_GRID_COLUMNS, COLORS
from block_shapes import I

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.renderer_mock = Mock()
        self.display_mock = Mock()
        self.block_mock = Mock()
        self.highscore_service_mock = Mock()
        self.game_loop = GameLoop(self.renderer_mock, self.display_mock, self.block_mock, self.highscore_service_mock)

        self.block_mock.color = COLORS["T"]

        self.renderer_mock.game_grid.grid = np.array([[COLORS["dark_grey"] if (row + col) % 2 == 0
                                                   else COLORS["light_grey"] \
                                                   for col in range(GAME_GRID_COLUMNS)] \
                                                   for row in range(GAME_GRID_ROWS)])

    def test_block_collision_with_bottom_is_detected_correctly_for_non_I(self):
        # Set coordinates to match the bottom of the grid and assert
        self.game_loop.current_block.shape_to_coordinates.return_value = [
            (0, GAME_GRID_ROWS - 1), 
            (1, GAME_GRID_ROWS - 1), 
            (2, GAME_GRID_ROWS - 1), 
            (3, GAME_GRID_ROWS - 1)
        ]

        self.assertTrue(self.game_loop._collided_with_bottom(GAME_GRID_ROWS - 1, self.game_loop.current_block.shape_to_coordinates.return_value))

        # Test with coordinates outside the bottom and assert
        self.game_loop.current_block.shape_to_coordinates.return_value = [
            (0, GAME_GRID_ROWS - 2),
            (1, GAME_GRID_ROWS - 2), 
            (2, GAME_GRID_ROWS - 2), 
            (3, GAME_GRID_ROWS - 2)
        ]

        self.assertFalse(self.game_loop._collided_with_bottom(GAME_GRID_ROWS - 2, self.game_loop.current_block.shape_to_coordinates.return_value))

    def test_block_collision_with_bottom_is_detected_correctly_for_I(self):
        self.renderer_mock.game_grid.grid = np.array([[COLORS["dark_grey"] if (row + col) % 2 == 0
                                                   else COLORS["light_grey"] \
                                                   for col in range(GAME_GRID_COLUMNS)] \
                                                   for row in range(GAME_GRID_ROWS)])
        
        self.game_loop.current_block.shape = I

        # Set coordinates to match the bottom of the grid with I shape and assert
        self.game_loop.current_block.shape_to_coordinates.return_value = [
            (0, GAME_GRID_ROWS), 
            (1, GAME_GRID_ROWS), 
            (2, GAME_GRID_ROWS), 
            (3, GAME_GRID_ROWS)
        ]

        self.assertTrue(self.game_loop._collided_with_bottom(GAME_GRID_ROWS, self.game_loop.current_block.shape_to_coordinates.return_value))

        # Test with coordinates outside the bottom with I shape and assert
        self.game_loop.current_block.shape_to_coordinates.return_value = [
            (0, GAME_GRID_ROWS - 1),
            (1, GAME_GRID_ROWS - 1), 
            (2, GAME_GRID_ROWS - 1), 
            (3, GAME_GRID_ROWS - 1)
        ]

        self.assertFalse(self.game_loop._collided_with_bottom(GAME_GRID_ROWS-1, self.game_loop.current_block.shape_to_coordinates.return_value))

    def test_block_collision_with_another_block_is_detected_correctly(self):
        # Place a random block at position (x,y) -> (1,20)
        self.game_loop.placed_blocks = {(1,20): COLORS["T"]}

        # And matching coordinates for intersection
        self.game_loop.current_block.shape_to_coordinates.return_value = [
            (1,20),
            (3,19), 
            (4,18), 
            (5,18)
        ]

        self.assertTrue(self.game_loop._collided_with_block(self.game_loop.current_block.shape_to_coordinates.return_value, self.game_loop.placed_blocks))
