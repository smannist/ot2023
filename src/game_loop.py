import pygame
from block import Block

class GameLoop:
    def __init__(self, renderer, display, block):
        self.renderer = renderer
        self.display = display
        self.clock = pygame.time.Clock()
        self.current_block = block

    def start(self):
        while True:

            if not self._handle_events():
                break

            self.renderer.render_all(self.display)

            pygame.display.update()
            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_down()
                    if event.key == pygame.K_LEFT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_left()
                    if event.key == pygame.K_RIGHT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.move_right()
                elif event.type == pygame.QUIT:
                    return False
        return True

    def move_block(self, block_coordinates):
        for i in range(len(block_coordinates)):
                x, y = block_coordinates[i]
                if y > -1:
                    self.renderer.game_grid.grid[y][x] = self.current_block.color
