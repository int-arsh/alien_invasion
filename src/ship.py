import pygame
from settings import Settings


class Ship:
    def __init__(self, ai):
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.set = ai.set

        self.image = pygame.image.load('src/public/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    
    def update(self):
        if self.moving_right and self.rect.x<self.screen_rect.right-self.rect.width:
            self.x += self.set.speed
        if self.moving_left and self.rect.x>0:
            self.x -= self.set.speed
        
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #     destination_surface.blit(source_surface, dest_coordinates, area=None, special_flags=0)