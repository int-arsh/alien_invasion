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
        self.prep_high_score()
        
    def prep_score(self):
        """Turn the score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.set.bg_color)
    
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """Turn high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.set.bg_color)
    
        # Display the score at the top  of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
        
    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.score_rect)
    
    def check_high_score(self):
        """Check if there's a high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
        
        