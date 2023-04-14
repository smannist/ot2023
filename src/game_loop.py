import pygame

class GameLoop:
    def __init__(self, renderer, display, block):
        self.renderer = renderer
        self.display = display
        self.current_block = block

    def start(self):
        clock = pygame.time.Clock()

        while True:

            if self._handle_events() == False:
                break

            self.renderer.render_all(self.display)

            self.renderer.game_grid.grid[0][1] = (0,255,0) # testing, remove later

            pygame.display.update()
            clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.y += 1
                    if event.key == pygame.K_LEFT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.x -= 1
                    if event.key == pygame.K_RIGHT:
                        if self.renderer.game_grid.is_valid_move(self.current_block):
                            self.current_block.x += 1
                elif event.type == pygame.QUIT:
                    return False
