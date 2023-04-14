import numpy as np
from config import GAME_GRID_COLUMNS, GAME_GRID_ROWS, BACKGROUND_COLORS

class GameGrid:
    def __init__(self):
        self.rows = GAME_GRID_ROWS
        self.columns = GAME_GRID_COLUMNS
        self.grid = self._initialize_grid()

    def _initialize_grid(self):
        grid = np.full((self.rows, self.columns, 3), (0, 0, 0), dtype=int)

        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                if (row + col) % 2 == 0:
                    grid[row][col] = BACKGROUND_COLORS["dark_grey"]
                else:
                    grid[row][col] = BACKGROUND_COLORS["light_grey"]

        return grid

    def update(self, positions):
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                if (row, col) in positions:
                    self.grid[row][col] = positions[(row, col)] # color of the block e.g (x,y) --> (1,2): RGB --> (255,0,0), not used yet (and not sure if works anyway)

    def is_valid_move(self, block):
        valid_moves = [(j, i) for i in range(GAME_GRID_ROWS) for j in range(GAME_GRID_COLUMNS) if np.array_equal(self.grid[i][j], np.array([0, 0, 0]))]
        print(valid_moves)
        block_positions = block.shape_to_position()

        for position in block_positions:
            print(position)
            if position not in valid_moves:
                return False

        return True
