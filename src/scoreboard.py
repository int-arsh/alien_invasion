import pygame.font

class Scoreboard:
    """A class to report scoring information"""
    def __init__(self, ai):
        """Initialise score keeping attributes"""
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.set = ai.set
        self.stats = ai.stats
        
        # font settings to for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # prepare initial score image
        self.prep_score()
        
    def prep_score(self):
        """Turn the score into rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.set.bg_color)
    
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        