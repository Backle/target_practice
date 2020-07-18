

class Settings:
	"""A class to store all settings for Side Shooter."""

	def __init__(self):
		"""Initialize the game's settings."""

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (3, 41, 120)

		#Ship Settings
		self.ship_speed = 10
		

		# Bullet settings
		self.bullet_width = 15
		self.bullet_height = 5
		self.bullet_color = (191, 122, 70)
		self.bullets_allowed = 3
		self.bullet_speed = 5	

		# target settings
		self.target_speed = 3

		self.initialize_dynamic_target_distance()

	def initialize_dynamic_target_distance(self):
		self.target_distance = 0.1
		self.cumulative_bullets = 0




