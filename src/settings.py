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
        self.bullet_speed = 1.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        