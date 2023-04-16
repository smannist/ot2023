import pygame
from config import FALL_TIME, FALL_SPEED

class GameLoop:
    def __init__(self, renderer, display, block):
        self.renderer = renderer
        self.display = display
        self.clock = pygame.time.Clock()
        self.previous_tick = pygame.time.get_ticks()
        self.current_block = block
        self.previous_block_coordinates = [(0,0), (0,0), (0,0), (0,0)]
        self.fall_time = FALL_TIME
        self.fall_speed = FALL_SPEED

        self.key_pressed = False
        self.block_dropped = False

    def start(self):
        while True:
            if not self._handle_events():
                break

            block_coordinates = self.current_block.shape_to_coordinates()

            self._drop_block()
            self._block_moved(block_coordinates)
            self._update_elapsed_time()

            self.renderer.render_all(self.display)

            print(self.current_block.x, self.current_block.y)

            pygame.display.update()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if not self.key_pressed and not self.block_dropped:
                    self.key_pressed = True
                    self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                    if event.key == pygame.K_UP:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.rotate()
                            self.delay_timer = 500
                    elif event.key == pygame.K_DOWN:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_down()
                    elif event.key == pygame.K_LEFT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_left()
                    elif event.key == pygame.K_RIGHT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_right()
            elif event.type == pygame.KEYUP:
                self.key_pressed = False
        return True

    def _block_moved(self, current_block_coordinates):
        for i in range(len(current_block_coordinates)):
            x, y = current_block_coordinates[i]
            self.renderer.game_grid.grid[y][x] = self.current_block.color
            self.renderer.game_grid.reset_cell_colors(self.previous_block_coordinates, current_block_coordinates)

    def _drop_block(self):
        if self.fall_time/1000 >= self.fall_speed:
                self.block_dropped = True
                self.fall_time = 0
                self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                self.current_block.move_down()
                print(self.block_dropped)
                self.block_dropped = False

    def _update_elapsed_time(self):
        current_tick = pygame.time.get_ticks()
        elapsed_time = current_tick - self.previous_tick
        self.fall_time += elapsed_time
        self.previous_tick = current_tick
