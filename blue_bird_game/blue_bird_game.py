import sys
import pygame

from settings import Settings
from bird import Bird

class BlueBirdGame:
	"""A class that manages game resources and behavior."""
	def __init__(self):
		"""Initialize game, create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Blue Bird Game")

		self.bird = Bird(self)

	def run_game(self):
		"""Start the main cycle of the game."""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				self.screen.fill(self.settings.big_color)
				self.bird.blitme()
			# Show the last display
			pygame.display.flip()

if __name__ == '__main__':
	# Create an instance of the game and run the game.
	bbg = BlueBirdGame()
	bbg.run_game()
