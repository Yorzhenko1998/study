import pygame

class Bird:
	"""A class to manage the bird."""

	def __init__(self, bbg_game):
		"""Initialize the bird and his position"""
		self.screen = bbg_game.screen
		self.settings = bbg_game.settings
		self.screen_rect = bbg_game.screen.get_rect()

		# Download the image of bird
		self.image = pygame.image.load('images/bird_small.bmp')
		self.rect = self.image.get_rect()

		# Create each new bird at the bottom of the screen, in the center.
		self.rect.centery = self.screen_rect.centery

		# Save the decimal value of the bird horizontally.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Traffic indicator.
		self.moving_up = False
		self.moving_down = False
	def update(self):
		"""
		Update the current position of the bird on the oson of the
		traffic indicators.
		"""
		# Update value bird_x, not a rect
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.settings.bird_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.bird_speed

		# Update object rect whit self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the bird in its original position."""
		self.screen.blit(self.image, self.rect)