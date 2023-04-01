import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class for controlling ship-launched bullets."""

	def __init__(self, bbg_game):
		"""Create a object 'Bullet' at the ship's current position."""
		super().__init__()
		self.screen = bbg_game.screen
		self.settings = bbg_game.settings
		self.color = self.settings.bullet_color

		# Create a bullet rect at (0, 0) and set the correct position.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
								self.settings.bullet_height)
		self.rect.midright = bbg_game.bird.rect.midright

		# Store the position of the bullet in a decimal value.
		self.x = float(self.rect.x)

	def update(self):
		"""Move the ball up the screen"""
		# Update the decimal position of the bullet.
		self.x += self.settings.bullet_speed
		# Update rect position
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw a bullet at the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
