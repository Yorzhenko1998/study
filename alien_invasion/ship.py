import pygame

class Ship:
	"""Class for steer the ship."""
	def __init__(self, ai_game):
		"""Initialize the ship and his position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Download the image of ship
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship at the bottom of the screen, in the center.
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Draw the ship in its original position."""
		self.screen.blit(self.image, self.rect)
