import pygame
from pygame.locals import KEYDOWN, KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, QUIT
from block import Block
from config import FALL_TIME, FALL_SPEED

class GameLoop:
    def __init__(self, renderer, display, block):
        self.renderer = renderer
        self.display = display
        self.previous_tick = pygame.time.get_ticks()
        self.current_block = block
        self.previous_block_coordinates = [(0,0), (0,0), (0,0), (0,0)]
        self.fall_time = FALL_TIME
        self.fall_speed = FALL_SPEED
        self.key_pressed = False
        self.is_dropping = False
        self.previous_rotation = self.current_block.shape
        self.placed_blocks = {}

    def start(self):
        while True:
            self.renderer.render_all(self.display)

            if not self._handle_events():
                break

            block_coordinates = self.current_block.shape_to_coordinates()

            self.renderer.game_grid.reset_cell_colors(self.previous_block_coordinates, \
                                                      block_coordinates, \
                                                      self.placed_blocks)

            self._update_elapsed_time()
            self._block_movement(block_coordinates)
            self._block_dropping()

            pygame.display.update()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            if event.type == KEYDOWN and not self.is_dropping:
                self._handle_keydown(event)
            elif event.type == KEYUP:
                self.key_pressed = False
        return True

    def _handle_keydown(self, event):
        if not self.key_pressed:
            self.key_pressed = True
            self.previous_block_coordinates = self.current_block.shape_to_coordinates()
            if event.key == K_UP:
                self._handle_rotate_block()
            elif event.key == K_DOWN:
                self._handle_move_block_down()
            elif event.key == K_LEFT:
                self._handle_move_block_left()
            elif event.key == K_RIGHT:
                self._handle_move_block_right()

    def _handle_rotate_block(self):
        self.previous_rotation = self.current_block.shape
        self.current_block.rotate()

        if not self.renderer.game_grid.is_valid_move(self.current_block, self.placed_blocks):
            self.current_block.shape = self.previous_rotation

    def _handle_move_block_down(self):
        self.current_block.move_down()

        if not self.renderer.game_grid.is_valid_move(self.current_block, self.placed_blocks):
            self.current_block.move_up()

    def _handle_move_block_left(self):
        self.current_block.move_left()

        if not self.renderer.game_grid.is_valid_move(self.current_block, self.placed_blocks):
            self.current_block.move_right()

    def _handle_move_block_right(self):
        self.current_block.move_right()

        if not self.renderer.game_grid.is_valid_move(self.current_block, self.placed_blocks):
            self.current_block.move_left()

    def _block_movement(self, current_block_coordinates):
        for _, (row, col) in enumerate(current_block_coordinates):
            if self._collided_with_bottom(col, current_block_coordinates) \
                    or self._collided_with_block(current_block_coordinates, self.placed_blocks):
                self._spawn_next_block()
                break
            self.renderer.game_grid.grid[col][row] = self.current_block.color

    def _block_dropping(self):
        if self.fall_time >= self.fall_speed * 1000:
            self.is_dropping = True
            self.fall_time = 0
            self.previous_block_coordinates = self.current_block.shape_to_coordinates()
            self.current_block.move_down()
        else:
            self.is_dropping = False

    def _collided_with_bottom(self, col, current_block_coordinates):
        if col == self.renderer.game_grid.grid.shape[0]-1:
            self._place_current_block(current_block_coordinates)
            return True
        return False

    def _collided_with_block(self, current_block_coordinates, placed_blocks):
        current_block_set = set(current_block_coordinates)
        if current_block_set.intersection(placed_blocks):
            self._place_current_block(current_block_coordinates, c_fact=1)
            return True
        return False

    def _place_current_block(self, current_block_coordinates, c_fact=0):
        for r, c in current_block_coordinates:
            self.placed_blocks[(r, c-c_fact)] = self.current_block.color
        for (r, c), color in self.placed_blocks.items():
            self.renderer.game_grid.grid[c][r] = color

    def _spawn_next_block(self):
        self.current_block = Block(5,3)

    def _update_elapsed_time(self):
        current_tick = pygame.time.get_ticks()
        elapsed_time = current_tick - self.previous_tick
        self.fall_time += elapsed_time
        self.previous_tick = current_tick
