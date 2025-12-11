class GameStats:
    """Track statistics for Alien Invasion"""
    def __init__(self, ai):
        self.set = ai.set
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
    
    def reset_stats(self):
        """Initialise stats that can change during the game"""
        self.ships_left = self.set.ship_limit
        self.score = 0
        self.level = 1
    
    # def read_score(self):
    #     with open('high_score.txt') as f:
    #         score = f.read()
    #         score = score.rstrip()
    
    # def write_score(self):
    #     with open('high_score.txt', 'w') as f:
    #         f.write