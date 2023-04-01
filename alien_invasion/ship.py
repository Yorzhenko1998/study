import pygame

class Ship:
	"""Class for steer the ship."""
	def __init__(self, ai_game):
		"""Initialize the ship and his position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Download the image of ship
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship at the bottom of the screen, in the center.
		self.rect.midbottom = self.screen_rect.midbottom

		# Save the decimal value of the ship horizontally.
		self.x = float(self.rect.x)

		# Traffic indicator.
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""
		Update the current position of the ship on the oson of the
		traffic indicators.
		"""
		# Update value ship_x, not a rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update object rect whit self.x
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship in its original position."""
		self.screen.blit(self.image, self.rect)
