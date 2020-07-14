import sys
from random import randint
import pygame
from settings import Settings
from target import Target
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from time import sleep
from button import Button
		
class TargetPractice:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Target Practice")

		#create an instance to store game statistics
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

		self.target = Target(self)

		#create a variable to count misses
		self.miss_count = 0
		self.max_misses = 10

		#make the the Play button
		self.play_button = Button(self, 'Press "P" to Play')


	def run_game(self):
		"""Start the main loop for the game."""
		#show press p to play

		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self.target._target_update(cumulative_bullets)

			self._update_screen()

	def _check_events(self):
		# respond to keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses. """
		if event.key == pygame.K_UP:
			# Move the ship up.
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			# Move the ship down.
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			#Press q to quit
			sys.exit()	
		elif event.key == pygame.K_SPACE:
			#fire bullets on spacebar
			self._fire_bullet()
		elif event.key == pygame.K_p:
			#Press p to start
			if not self.stats.game_active:
				self._start_game()

	def _check_keyup_events(self,event):
		""" respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _start_game(self):
		#Make game active and reset the game stats
		self._update_stats()
		self.stats.game_active = True

		#get rid of any remaining any buns and bullets
		self.bullets.empty()
			#create a new batch and center the ship
		self.ship.center_ship()

	def _fire_bullet(self):
		""" Create a new bullet and add it to the bullets group"""
		if len(self.bullets)< self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
		#add a total bullet counter
			self.settings.cumulative_bullets += 1
			print(self.settings.cumulative_bullets)

	def _update_bullets(self):
		""" updated bullet position and gets rid of old bullets"""
		#update bullet positons.
		self.bullets.update()
		# check to see if any bullet hit the target, if so, get rid of it
		for bullet in self.bullets.copy():
			collisions = bullet.rect.colliderect(self.target)
			if collisions:
				self.bullets.remove(bullet)
		#if bullet misses (reaches right edge), get rid of it and count miss
			elif bullet.rect.left >= self.settings.screen_width:
				self.bullets.remove(bullet)
				self.miss_count +=1
				self._check_max_miss()

	def _check_max_miss(self):
		""" check to see if miss_count has reached max - then flag active off"""
		if self.miss_count >= self.max_misses:
			self.stats.game_active = False

	def _update_stats(self):
		"""reset miss count to 0"""
		self.miss_count = 0
		self.settings.initialize_dynamic_target_distance()

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.target.screen.fill(self.target.target_color, self.target.rect)

		#Draw the play button if the game is inactive.
		if not self.stats.game_active:
			self.play_button.draw_button()
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.q
	cumulative_bullets = 0
	tp = TargetPractice()
	tp.run_game()
