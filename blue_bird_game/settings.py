class Settings:
	"""Class for saving all settings in the game"""
	def __init__(self):
		"""Initialize game settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.big_color = (0, 0, 0)

		# Ship setting
		self.bird_speed = 1.5

		self.bullet_speed = 1.0
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (69, 139, 0)
		self.bullet_allowed = 3