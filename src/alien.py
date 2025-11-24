import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai):
        super().__init__()

        self.screen = ai.screen
        self.set = ai.set

        self.image = pygame.image.load('src/public/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
