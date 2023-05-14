import random
import numpy as np
from block_shapes import SHAPES


class Block:
    """Class which represents a single block object in the game

    Attributes:
        x (int): X-coordinate position of the block
        y (int): Y-cooordinate position of the block
    """

    def __init__(self, x, y):
        """Class constructor which creates a single block object

        Args:
            x (int): X-coordinate position of the block
            y (int): Y-cooordinate position of the block
            shape_info_list (list): A list containing the shape and color of the block
            shape (numpy_array): Shape of the block
            color (tuple): Color of the block in RGBA format e.g (0,255,0)
        """
        self.x = x
        self.y = y
        self.shape_info_list = random.choice(SHAPES)
        self.shape = self.shape_info_list[0]
        self.color = self.shape_info_list[1]

    def shape_to_coordinates(self):
        """Translates the shape of a block into a list of coordinates

        Returns:
            list: 4 coordinate tuples e.g [(1,1), (1,1), (1,1), (1,1)] 
        """
        row, col = np.where(self.shape == 1)
        coordinates = list(zip(self.x + col - 2, self.y + row - 4))
        return coordinates

    def move_down(self):
        """Increases the y-coordinate of the block by 1
        """
        self.y += 1

    def move_left(self):
        """Decreases the x-coordinate of the block by 1
        """
        self.x -= 1

    def move_right(self):
        """Increases the x-coordinate of the block by 1
        """
        self.x += 1

    def move_up(self):
        """Decreases the y-coordinate of the block by 1
        """
        self.y -= 1

    def rotate(self):
        """Rotates the shape of the block by 90 degrees and flips the array
        """
        rotated_shape = np.transpose(self.shape)
        rotated_shape = np.flip(rotated_shape, axis=0)
        self.shape = rotated_shape
