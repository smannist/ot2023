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
        coordinates = []
        block_shape_list = self.shape.tolist()

        for i, row in enumerate(block_shape_list):
            for j, col in enumerate(row):
                if col == 1:
                    coordinates.append((self.x + j, self.y + i))

        for i, coord in enumerate(coordinates):
            coordinates[i] = (coord[0] - 2, coord[1] - 4)

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
