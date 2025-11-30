class Settings:
    """A class to store all settings for Alien Inversion"""
    def __init__(self):
        """Initialise the game static settings"""
        # Screen settings
        self.bg_color = (230, 230, 230)
        self.width = 1200
        self.height = 800

        # bullets settings
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 4
        
        # alien settings
        self.fleet_drop_speed = 5
        
        
        # stats
        self.ship_limit = 3
        
        # how quickly the game speeds up
        self.speedup_scale = 1.1
        
        self.initialise_dynamic_settings()
    
    def initialise_dynamic_settings(self):
        """Initialise the settings that change throughout the game"""
        self.speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        # 1 right, -1 left
        self.fleet_direction = 1
        
    def increase_speed(self):
        """increase speed settings"""
        self.speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        
        
        
        
        