import pygame

class GameLoop:
    def __init__(self, renderer, display, block):
        self.renderer = renderer
        self.display = display
        self.clock = pygame.time.Clock()
        self.current_block = block
        self.previous_block_coordinates = [(0,0), (0,0), (0,0), (0,0)]

    def start(self):
        while True:

            if not self._handle_events():
                break

            self.renderer.render_all(self.display)

            block_coordinates = self.current_block.shape_to_coordinates()
            self.move_block(block_coordinates)

            pygame.display.update()
            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                            self.current_block.rotate()
                    if event.key == pygame.K_DOWN:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                            self.current_block.move_down()
                    if event.key == pygame.K_LEFT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                            self.current_block.move_left()
                    if event.key == pygame.K_RIGHT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.previous_block_coordinates = self.current_block.shape_to_coordinates()
                            self.current_block.move_right()
                elif event.type == pygame.QUIT:
                    return False
        return True

    def move_block(self, current_block_coordinates):
        for i in range(len(current_block_coordinates)):
            x, y = current_block_coordinates[i]
            self.renderer.game_grid.grid[y][x] = self.current_block.color
            self.renderer.game_grid.reset_cell_colors(self.previous_block_coordinates, current_block_coordinates)
