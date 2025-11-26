import pygame
import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

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
        
        self.stats = GameStats(self)

        # make an instance of Ship after the screen has been created
        self.ship = Ship(self)
        # parameter that gives Ship access to the game’s
        # resources, such as the screen object

        self.bullets = pygame.sprite.Group()
        # print("init ",self.bullets)

        self.aliens = pygame.sprite.Group()

        self._create_fleet()


        

    def run_game(self):
        while(True):
            # watch for any keyboard event
            # To access the events that Pygame detects
            self._check_events()
            # A helper method does work inside a class 
            # but isn’t meant to be called through an instance
            if self.stats.game_active:
            # ship’s position will be updated 
            # after we’ve checked for keyboard
            # events and before we update the screen
                self.ship.update()

                self._update_bullets()
                
                self._update_aliens()

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()


    def _check_keyup_events(self, event):    
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        """create a new bullet and add it to the group"""
        if len(self.bullets) < self.set.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # print("on func fire ",self.bullets)

    def _update_bullets(self):
        self.bullets.update()
            # print("update ",self.bullets)

        # getv rid of the bullets that have disaapeared from the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        self._check_bullet_alien_collisions()
        
    
    def _check_bullet_alien_collisions(self):
        # check for any bullet hit the alien
        # if so get rid of both
        collisinons = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        
    
    def _update_aliens(self):
        """update the positions of all aliens in the fleet. """
        self._check_fleet_edges()
        self.aliens.update()  # calls update on group of alien
        
        # look for alien-ship collisions
        if pygame.sprite. spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # chack for any alien hitting the bottom of the screen
        self._check_aliens_bottom()
            
    def _ship_hit(self):
        """REspond to ship being hit"""
        
        if self.stats.ships_left > 0:
        
            # decrement ships left
            self.stats.ships_left -= 1
            
            # get rid of remianing aleins and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # create fleet center ship
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause
            sleep(0.5)
        
        else:
            self.stats.game_active = False
    
    def _check_aliens_bottom(self):
        """check if any alien reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat as ship hit
                self._ship_hit()
                break
        

    def _create_fleet(self):
        alien = Alien(self) # will not be added to screen as not part of group
        # alien.add(self.aliens)
        alien_width, alien_height = alien.rect.size
        avail_space_x = self.set.width - (2*alien_width)
        num_aliens_x = avail_space_x // (2*alien_width)
        
        # determine the no. of rows of aliens that fit the screen
        ship_height = self.ship.rect.height
        avail_space_y = (self.set.height - ship_height 
                         - (3*alien_height))
        num_rows = avail_space_y // (2*alien_height)
        '''
        # first row of the alien
        for alien_number in range(num_aliens_x):
            # create an alien and place it on the row
            self._create_alien(alien_number)
        '''
        # create a full fleet of aliens
        for row_num in range(num_rows):
            for alien_number in range(num_aliens_x):
                # create an alien and place it on the row
                self._create_alien(alien_number, row_num)
            
            
    def _create_alien(self, alien_number, row_num):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_num
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)
        
    def _check_fleet_edges(self):
        """respond approppp if any alien reached the end of the ship"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """drop the entire fleet and change the entire fleet direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.set.fleet_drop_speed
        self.set.fleet_direction *= -1
        
        


    # helper method screen update
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # redraw the screen during each pass through the loop
        self.screen.fill(self.set.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # flip the display to put ur work on screen
        pygame.display.flip()



if __name__ == "__main__":
    # make the game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
