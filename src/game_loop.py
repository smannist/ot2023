import pygame
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
        self.previous_rotation = self.current_block.shape

    def start(self):
        while True:
            self.renderer.render_all(self.display)

            if not self._handle_events():
                break

            block_coordinates = self.current_block.shape_to_coordinates()

            self._block_moved(block_coordinates)
            self._drop_block(block_coordinates)
            self._update_elapsed_time()

            pygame.display.update()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if not self.key_pressed:
                    self.key_pressed = True
                    self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                    if event.key == pygame.K_UP:
                        self.previous_rotation = self.current_block.shape
                        self.current_block.rotate()
                        if not self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.shape = self.previous_rotation
                    elif event.key == pygame.K_DOWN:
                        self.current_block.move_down()
                        if not self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_up()
                    elif event.key == pygame.K_LEFT:
                        self.current_block.move_left()
                        if not self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_right()
                    elif event.key == pygame.K_RIGHT:
                        self.current_block.move_right()
                        if not self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_left()
            elif event.type == pygame.KEYUP:
                self.key_pressed = False
        return True

    def _block_moved(self, current_block_coordinates):
        self.renderer.game_grid.reset_cell_colors(self.previous_block_coordinates, current_block_coordinates)
        for i in range(len(current_block_coordinates)):
            x, y = current_block_coordinates[i]
            self.renderer.game_grid.grid[y][x] = self.current_block.color
        self.renderer.game_grid.reset_cell_colors(self.previous_block_coordinates, current_block_coordinates)

    def _drop_block(self, current_block_coordinates):
        if self.fall_time/1000 >= self.fall_speed:
                self.renderer.game_grid.reset_cell_colors(self.previous_block_coordinates, current_block_coordinates)
                self.fall_time = 0
                self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                self.current_block.move_down()

    def _update_elapsed_time(self):
        current_tick = pygame.time.get_ticks()
        elapsed_time = current_tick - self.previous_tick
        self.fall_time += elapsed_time
        self.previous_tick = current_tick
