import numpy as np
from config import GAME_GRID_COLUMNS, GAME_GRID_ROWS, COLORS

class GameGrid:
    def __init__(self):
        self.rows = GAME_GRID_ROWS
        self.columns = GAME_GRID_COLUMNS
        self.grid = np.array([[COLORS["dark_grey"] if (row + col) % 2 == 0
                                                   else COLORS["light_grey"] \
                                                   for col in range(self.columns)] \
                                                   for row in range(self.rows)])
        self.score = 0

    def is_valid_move(self, block, placed_blocks):
        valid_moves = set((col, row) for row in range(GAME_GRID_ROWS) \
                                     for col in range(GAME_GRID_COLUMNS))

        blocks_on_grid = set(placed_blocks.keys())
        valid_moves -= blocks_on_grid
        block_positions = set(block.shape_to_coordinates())
        return block_positions.issubset(valid_moves)

    def reset_cell_colors(self, block_coordinates, placed_blocks):
        for col, row in block_coordinates:
            if (col, row) not in placed_blocks and row < self.rows:
                if (col + row) % 2 == 0:
                    self.grid[row][col] = COLORS["dark_grey"]
                else:
                    self.grid[row][col] = COLORS["light_grey"]
        self._update_grid(placed_blocks)

    def clear_rows(self, placed_blocks, block_landed=False):
        rows_to_clear = self._get_rows_to_clear(placed_blocks)

        if block_landed and rows_to_clear:
            self.score += 100*len(rows_to_clear)
            self._remove_rows_and_move(rows_to_clear, placed_blocks)
            self._add_new_top(placed_blocks)

        return placed_blocks, len(rows_to_clear) > 0

    def _remove_rows_and_move(self, rows_to_clear, placed_blocks):
        for row in rows_to_clear:
            self._remove_row(row, placed_blocks)
            self._move_blocks_down(row, placed_blocks)

    def _remove_row(self, row, placed_blocks):
        for col in range(self.columns):
            del placed_blocks[(col, row)]

    def _move_blocks_down(self, row, placed_blocks):
        for r in range(row-1, -1, -1):
            for c in range(self.columns):
                if (c, r) in placed_blocks:
                    color = placed_blocks.pop((c, r))
                    placed_blocks[(c, r+1)] = color
                else:
                    self.grid[r+1][c] = self.grid[r][c]

    def _add_new_top(self, placed_blocks):
        new_row = [COLORS["dark_grey"] if (col+1) % 2 == 0 else COLORS["light_grey"] \
                for col in range(self.columns)]

        for c in range(self.columns):
            if (c, 0) in placed_blocks:
                color = placed_blocks.pop((c, 0))
                placed_blocks[(c, 1)] = color
            else:
                self.grid[1][c] = self.grid[0][c]

        self.grid[0] = new_row

    def _get_rows_to_clear(self, placed_blocks):
        rows_to_clear = []

        for row in range(self.rows):
            if all((col, row) in placed_blocks for col in range(self.columns)):
                rows_to_clear.append(row)

        return rows_to_clear

    def _update_grid(self, placed_blocks):
        self.grid = np.array([[COLORS["dark_grey"] if (row + col) % 2 == 0 \
                              else COLORS["light_grey"] \
                              for col in range(self.columns)] \
                              for row in range(self.rows)])

        for coords, color in placed_blocks.items():
            col, row = coords
            self.grid[row][col] = color
