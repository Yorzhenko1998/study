class Settings:
	"""Class for saving all settings in the game"""

	def __init__(self):
		"""Initialize game settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.big_color = (230, 230, 230)

		# Ship setting
		self.ship_speed = 1.5

		# Initialize game settings.
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
