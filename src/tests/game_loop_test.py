import unittest
import numpy as np
from unittest.mock import Mock
from game_loop import GameLoop
from config import GAME_GRID_ROWS, GAME_GRID_COLUMNS, COLORS
from block_shapes import I, I_rot_list
from block import Block
from renderer import Renderer
from game_grid import GameGrid

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.renderer_mock = Mock()
        self.display_mock = Mock()

        self.block_mock = Mock()
        self.block = Block(5,10)

        self.highscore_service_mock = Mock()

        self.game_loop = GameLoop(self.renderer_mock, self.display_mock, self.block_mock, self.highscore_service_mock)
        self.game_loop_no_block_mock = GameLoop(self.renderer_mock, self.display_mock, self.block, self.highscore_service_mock)

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

    def test_block_is_moved_down_correctly_on_the_game_grid_when_move_is_valid(self):
        self.game_loop_no_block_mock._handle_move_block_down()
        self.assertEqual(self.game_loop_no_block_mock.current_block.y, 11)

    def test_block_is_moved_left_correctly_on_the_game_grid_when_move_is_valid(self):
        self.game_loop_no_block_mock._handle_move_block_left()
        self.assertEqual(self.game_loop_no_block_mock.current_block.x, 4)

    def test_block_is_moved_right_correctly_on_the_game_grid_when_move_is_valid(self):
        self.game_loop_no_block_mock._handle_move_block_right()
        self.assertEqual(self.game_loop_no_block_mock.current_block.x, 6)

    def test_block_is_not_moved_left_on_the_game_grid_when_move_is_not_valid(self):
        renderer = Renderer(self.display_mock, GameGrid())
        self.game_loop = GameLoop(renderer, self.display_mock, Block(GAME_GRID_ROWS-1, 0), self.highscore_service_mock)
        self.game_loop._handle_move_block_left()
        self.assertEqual(self.game_loop.current_block.x, GAME_GRID_ROWS-1)

    def test_block_is_not_moved_right_on_the_game_grid_when_move_is_not_valid(self):
        renderer = Renderer(self.display_mock, GameGrid())
        self.game_loop = GameLoop(renderer, self.display_mock, Block(0, 0), self.highscore_service_mock)
        self.game_loop._handle_move_block_right()
        self.assertEqual(self.game_loop.current_block.x, 0)
    
    def test_block_is_rotated_correctly_on_the_game_grid_when_move_is_valid(self):
        self.game_loop_no_block_mock.current_block.shape = I
        self.game_loop_no_block_mock._handle_rotate_block()
        expected_shape = I_rot_list[3]
        actual_shape = self.game_loop_no_block_mock.current_block.shape
        self.assertTrue(np.array_equal(expected_shape, actual_shape))

    def test_block_is_not_rotated_if_the_move_is_not_valid(self):
        renderer = Renderer(self.display_mock, GameGrid())
        self.game_loop = GameLoop(renderer, self.display_mock, Block(0, 5), self.highscore_service_mock)
        self.game_loop.current_block.shape = I
        self.game_loop._handle_rotate_block()
        expected_shape = I_rot_list[0]
        actual_shape = self.game_loop.current_block.shape
        self.assertTrue(np.array_equal(expected_shape, actual_shape))
