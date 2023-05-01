import numpy as np
from config import GAME_GRID_COLUMNS, GAME_GRID_ROWS, COLORS


class GameGrid:
    """Class which represents the game grid
    """

    def __init__(self):
        """Class constructor which creates a single game grid object

        Args:
            rows (int): Number of rows on the game grid
            columns (int): Number of columns on the game grid
            grid (numpy_array): The grid itself
            score (int): Amount of points earned by the player
        """
        self.rows = GAME_GRID_ROWS
        self.columns = GAME_GRID_COLUMNS
        self.grid = np.array([[COLORS["dark_grey"] if (row + col) % 2 == 0 else COLORS["light_grey"]
                             for col in range(self.columns)] for row in range(self.rows)])
        self.score = 0

    def is_valid_move(self, block, placed_blocks):
        """Checks if the move issued by the player is valid

        Args:
            block (object): Current block object on the game grid
            placed_blocks (dict): Currently placed blocks on the game grid

        Returns:
            bool: True if the current block position is a subset of valid moves
                  else false
        """
        valid_moves = set((col, row) for row in range(GAME_GRID_ROWS)
                          for col in range(GAME_GRID_COLUMNS))

        blocks_on_grid = set(placed_blocks.keys())
        valid_moves -= blocks_on_grid
        block_positions = set(block.shape_to_coordinates())
        return block_positions.issubset(valid_moves)

    def reset_cell_colors(self, block_coordinates, placed_blocks):
        """Resets the cell colors based on block coordinates
           and currently placed blocks

        Args:
            block_coordinates (list): 4 coordinate tuples e.g [(1,1), (1,1), (1,1), (1,1)]
            placed_blocks (dict): Currently placed blocks on the game grid
        """
        for col, row in block_coordinates:
            if (col, row) not in placed_blocks and row < self.rows:
                if (col + row) % 2 == 0:
                    self.grid[row][col] = COLORS["dark_grey"]
                else:
                    self.grid[row][col] = COLORS["light_grey"]
        self._update_grid(placed_blocks)

    def clear_rows(self, placed_blocks, block_landed=False):
        """Clears any full rows on the game grid and updates score

        Args:
            placed_blocks (dict): Currently placed blocks on the game grid
            block_landed (bool): True if block has landed else false

        Returns:
            tuple: dictionary of current blocks on game grid
                   and if any clearable rows were found i.e
                   dict, True
        """
        rows_to_clear = self._get_rows_to_clear(placed_blocks)

        if block_landed and rows_to_clear:
            self._update_score(rows_to_clear)
            self._remove_rows_and_move(rows_to_clear, placed_blocks)
            self._add_new_top()

        return placed_blocks, len(rows_to_clear) > 0

    def _remove_rows_and_move(self, rows_to_clear, placed_blocks):
        """Removes full rows and move the placed blocks down

        Args:
            rows_to_clear (list): Full rows in need of clearing
            placed_blocks (dict): Currently placed blocks on the game grid
        """
        for row in rows_to_clear:
            self._remove_row(row, placed_blocks)
            self._move_blocks_down(row, placed_blocks)

    def _remove_row(self, row, placed_blocks):
        """Removes a single game grid row

        Args:
            row (int): Row to be removed
            placed_blocks (dict): Currently placed blocks on the game grid
        """
        for col in range(self.columns):
            del placed_blocks[(col, row)]

    def _move_blocks_down(self, row, placed_blocks):
        """Moves the blocks on the placed block dictionary down

        Args:
            row (int): Row to be removed
            placed_blocks (dict): Currently placed blocks on the game grid
        """
        for r in range(row-1, -1, -1):
            for c in range(self.columns):
                if (c, r) in placed_blocks:
                    color = placed_blocks.pop((c, r))
                    placed_blocks[(c, r+1)] = color

    def _add_new_top(self):
        """Adds a new row on top of the grid

        Args:
            placed_blocks (dict): Currently placed blocks on the game grid
        """
        self.grid[0] = [COLORS["dark_grey"] if (
            col+1) % 2 == 0 else COLORS["light_grey"] for col in range(self.columns)]

    def _get_rows_to_clear(self, placed_blocks):
        """Checks if the grid currently contains any full rows

        Args:
            placed_blocks (dict): Currently placed blocks on the game grid

        Returns:
            list: Any rows that need clearing as integer values
        """
        rows_to_clear = []

        for row in range(self.rows):
            if all((col, row) in placed_blocks for col in range(self.columns)):
                rows_to_clear.append(row)

        return rows_to_clear

    def _update_grid(self, placed_blocks):
        """Updates the cell colors on the grid

        Args:
            placed_blocks (dict): Currently placed blocks on the game grid
        """
        self.grid = np.array([[COLORS["dark_grey"] if (row + col) % 2 == 0 else COLORS["light_grey"]
                             for col in range(self.columns)] for row in range(self.rows)])

        for coords, color in placed_blocks.items():
            col, row = coords
            self.grid[row][col] = color

    def _update_score(self, rows_to_clear):
        """Updates the score based on the number of cleared rows
           100 points for each row

        Args:
            rows_to_clear (list): Cleared rows as a list
        """
        self.score += 100*len(rows_to_clear)
