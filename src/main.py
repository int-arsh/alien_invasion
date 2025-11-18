import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        self.set = Settings()

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.set.width = self.screen.get_rect().width
        self.set.height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # set the bg color
        self.bg_color = self.set.bg_color

        # make an instance of Ship after the screen has been created
        self.ship = Ship(self)
        # parameter that gives Ship access to the game’s
        # resources, such as the screen object


        

    def run_game(self):
        while(True):
            # watch for any keyboard event
            # To access the events that Pygame detects
            self._check_events()
            # A helper method does work inside a class 
            # but isn’t meant to be called through an instance

            # ship’s position will be updated 
            # after we’ve checked for keyboard
            # events and before we update the screen
            self.ship.update()

            self._update_screen()

            

    # helper method for checking events
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):    
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # helper method screen update
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # redraw the screen during each pass through the loop
        self.screen.fill(self.set.bg_color)
        self.ship.blitme()
        # flip the display to put ur work on screen
        pygame.display.flip()



if __name__ == "__main__":
    # make the game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
