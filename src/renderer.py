import pygame

colors = {"grey": (80,80,80)}

class Renderer:
    def __init__(self, display):
        self.display = display

    def render_background(self):
        self.display.fill((colors["grey"]))
        pygame.display.update()
