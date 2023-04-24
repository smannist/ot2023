import random
import numpy as np
from block_shapes import SHAPES

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape_info_list = random.choice(SHAPES)
        self.shape = self.shape_info_list[0]
        self.color = self.shape_info_list[1]

    def shape_to_coordinates(self):
        row, col = np.where(self.shape == 1)
        coordinates = list(zip(self.x + col - 2, self.y + row - 4))
        return coordinates

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def rotate(self):
        rotated_shape = np.transpose(self.shape)
        rotated_shape = np.flip(rotated_shape, axis=0)
        self.shape = rotated_shape
