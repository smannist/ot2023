import numpy as np

class GameGrid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        return np.zeros((self.rows, self.columns))
