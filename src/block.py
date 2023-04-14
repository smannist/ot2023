import random
from block_shapes import SHAPES

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape_info_list = random.choice(SHAPES)
        self.shape = self.shape_info_list[0]
        self.color = self.shape_info_list[1]
        self.rotation = 0

    def shape_to_coordinates(self):
        coordinates = []
        block_shape_list = self.shape.tolist()

        for i in range(len(block_shape_list)):
            for j in range(len(block_shape_list[0])):
                if block_shape_list[i][j] == 1:
                    coordinates.append((self.x + j, self.y + i))

        for i in range(len(coordinates)):
            coordinates[i] = (coordinates[i][0] - 2, coordinates[i][1] - 4)

        return coordinates
