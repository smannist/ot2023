import numpy as np
from config import COLORS

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

# I rotations list is used just for testing now
I_rot = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]])

I_rot_2 = np.array([[0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]])

I_rot_3 = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]])

I_rot_list = [I, I_rot, I_rot_2, I_rot_3]

SHAPES = {0: [S, COLORS["S"]],
          1: [O, COLORS["O"]],
          2: [I, COLORS["I"]],
          3: [Z, COLORS["Z"]],
          4: [J, COLORS["J"]],
          5: [L, COLORS["L"]],
          6: [T, COLORS["T"]]}
