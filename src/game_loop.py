import pygame

class GameLoop:
    def __init__(self, renderer, display):
        self.renderer = renderer
        self.display = display

    def start(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.renderer.render_background()
            self.renderer.render_board(self.display)

            pygame.display.update()
            clock.tick(60)
