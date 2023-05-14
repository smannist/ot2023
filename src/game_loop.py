import pygame
from pygame.locals import KEYDOWN, K_DOWN, K_UP, K_LEFT, K_RIGHT, QUIT
from block import Block
from config import FALL_TIME, FALL_SPEED, BLOCK_START_X, BLOCK_START_Y


class GameLoop:
    """A class that is responsible for running the main game loop for Tetris game.

    Attributes:
        renderer (object): handles the visualization of the game
        display (object): handles the window management
        block (object): represents the block on the game grid
        highscore_service (object): handles the saving and loading of highscores
    """

    def __init__(self, renderer, display, block, highscore_service):
        """Class constructor which creates a single game grid object


        Args:
            renderer (object): handles the visualization of the game
            display (object): handles the window management
            current_block (object): The current block on the game grid
            highscore_service (object): handles the saving and loading of highscores
            previous_tick (int): Time elapsed in milliseconds
            fall_time (int): Time since the current block started falling
            fall_speed (int): The interval in seconds between successive falls of the current block
            block_landed (bool): Whether or not the current block has landed on the game grid
            previous_rotation (numpy_array): Previous orientation of the current block
            placed_blocks (dict): A dictionary of currently placed blocks on the game grid
            next_block (object): The next block that will be generated
            score (int): The player's score
            difficulty (int): The current difficulty level of the game
        """
        self.renderer = renderer
        self.display = display
        self.current_block = block
        self.highscore_service = highscore_service
        self.previous_tick = pygame.time.get_ticks()
        self.fall_time = FALL_TIME
        self.fall_speed = FALL_SPEED
        self.block_landed = False
        self.previous_rotation = self.current_block.shape
        self.placed_blocks = {}
        self.next_block = self._spawn_next_block()
        self.score = 0
        self.difficulty = 2

    def start(self):
        """Starts the main game loop, running until the player either loses or quits the game
        """
        while True:
            self._render_all()

            if not self._handle_events():
                break

            block_coordinates = self.current_block.shape_to_coordinates()

            self._clear_rows(block_coordinates)

            if self.block_landed is True:
                self.block_landed = False

            self._reset_cells(block_coordinates)
            self._block_logic(block_coordinates)
            self._block_dropping()
            self._update_elapsed_time()
            self._increase_difficulty()
            self._update_score()

            if self._check_if_player_lost(self.placed_blocks):
                self._render_game_over()

                if self.score > 0:
                    self._add_highscore()
                    self._delete_lowest_highscore()

                self._render_highscores(
                    self.highscore_service.get_highscores())

                pygame.display.update()
                pygame.time.delay(3000)

                break

            pygame.display.update()

    def _handle_events(self):
        """Handles user events during the game loop, such as window closing or keyboard input.

        Returns:
            bool: False if the user closed the game window, True otherwise.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            if event.type == KEYDOWN:
                self._handle_keydown(event)
        return True

    def _handle_keydown(self, event):
        """Handles a keydown event during the game loop
           such as updating the current block's position based on the pressed key

        Args:
            event (pygame.event): pygame event object that represents the key pressed
        """
        if event.key == K_UP:
            self._handle_rotate_block()
        elif event.key == K_DOWN:
            self._handle_move_block_down()
        elif event.key == K_LEFT:
            self._handle_move_block_left()
        elif event.key == K_RIGHT:
            self._handle_move_block_right()

    def _handle_rotate_block(self):
        """Rotates the current block to its next orientation
           and checks that the rotation is valid
        """
        self.previous_rotation = self.current_block.shape
        self.current_block.rotate()

        if not self._is_valid_move():
            self.current_block.shape = self.previous_rotation

    def _handle_move_block_down(self):
        """Moves the current block down, validity check is not needed here
        """
        self.current_block.move_down()

    def _handle_move_block_left(self):
        """Moves the current block left and checks that the move is valid
        """
        self.current_block.move_left()

        if not self._is_valid_move():
            self.current_block.move_right()

    def _handle_move_block_right(self):
        """Moves the current block right and checks that the move is valid
        """
        self.current_block.move_right()

        if not self._is_valid_move():
            self.current_block.move_left()

    def _block_logic(self, current_block_coordinates):
        """Manages the movement of the current block and handles collision and placing
           of next block

        Args:
            current_block_coordinates (list): A list of (col, row) 
            tuples representing the current block's position.
        """
        for _, (col, row) in enumerate(current_block_coordinates):
            if self._block_collided(current_block_coordinates, row):
                self._handle_collision(current_block_coordinates)
                break

            self._move_block_on_grid(col, row)

    def _block_collided(self, current_block_coordinates, row):
        """Checks if the block has collided with the bottom or another block.
        
        Args:
            current_block_coordinates (list): A list of (col, row) 
            tuples representing the current block's position.
            row (int): The row index.

        Returns:
            bool: True if the block has collided, False otherwise.
        """
        return self._collided_with_bottom(row) or self._collided_with_block(current_block_coordinates, self.placed_blocks)

    def _handle_collision(self, current_block_coordinates):
        """Places current block on game grid and spawns next block

        Args:
            current_block_coordinates (list): A list of (col, row) 
            tuples representing the current block's position.
        """
        self._place_current_block(current_block_coordinates, y_offset=1)
        self.block_landed = True
        self.current_block = self.next_block
        self.next_block = self._spawn_next_block()

    def _move_block_on_grid(self, col, row):
        """Moves the block on the game grid by setting the colors on the 
           game grid to match the color of the current block
        
        Args:
            col (int): The column index.
            row (int): The row index.
        """
        if row >= 0:
            self.renderer.game_grid.grid[row][col] = self.current_block.color

    def _block_dropping(self):
        """Moves the current block down one row

        Returns:
            bool: True if the block was successfully moved down, False otherwise.
        """
        if self.fall_time >= self.fall_speed * 1000:
            self.fall_time = 0
            self.current_block.move_down()

    def _collided_with_bottom(self, row):
        """Checks if the current block has collided with the bottom of the game grid

        Args:
            row (int): Current row on the game rid
            current_block_coordinates (list): A list of (col, row)
            tuples representing the current block's position

        Returns:
            bool: True if the block has collided with the bottom of the game grid, False otherwise
        """
        if row == self.renderer.game_grid.grid.shape[0]:
            return True
        return False

    def _collided_with_block(self, current_block_coordinates, placed_blocks):
        """Checks if the current block has collided with any placed blocks on the game grid

        Args:
            current_block_coordinates (list): A list of (col, row)
            tuples representing the current block's position
            placed_blocks (dict): A dictionary of currently placed blocks on the game grid

        Returns:
            bool: True if the block collided with another block, False otherwise
        """
        current_block_set = set(current_block_coordinates)
        if current_block_set.intersection(placed_blocks):
            return True
        return False

    def _place_current_block(self, current_block_coordinates, y_offset=0, clear_block=False):
        """Places the current block onto the game grid by updating the placed_blocks dictionary

        Args:
            current_block_coordinates (list): A list of (col, row) 
            tuples representing the current block's position
            y_offset (int): The y offset for the coordinate
            clear_block (bool): True if the block cleared a row, False otherwise
        """
        if not clear_block:
            for col, row in current_block_coordinates:
                self.placed_blocks[(col, row-y_offset)
                                   ] = self.current_block.color

        for (c, r), color in self.placed_blocks.items():
            self.renderer.game_grid.grid[r][c] = color

    def _spawn_next_block(self):
        """Spawns a new random block

        Returns:
            Object: The next block object
        """
        return Block(BLOCK_START_X, BLOCK_START_Y)

    def _reset_cells(self, block_coordinates):
        """Resets the cells on the game grid

        Args:
            block_coordinates (list): A list of (col, row)
            tuples representing the current block's position
        """
        self.renderer.game_grid.reset_cell_colors(block_coordinates,
                                                  self.placed_blocks)

    def _clear_rows(self, block_coordinates):
        """Clears any full rows on the game grid

        Args:
            block_coordinates (list): A list of (col, row)
            tuples representing the current block's position
        """
        while self.renderer.game_grid.clear_rows(self.placed_blocks, self.block_landed)[1]:
            self._place_current_block(block_coordinates, clear_block=True)

    def _check_if_player_lost(self, placed_blocks):
        """Checks if the current block has landed on the top row of the game grid

        Args:
            placed_blocks (dict): A dictionary of currently placed blocks on the game grid

        Returns:
            bool: True if block hit the top, False otherwise.
        """
        for (_, row) in placed_blocks.keys():
            if row < 1:
                return True
        return False

    def _update_elapsed_time(self):
        """Updates the elapsed time
        """
        current_tick = pygame.time.get_ticks()
        elapsed_time = current_tick - self.previous_tick
        self.fall_time += elapsed_time
        self.previous_tick = current_tick

    def _increase_fall_speed(self, amount):
        """Increases the fall speed of the block being dropped, making the game more difficult

        Args:
            amount (float): The amount fall_speed will be decreased by
                            decreasing fall speed makes the block drop faster
        """
        self.fall_speed -= amount

    def _is_valid_move(self):
        """Checks if the move issued by the player is valid

        Returns:
            bool: True if the move is valid, False otherwise
        """
        return self.renderer.game_grid.is_valid_move(self.current_block,
                                                     self.placed_blocks)

    def _update_score(self):
        """Updates player score
        """
        self.score = self.renderer.game_grid.score

    def _render_all(self):
        """Renders all base components to the game window
        """
        self.renderer.render_all(self.display, self.next_block, self.score)

    def _render_game_over(self):
        """Renders the game over text
        """
        self.renderer.render_game_over_txt(self.display)

    def _render_highscores(self, highscore):
        """Renders the highscore text

        Args:
            highscore (list): list of current highscores in a form of dict
        """
        self.renderer.render_highscores(self.display, highscore)

    def _add_highscore(self):
        """Adds a highscore if it meets the criteria
        """
        self.highscore_service.add_highscore(self.score)

    def _delete_lowest_highscore(self):
        """Deletes the lowest highscore from database
        """
        self.highscore_service.delete_lowest()

    def _increase_difficulty(self):
        """Increases fall speed based on elapsed time and current
           difficulty value
        """
        if self.previous_tick >= self.difficulty * 1000:
            self._increase_fall_speed(0.01)
            self.difficulty += 5
