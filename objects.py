import pygame
import random
from random import randrange

SCREEN = WIDTH, HEIGHT = 510, 510

player_1 = pygame.image.load('Assets/astronauts/astronaut_girl.png')
player_2 = pygame.image.load('Assets/spaceships/red_spaceship.png')
player_3 = pygame.image.load('Assets/spaceships/pink_spaceship.png')
player_4 = pygame.image.load('Assets/astronauts/astronaut_boy.png')

earth_ball = pygame.image.load('Assets/earth.png')
earth_sprite = pygame.image.load('Assets/earth_sprite.png')
earth_sprite = pygame.transform.scale(earth_sprite, (WIDTH, 100))
earth_sprite_2 = pygame.image.load('Assets/earth_sprite_2.png')
earth_sprite_3 = pygame.image.load('Assets/earth_sprite_3.png')

pygame.mixer.init()

# BACKGROUND CLASS -------------------------------------------------------------------------------

class Background():
	def __init__(self, screen):
		self.screen = screen

		self.image = pygame.image.load('Assets/bg.jpeg')
		self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
		self.rect = self.image.get_rect()

		self.reset()

	def update(self):
		self.screen.blit(self.image, (self.x, self.y1))
		self.screen.blit(self.image, (self.x, self.y2))

	def reset(self):
		self.x = 0
		self.y1 = 0
		self.y2 = -HEIGHT

# PLAYER 1 CLASS ---------------------------------------------------------------------------------------

class Player1:
	def __init__(self, x,  y):
		self.x, self.y = x, y
		self.reset(self.x, self.y, player_1)

	def reset(self, x, y, player_1):
		self.index = 0
		self.image = player_1
		self.image = pygame.transform.scale(self.image, (110, 150))
		self.rect = self.image.get_rect(center=(x, y))

		self.counter = 0
		self.speed = 5
		self.health = 100
		self.fuel = 100
		self.powerup = 0
		self.alive = True
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def update(self, moving_left, moving_right, explosion_group):
		if self.alive:
			if moving_left and self.rect.x > 2:
				self.rect.x -= self.speed

			if moving_right and self.rect.x < WIDTH - self.width:
				self.rect.x += self.speed

			if self.rect.bottom >= HEIGHT:
				self.rect.bottom = HEIGHT

			if self.rect.top <= 0:
				self.rect.top = 0

			if self.health <= 0:
				x, y = self.rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)

				self.alive = False

	def draw(self, screen):
		if self.alive:
			screen.blit(self.image, self.rect)

# PLAYER 2 CLASS -----------------------------------------------------------------------------------

class Player2:
	def __init__(self, x,  y):
		self.x, self.y = x, y
		self.reset(self.x, self.y, player_2)

	def reset(self, x, y, player_2):
		self.index = 0
		self.image = player_2
		self.image = pygame.transform.scale(self.image, (75, 75))
		self.rect = self.image.get_rect(center=(x, y))

		self.counter = 0
		self.speed = 5
		self.health = 100
		self.fuel = 100
		self.powerup = 0
		self.alive = True
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def update(self, moving_left, moving_right, explosion_group):
		if self.alive:
			if moving_left and self.rect.x > 2:
				self.rect.x -= self.speed

			if moving_right and self.rect.x < WIDTH - self.width:
				self.rect.x += self.speed

			if self.rect.bottom >= HEIGHT:
				self.rect.bottom = HEIGHT

			if self.rect.top <= 0:
				self.rect.top = 0

			if self.health <= 0:
				x, y = self.rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)

				self.alive = False

	def draw(self, screen):
		if self.alive:
			screen.blit(self.image, self.rect)

# PLAYER 3 CLASS ----------------------------------------------------------------------------------

class Player3:
	def __init__(self, x,  y):
		self.x, self.y = x, y
		self.reset(self.x, self.y, player_3)

	def reset(self, x, y, player_3):
		self.index = 0
		self.image = player_3
		self.image = pygame.transform.scale(self.image, (105, 105))
		self.rect = self.image.get_rect(center=(x, y))

		self.counter = 0
		self.speed = 5
		self.health = 100
		self.fuel = 100
		self.powerup = 0
		self.alive = True
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def update(self, moving_left, moving_right, explosion_group):
		if self.alive:
			if moving_left and self.rect.x > 2:
				self.rect.x -= self.speed

			if moving_right and self.rect.x < WIDTH - self.width:
				self.rect.x += self.speed

			if self.rect.bottom >= HEIGHT:
				self.rect.bottom = HEIGHT

			if self.rect.top <= 0:
				self.rect.top = 0

			if self.health <= 0:
				x, y = self.rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)

				self.alive = False

	def draw(self, screen):
		if self.alive:
			screen.blit(self.image, self.rect)

# PLAYER 4 CLASS
class Player4:
	def __init__(self, x,  y):
		self.x, self.y = x, y
		self.reset(self.x, self.y, player_4)

	def reset(self, x, y, player_4):
		self.index = 0
		self.image = player_4
		self.image = pygame.transform.scale(self.image, (110, 150))
		self.rect = self.image.get_rect(center=(x, y))

		self.counter = 0
		self.speed = 5
		self.health = 100
		self.fuel = 100
		self.powerup = 0
		self.alive = True
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def update(self, moving_left, moving_right, explosion_group):
		if self.alive:
			if moving_left and self.rect.x > 2:
				self.rect.x -= self.speed

			if moving_right and self.rect.x < WIDTH - self.width:
				self.rect.x += self.speed

			if self.rect.bottom >= HEIGHT:
				self.rect.bottom = HEIGHT

			if self.rect.top <= 0:
				self.rect.top = 0

			if self.health <= 0:
				x, y = self.rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)

				self.alive = False

	def draw(self, screen):
		if self.alive:
			screen.blit(self.image, self.rect)

# ENEMY CLASS --------------------------------------------------------------------------------------

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, type_, earth_health_enemy):
		super(Enemy, self).__init__()

		self.type = type_
		self.image_list = []
		for i in range(2):
			if type_ == 1:
				img = pygame.image.load('Assets/Enemies/enemy1-1.png')
			if type_ == 2:
				img = pygame.image.load('Assets/Enemies/enemy1-2.png')
			if type_ == 3:
				img = pygame.image.load('Assets/Enemies/enemy2-1.png')
			if type_ == 4:
				img = pygame.image.load('Assets/Enemies/enemy2-2.png')
			if type_ == 5:
				img = pygame.image.load('Assets/Enemies/enemy3-1.png')
			if type_ == 6:
				img = pygame.image.load(f'Assets/Enemies/enemy_meteor-{i+1}.png')
			if type_ == 7:
				img = pygame.image.load(f'Assets/Enemies/enemy_skull-{i+1}.png')

			w, h = img.get_width(), img.get_height()
			height = 75
			image = pygame.transform.scale(img, (75, 75))

			self.image_list.append(image)

		self.index = 0
		self.image = self.image_list[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.frame_dict = {1:3, 2:3, 3:3, 4:5, 5:4, 6:4, 7:10}
		self.frame_fps = self.frame_dict[type_]

		self.counter = 0
		self.speed = 1
		self.health = 50
		self.bullet_counter = 0
		self.earth_health_enemy = earth_health_enemy

	def shoot(self, enemy_bullet_group):
		if self.type in (4, 7):
			x, y = self.rect.center
			b = Bullet(x, y, self.type)
			enemy_bullet_group.add(b)
		if self.type == 3:
			x, y = self.rect.center
			b = Bullet(x - 25, y + 10, self.type)
			enemy_bullet_group.add(b)
			b = Bullet(x + 25, y + 10, self.type)
			enemy_bullet_group.add(b)

	def update(self, enemy_bullet_group, explosion_group, game_page, score_page, earth_health):
		self.rect.y += self.speed
		self.earth_health = earth_health
		if self.rect.top >= 365:
			self.earth_health -= 10
			self.kill()

		if self.health <= 0:
			x, y = self.rect.center
			explosion = Explosion(x, y, 2)
			explosion_group.add(explosion)

			self.kill()

		self.bullet_counter += 1
		if self.bullet_counter >= 60:
			self.shoot(enemy_bullet_group)
			self.bullet_counter = 0

		self.counter += 1
		if self.counter >= self.frame_fps:
			self.index = (self.index + 1) % len(self.image_list)
			self.image = self.image_list[self.index]
			self.counter = 0

	def draw(self, screen):
		WHITE = (255, 255, 255)
		BLUE = (30, 144, 255)
		RED = (255, 0, 0)
		GREEN = (0, 255, 0)
		BLACK = (0, 0, 20)
		screen.blit(self.image, self.rect)

# BULLET CLASS ----------------------------------------------------------------------------------

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, type_, dx=None):
		super(Bullet, self).__init__()

		self.dx = dx
		powerup_bullet = False
		if self.dx in range(-3, 4):
			powerup_bullet = True

		if type_ == 1:
			self.image = pygame.image.load('Assets/Bullets/1.png')
			self.image = pygame.transform.scale(self.image, (20, 40))
		if type_ == 2:
			self.image = pygame.image.load('Assets/Bullets/2.png')
			self.image = pygame.transform.scale(self.image, (15, 30))
		if type_ == 3:
			self.image = pygame.image.load('Assets/Bullets/3.png')
			self.image = pygame.transform.scale(self.image, (20, 40))
		if type_ in (4, 5):
			self.image = pygame.image.load('Assets/Bullets/4.png')
			self.image = pygame.transform.scale(self.image, (20, 20))
		if type_ == 6:
			self.image = pygame.image.load('Assets/Bullets/6.png')
			self.image = pygame.transform.scale(self.image, (15, 30))
		if type_ == 7:
			self.image = pygame.image.load('Assets/Bullets/fire_ball.png')
			self.image = pygame.transform.scale(self.image, (35, 40))

		self.rect = self.image.get_rect(center=(x, y))
		if type_ == 6 or powerup_bullet:
			self.speed = -5
		else:
			self.speed = 2

		if self.dx == None:
			self.dx = 0

		self.damage_dict = {1:5, 2:10, 3:15, 4:25, 5:25, 6:20, 7:15}
		self.damage = self.damage_dict[type_]
		if powerup_bullet:
			self.damage = 50


	def update(self):
		self.rect.x += self.dx
		self.rect.y += self.speed
		if self.rect.bottom <= 0:
			self.kill()
		if self.rect.top >= HEIGHT:
			self.kill()

	def draw(self, screen):
		screen.blit(self.image, self.rect)

# EXPLOSION CLASS -------------------------------------------------------------------------

class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y, type_):
		super(Explosion, self).__init__()


		self.img_list = []
		if type_ == 1:
			self.length = 3
		elif type_ == 2:
			self.length = 8

		for i in range(self.length):
			img = pygame.image.load(f'Assets/Explosion{type_}/{i+1}.png')
			w, h = img.get_size()
			width = int(w * 0.40)
			height = int(w * 0.40)
			img = pygame.transform.scale(img, (width, height))
			self.img_list.append(img)

		self.index = 0
		self.image = self.img_list[self.index]
		self.rect = self.image.get_rect(center=(x, y))

		self.counter = 0

	def update(self):
		self.counter += 1
		if self.counter >= 7:
			self.index += 1
			if self.index >= self.length:
				self.kill()
			else:
				self.image = self.img_list[self.index]
				self.counter = 0

		
	def draw(screen, self=None):
		screen.blit(self.image, self.rect)

# FUEL CLASS -------------------------------------------------------------------------------

class Fuel(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(Fuel, self).__init__()

		self.image = pygame.image.load('Assets/fuel.png')
		self.image = pygame.transform.scale(self.image, (30, 29))
		self.rect = self.image.get_rect(center=(x, y))

	def update(self):
		self.rect.y += 1
		if self.rect.top >= HEIGHT:
			self.kill()

	def draw(self, screen):
		screen.blit(self.image, self.rect)

# POWERUP CLASS ----------------------------------------------------------------------------

class Powerup(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(Powerup, self).__init__()

		self.image = pygame.image.load('Assets/powerup.png')
		self.image = pygame.transform.scale(self.image, (30, 29))
		self.rect = self.image.get_rect(center=(x, y))

	def update(self):
		self.rect.y += 1
		if self.rect.top >= HEIGHT:
			self.kill()

	def draw(self, screen):
		screen.blit(self.image, self.rect)

# BUTTON CLASS---------------------------------------------------------------------------

class Button(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Button, self).__init__()
		
		self.scale = scale
		self.image = pygame.transform.scale(img, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = pygame.transform.scale(img, self.scale)

	def draw(self, screen):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		screen.blit(self.image, self.rect)
		return action

# MESSAGE CLASS --------------------------------------------------------------------------

class Message:
	def __init__(self, x, y, size, text, font, color, screen):
		self.screen = screen
		self.color = color
		self.x, self.y = x, y
		if not font:
			self.font = pygame.font.SysFont("Verdana", size)
			anti_alias = True
		else:
			self.font = pygame.font.Font(font, size)
			anti_alias = False
		self.image = self.font.render(text, anti_alias, color)
		self.rect = self.image.get_rect(center=(x,y))
		self.shadow = self.font.render(text, anti_alias, (54,69,79))
		self.shadow_rect = self.image.get_rect(center=(x+2,y+2))
		
	def update(self, text=None, shadow=True):
		if text:
			self.image = self.font.render(f"{text}", False, self.color)
			self.rect = self.image.get_rect(center=(self.x, self.y))
			self.shadow = self.font.render(f"{text}", False, (54, 69, 79))
			self.shadow_rect = self.image.get_rect(center=(self.x+2, self.y+2))
		if shadow:
			self.screen.blit(self.shadow, self.shadow_rect)
		self.screen.blit(self.image, self.rect)

# BLINKING TEXT CLASS ---------------------------------------------------------------------------------

class BlinkingText(Message):
	def __init__(self, x, y, size, text, font, color, screen):
		super(BlinkingText, self).__init__(x, y, size, text, font, color, screen)
		self.index = 0
		self.show = True

	def update(self):
		self.index += 1
		if self.index % 40 == 0:
			self.show = not self.show

		if self.show:
			self.screen.blit(self.image, self.rect)

# EARTH CLASS -------------------------------------------------------------------------------------

class Earth:
	def __init__(self, x, y, earth_sprite, earth_health):
		self.image = earth_sprite
		self.image = pygame.transform.scale(self.image, (WIDTH, 100))
		self.health = earth_health
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, screen, enemy_group):
		screen.blit(self.image, self.rect )

	def draw(self, screen):
		screen.blit(self.image, self.rect)

