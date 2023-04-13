import numpy as np
from config import GAME_GRID_COLUMNS, GAME_GRID_ROWS

class GameGrid:
    def __init__(self):
        self.rows = GAME_GRID_ROWS
        self.columns = GAME_GRID_COLUMNS
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        return np.zeros((self.rows, self.columns))
