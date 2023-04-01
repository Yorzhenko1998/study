import sys
import pygame

from settings import Settings
from bird import Bird
from bullet import Bullet

class BlueBirdGame:
	"""A class that manages game resources and behavior."""

	def __init__(self):
		"""Initialize game, create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Blue Bird Game")

		self.bird = Bird(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Start the main cycle of the game."""
		while True:
			self._check_events()
			self.bird.update()
			self._update_bullet()
			self._update_screen()

	def _check_events(self):
		# Monitor mouse and keyboard events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Response to keystrokes."""
		if event.key == pygame.K_UP:
			self.bird.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.bird.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Respond when the key is not pressed."""
		if event.key == pygame.K_UP:
			self.bird.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.bird.moving_down = False


	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullet group."""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
		print(len(self.bullets))

	def _update_bullet(self):
		"""Update the position of bullets and get rid of old bullets."""
		self.bullets.update()

		# Delete old bullets
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.screen.get_rect().right:
				self.bullets.remove(bullet)
	def _update_screen(self):
		# Redraw the screen on each loop iteration.
		self.screen.fill(self.settings.big_color)
		self.bird.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Show the last display
		pygame.display.flip()

if __name__ == '__main__':
	# Create an instance of the game and run the game.
	bbg = BlueBirdGame()
	bbg.run_game()
