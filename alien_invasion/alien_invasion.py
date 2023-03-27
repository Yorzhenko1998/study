import sys
import pygame

from settings import Settings
class AlienInvasion:
	"""A class that manages game resources and behavior."""
	def __init__(self):
		"""Initialize game, create game resources."""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# Color of screen
		self.big_color = (230, 230, 230)

	def run_game(self):
		"""Start the main cycle of the game."""
		while True:
			# Monitor mouse and keyboard events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				# Redraw the screen on each loop iteration.
				self.screen.fill(self.settings.big_color)

			# Show the last display
			pygame.display.flip()

if __name__ == '__main__':
	# Create an instance of the game and run the game.
	ai = AlienInvasion()
	ai.run_game()
