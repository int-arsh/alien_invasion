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
        
        self.set = ai.set
        
    def update(self):
        """move the alien to the right"""
        self.x+= self.set.alien_speed * self.set.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        """Return true if any alien is ta the end of gthe creen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
    
    
    
 