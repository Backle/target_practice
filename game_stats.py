class GameStats:
	"""Track the statistics for Side Shooter"""

	def __init__ (self, tp_game):
		""" Intitialize Statistics"""
		self.settings = tp_game.settings

		#start game in an inactive state
		self.game_active = False

