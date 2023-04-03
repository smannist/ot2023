import pygame

class GameLoop:
    def __init__(self, renderer):
        self.renderer = renderer

    def start(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            self.renderer.render_background()
