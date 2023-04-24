import numpy as np
from config import GAME_GRID_COLUMNS, GAME_GRID_ROWS, BACKGROUND_COLORS

class GameGrid:
    def __init__(self):
        self.rows = GAME_GRID_ROWS
        self.columns = GAME_GRID_COLUMNS
        self.grid = self._initialize_grid()

    def _initialize_grid(self):
        grid = np.full((self.rows, self.columns, 3), (0, 0, 0))

        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                if (row + col) % 2 == 0:
                    grid[row][col] = BACKGROUND_COLORS["dark_grey"]
                else:
                    grid[row][col] = BACKGROUND_COLORS["light_grey"]

        return grid

    def is_valid_move(self, block, placed_blocks):
        valid_moves = set((col, row) for row in range(GAME_GRID_ROWS) for col in range(GAME_GRID_COLUMNS))
        blocks_on_grid = set(placed_blocks.keys())
        valid_moves -= blocks_on_grid
        block_positions = set(block.shape_to_coordinates())
        return block_positions.issubset(valid_moves)

    def reset_cell_colors(self, previous_block_coordinates, block_coordinates, placed_blocks):
        for row, col in previous_block_coordinates:
            if (row, col) not in block_coordinates and (row, col) not in placed_blocks:
                if (row + col) % 2 == 0:
                    self.grid[col][row] = BACKGROUND_COLORS["dark_grey"]
                else:
                    self.grid[col][row] = BACKGROUND_COLORS["light_grey"]
