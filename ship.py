import pygame

class Ship:
    """A class to mage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.scree_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        path = 'C:/Users/Alejo/Documents/python_work/Project1/alien_invasion/images/Turtle.png'
        # path = 'C:/Users/Alejo/Documents/python_work/Project1/alien_invasion/images/ship.bmp'
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.scree_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)