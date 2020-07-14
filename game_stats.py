class GameStats:
	"""Track the statistics for Side Shooter"""

	def __init__ (self, tp_game):
		""" Intitialize Statistics"""
		self.settings = tp_game.settings
		self.reset_stats()

		#start game in an inactive state
		self.game_active = False


	def reset_stats(self):
		""" Initialize statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit