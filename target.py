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

	def move_target(self, distance_adjustment):
		""" moves the target further out as a % of the screen """
		self.x = float(self.screen_rect.right - self.width)
		self.x = self.x * distance_adjustment
		self.rect.x = self.x

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


