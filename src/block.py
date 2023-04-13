import random
from block_shapes import SHAPES
from config import SHAPE_COLORS

class Block:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPE_COLORS[shape]
        self.rotation = 0
