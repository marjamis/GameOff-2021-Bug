import pygame

from settings.screen import Settings
from sprites.plant import Plant


class Screen:
    def __init__(self):
        self.settings = Settings()
        self.screen_surface = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        self.plant = Plant(self)

    def update(self):
        self.screen_surface.fill(self.settings.bg_colour)
        self.plant.draw()
