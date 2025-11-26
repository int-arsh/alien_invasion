class Settings:
    """A class to store all settings for Alien Inversion"""
    def __init__(self):
        """Initialise the game settings"""
        # Screen settings
        self.bg_color = (230, 230, 230)
        self.width = 1200
        self.height = 800
        self.speed = 1.5

        # bullets settings
        self.bullet_speed = 2.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 4
        
        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # 1 right, -1 left
        self.fleet_direction = 1
        
        # stats
        self.ship_limit = 3
        
        