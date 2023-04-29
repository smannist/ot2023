import pygame
import numpy as np
from pygame.locals import KEYDOWN, K_DOWN, K_UP, K_LEFT, K_RIGHT, QUIT
from block import Block
from config import FALL_TIME, FALL_SPEED
from block_shapes import I_rot_list

class GameLoop:
    def __init__(self, renderer, display, block, highscore_service):
        self.renderer = renderer
        self.display = display
        self.current_block = block
        self.highscore_service = highscore_service
        self.previous_tick = pygame.time.get_ticks()
        self.fall_time = FALL_TIME
        self.fall_speed = FALL_SPEED
        self.is_dropping = False
        self.block_landed = False
        self.previous_rotation = self.current_block.shape
        self.placed_blocks = {}
        self.next_block = self._spawn_next_block()
        self.score = 0
        self.difficulty = 2

    def start(self):
        while True:
            self._render_all()

            if not self._handle_events():
                break

            block_coordinates = self.current_block.shape_to_coordinates()

            self._clear_rows(block_coordinates)

            if self.block_landed is True:
                self.block_landed = False

            self._reset_cells(block_coordinates)
            self._block_movement(block_coordinates)
            self._block_dropping()
            self._update_elapsed_time()
            self._increase_difficulty()
            self._update_score()

            if self._check_if_player_lost(self.placed_blocks):
                self._render_game_over()

                if self.score > 0:
                    self._add_highscore()

                self._render_highscores(self.highscore_service.get_highscores())
                pygame.display.update()
                pygame.time.delay(3000)
                break

            pygame.display.update()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            if event.type == KEYDOWN and not self.is_dropping:
                self._handle_keydown(event)
        return True

    def _handle_keydown(self, event):
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

        if not self._is_valid_move():
            self.current_block.shape = self.previous_rotation

    def _handle_move_block_down(self):
        self.current_block.move_down()

        if not self._is_valid_move():
            self.current_block.move_up()

    def _handle_move_block_left(self):
        self.current_block.move_left()

        if not self._is_valid_move():
            self.current_block.move_right()

    def _handle_move_block_right(self):
        self.current_block.move_right()

        if not self._is_valid_move():
            self.current_block.move_left()

    def _block_movement(self, current_block_coordinates):
        for _, (col, row) in enumerate(current_block_coordinates):
            if self._collided_with_bottom(row, current_block_coordinates) \
                    or self._collided_with_block(current_block_coordinates, self.placed_blocks):
                self.block_landed = True
                self.current_block = self.next_block
                self.next_block = self._spawn_next_block()
                break
            if row >= 0:
                self.renderer.game_grid.grid[row][col] = self.current_block.color

    def _block_dropping(self):
        if self.fall_time >= self.fall_speed * 1000:
            self.is_dropping = True
            self.fall_time = 0
            self.current_block.move_down()
        else:
            self.is_dropping = False

    def _collided_with_bottom(self, row, current_block_coordinates):
        if row == self.renderer.game_grid.grid.shape[0]:
            if any(np.array_equal(self.current_block.shape, shape) for shape in I_rot_list):
                self._place_current_block(current_block_coordinates, y_offset=1)
                return True

        if row == self.renderer.game_grid.grid.shape[0]-1:
            if not any(np.array_equal(self.current_block.shape, shape) for shape in I_rot_list):
                self._place_current_block(current_block_coordinates)
                return True

        return False

    def _collided_with_block(self, current_block_coordinates, placed_blocks):
        current_block_set = set(current_block_coordinates)
        if current_block_set.intersection(placed_blocks):
            self._place_current_block(current_block_coordinates, y_offset=1)
            return True
        return False

    def _place_current_block(self, current_block_coordinates, y_offset=0, clear_block=False):
        if not clear_block:
            for col, row in current_block_coordinates:
                self.placed_blocks[(col, row-y_offset)] = self.current_block.color

        for (c, r), color in self.placed_blocks.items():
            self.renderer.game_grid.grid[r][c] = color

    def _spawn_next_block(self):
        return Block(5,0)

    def _reset_cells(self, block_coordinates):
        self.renderer.game_grid.reset_cell_colors(block_coordinates, \
                                                  self.placed_blocks)

    def _clear_rows(self, block_coordinates):
        while self.renderer.game_grid.clear_rows(self.placed_blocks, self.block_landed)[1]:
            self._place_current_block(block_coordinates, clear_block=True)

    def _check_if_player_lost(self, placed_blocks):
        for (_, row) in placed_blocks.keys():
            if row < 1:
                return True
        return False

    def _update_elapsed_time(self):
        current_tick = pygame.time.get_ticks()
        elapsed_time = current_tick - self.previous_tick
        self.fall_time += elapsed_time
        self.previous_tick = current_tick

    def _increase_fall_speed(self, amount):
        self.fall_speed -= amount

    def _is_valid_move(self):
        return self.renderer.game_grid.is_valid_move(self.current_block, \
                                                    self.placed_blocks)

    def _update_score(self):
        self.score = self.renderer.game_grid.score

    def _render_all(self):
        self.renderer.render_all(self.display, self.next_block, self.score)

    def _render_game_over(self):
        self.renderer.render_game_over_txt(self.display)

    def _render_highscores(self , highscore):
        self.renderer.render_highscores(self.display, highscore)

    def _add_highscore(self):
        self.highscore_service.add_highscore(self.score)

    def _increase_difficulty(self):
        if self.previous_tick >= self.difficulty * 1000:
            self._increase_fall_speed(0.01)
            self.difficulty += 5
