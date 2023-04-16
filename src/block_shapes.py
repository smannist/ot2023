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

I = np.array([[0, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 0]])

Z = np.array([[0, 0, 0, 0],
              [1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

L = np.array([[0, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 1, 1],
              [0, 0, 0, 0]])

J = np.array([[0, 0, 0, 0],
              [0, 0, 1, 0],
              [1, 1, 1, 0],
              [0, 0, 0, 0]])

T = np.array([[0, 0, 0, 0],
              [0, 1, 0, 0],
              [1, 1, 1, 0],
              [0, 0, 0, 0]])

SHAPES = {0: [S, BLOCK_COLORS["S"]],
          1: [O, BLOCK_COLORS["O"]],
          2: [I, BLOCK_COLORS["I"]],
          3: [Z, BLOCK_COLORS["Z"]],
          4: [J, BLOCK_COLORS["J"]],
          5: [L, BLOCK_COLORS["L"]],
          6: [T, BLOCK_COLORS["T"]]}
