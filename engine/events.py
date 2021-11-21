import sys
import pygame

from engine.internal import ExitGame


class Events():
    def __init__(self, plant):
        self.plant = plant

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ExitGame()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.plant.growing = True
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.plant.shrinking = True
        elif event.key == pygame.K_q:
            ExitGame()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.plant.growing = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.plant.shrinking = False
