import pygame
from pygame.sprite import Sprite


class Plant(Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen_surface = screen.screen_surface
        self.screen_rect = self.screen_surface.get_rect()

        self.image = pygame.image.load('./media/images/active/plant.png')
        self.image_height = self.image.get_size()[0]
        self.image_width = self.image.get_size()[1]
        self.image_scale = 1
        self.image_scale_by = 1

        # Better method for this as this does allow for the possibility for both to be true at once. Very unlikely, so am I over thinking this?
        self.growing = False
        self.shrinking = False

    def draw(self):
        """Draw the plant at its current location."""
        if self.growing:
            self.grow()
        elif self.shrinking:
            self.shrink()

        self.image = pygame.transform.scale(
            self.image, (self.image_height * self.image_scale, self.image_width * self.image_scale))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.screen_surface.blit(self.image, self.rect)

    def grow(self):
        self.image_scale += self.image_scale_by
        if self.image_scale > 5:
            self.image_scale = 5

    def shrink(self):
        self.image_scale -= self.image_scale_by
        if self.image_scale <= 0:
            self.image_scale = 1
