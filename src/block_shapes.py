import numpy as np
from config import BLOCK_COLORS

S = np.array([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [1, 1, 0, 0],
              [0, 0, 0, 0]])

O = np.array([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

SHAPES = {0: [S, BLOCK_COLORS["S"]],
          1: [O, BLOCK_COLORS["O"]]}
