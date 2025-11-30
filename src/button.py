import pygame.font
import pygame

class Button:
    def __init__(self, ai, msg):
        """Iniitiaalise the button attribute"""
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        
        # set the dimensions and properties of the button
        self.height, self.width = 50, 200
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # build the button rect and center it
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # the button needs only to be prepped once
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """ turns msg into into the rendered image and center on the button"""
        self.msg_image = self.font.render(msg,True,self.text_color, self.button_color)
        self.msg_image_rect= self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # draw blank button and then draw msg
        
        # Fills the Surface with the specified color. Optionally, fills only the given rect area
        self.screen.fill(self.button_color, self.rect)
        
        # destination_surface.blit(source_surface, dest_coordinates, area=None, special_flags=0)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        