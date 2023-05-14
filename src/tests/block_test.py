import unittest
import numpy as np
from src.block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(5, 3)

    def test_block_moves_down_correctly(self):
        self.block.move_down()
        self.assertEqual(self.block.y, 4)

    def test_block_moves_up_correctly(self):
        self.block.move_up()
        self.assertEqual(self.block.y, 2)

    def test_block_moves_right_correctly(self):
        self.block.move_right()
        self.assertEqual(self.block.x, 6)

    def test_block_moves_left_correctly(self):
        self.block.move_left()
        self.assertEqual(self.block.x, 4)

    def test_block_is_rotated_correctly(self):
        self.block.shape = np.array([[0, 0, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 0, 0, 0]])

        expected_block_shape = np.array([[0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0],
                                         [0, 1, 1, 1, 1, 0],
                                         [0, 0, 0, 0, 0, 0]])

        self.block.rotate()
        self.assertTrue(np.array_equal(self.block.shape, expected_block_shape))
