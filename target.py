import pygame.font
from settings import Settings

class Target:
	def __init__(self, tp_game):
		""" Initialize target attributes"""
		self.settings = Settings()
		self.screen = tp_game.screen
		self.screen_rect = self.screen.get_rect()
		self.target_direction = -1

		#set the dimensions and properties of the target
		self.width, self.height = 50, 200
		self.target_color = (0, 255, 0)
		
		#Build the target's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.midright = self.screen_rect.midright

		#adust target to left by a % of right of screen
		self.x = float(self.screen_rect.right - self.width)
		self.x = self.x * self.settings.target_distance
		self.rect.x = self.x

		#store the target's exact vertical position.
		self.y = float(self.rect.y)

	def update_target(self):
		"""Check if at top or bottoom and move target"""
		self.check_top()
		self.check_bottom()
		self.update()
		self.screen.fill(self.target_color, self.rect)

	def check_top(self):
		""" Checks top to target to see if it hit top of screen"""
		if self.rect.top  <=0:
			self.target_direction = 1

	def check_bottom(self):
		if self.rect.bottom >= self.screen_rect.bottom:
			self.target_direction = -1

	def update(self):
		""" Move the target up and down"""
		self.y += (self.settings.target_speed * self.target_direction)
		self.rect.y = self.y

	def _target_update(self,cumulative_bullets):
		""" move target to right out every 10 shots"""
		print(f"_target_update {cumulative_bullets}")
		if cumulative_bullets == 0:
			self.settings.target_distance = 0.8
		elif cumulative_bullets >= 70:
			self.settings.target_distance = 0.7
		elif cumulative_bullets >= 60:
			self.settings.target_distance = 0.6
		elif cumulative_bullets >= 50:
			target_distance = 0.5
		elif cumulative_bullets >= 40:
			self.settings.target_distance = 0.4
		elif cumulative_bullets >= 30:
			self.settings.target_distance = 0.3
		elif cumulative_bullets >= 20:
			self.settings.target_distance = 0.2
		else:
			self.settings.target_distance = 0.1

		self.x = float(self.screen_rect.right - self.width)
		self.x = self.x * self.settings.target_distance
		self.rect.x = self.x

		self.check_top()
		self.check_bottom()
		self.update()
		
