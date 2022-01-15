# space war

# importing libraries
import random
import sys
import pygame
import pygame.image
from objects import Background, Player1, Player2, Player3, Enemy, Bullet, Explosion, Fuel, \
	Powerup, Button, Message, Earth, player_2, Player4, player_1, player_3, player_4, BlinkingText
from os import environ
from sys import platform as _sys_platform

# initializing pygame
pygame.init()

# screen and width
SCREEN = WIDTH, HEIGHT = 512, 512

# display ifo
info = pygame.display.Info()
width = info.current_w
height = info.current_h
mouse_x, mouse_y = pygame.mouse.get_pos()

if width >= height:
	screen = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	screen = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60

# SETTING GAME NAME AND ICON ************************************************

icon = pygame.image.load('Assets/icon.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('SPACE WARS')

# BUILDOZER *******************************************************************

def platform():
	if 'ANDROID_ARGUMENT' in environ:
		return 'android'
	elif _sys_platform in ('linux', 'linux2', 'linux3'):
		return 'linux'
	elif _sys_platform in ('win32', 'cygwin'):
		return 'win'

if platform() == 'android':
	path = '/data/data/org.test.pygame/files/app/'
elif platform() == 'linux':
	path = './'

# image = pygame.image.load(path='image.png')


# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

# VARIABLES *******************************************************************

# user_text = ''
# input_rect = pygame.Rect(10, 200, 480, 50)
# color_active = pygame.Color('lightskyblue3')
# color_passive = pygame.Color('gray15')
# color = color_passive

active = False

# IMAGES **********************************************************************

plane_img = pygame.image.load('Assets/plane.png')
plane_img = pygame.transform.scale(plane_img, (30,30))
logo_img = pygame.image.load('Assets/logo.png')
logo_img = pygame.transform.scale(logo_img, (400, 200))
logo_img_2 = pygame.image.load('Assets/logo.png')
logo_img_2 = pygame.transform.scale(logo_img_2, (400, 160))
fighter_img = pygame.image.load('Assets/fighter.png')
fighter_img = pygame.transform.scale(fighter_img, (80, 80))
earth_img = pygame.image.load('Assets/earth.png')
earth_img = pygame.transform.scale(earth_img, (33, 33))
home_bg = pygame.image.load('Assets/home_bg.jpeg')
home_bg = pygame.transform.scale(home_bg, (WIDTH, HEIGHT))
earth_sprite = pygame.image.load('Assets/earth_sprite.png')

home_img = pygame.image.load('Assets/Buttons/homeBtn.png')
replay_img = pygame.image.load('Assets/Buttons/replay.png')
sound_off_img = pygame.image.load("Assets/Buttons/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/Buttons/soundOnBtn.png")
start_img = pygame.image.load('Assets/Buttons/start.png')
help_img = pygame.image.load('Assets/Buttons/help.png')
quit_img = pygame.image.load('Assets/Buttons/quit.png')

up_arrow_btn_img = pygame.image.load('Assets/Buttons/up_arrow.png')
down_arrow_btn_img = pygame.image.load('Assets/Buttons/down-arrow.png')

yes_img = pygame.image.load('Assets/Buttons/yes.png')
no_img = pygame.image.load('Assets/Buttons/no.png')

earth_sprite_2 = pygame.image.load('Assets/earth_sprite_2.png')
earth_sprite_3 = pygame.image.load('Assets/earth_sprite_3.png')
earth_sprite_2 = pygame.transform.scale(earth_sprite_2, (80, WIDTH))
earth_sprite_3 = pygame.transform.scale(earth_sprite_3, (80, WIDTH))

go_img = pygame.image.load('Assets/Buttons/right-arrow.png')

player_1_img = pygame.image.load('Assets/Buttons/btn_ship_red.jpg')
player_2_img = pygame.image.load('Assets/Buttons/btn_ship_pink.jpg')
player_3_img = pygame.image.load('Assets/Buttons/btn_ast_boy.jpg')
player_4_img = pygame.image.load('Assets/Buttons/btn_ast_girl.jpg')


# BUTTONS *********************************************************************

home_btn = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 120)
replay_btn = Button(replay_img, (36, 36), WIDTH // 2 - 18, HEIGHT//2 + 115)
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 + 120)
plane_img_button = Button(plane_img, (30, 30), 10, 15)
home_btn_2 = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 120)
replay_btn_2 = Button(replay_img, (36, 36), WIDTH // 2 - 18, HEIGHT//2 + 115)
sound_btn_2 = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 + 120)
start_button = Button(start_img, (100, 100), WIDTH//2-200, HEIGHT-100)
help_button = Button(help_img, (100, 100), WIDTH//2+105, HEIGHT-100)
quit_button = Button(quit_img, (100, 100), WIDTH//2-41, HEIGHT-100)
home_btn_3 = Button(home_img, (24, 24), WIDTH // 2, HEIGHT//2 + 250)
up_arrow_btn = Button(up_arrow_btn_img, (30, 30), 8, 440)
down_arrow_btn = Button(down_arrow_btn_img, (30, 30), 8, 470)
yes_btn = Button(yes_img, (120, 70), 70, HEIGHT//2)
no_btn = Button(no_img, (120, 70), 300, HEIGHT//2)
go_btn = Button(go_img, (60, 60), WIDTH//2-20, HEIGHT//2+170)

player_1_btn = Button(player_1_img, (90, 90), 70, 100)
player_2_btn = Button(player_2_img, (90, 90), 350, 100)
player_3_btn = Button(player_3_img, (90, 90), 70, 270)
player_4_btn = Button(player_4_img, (90, 90), 350, 270)

# FONTS ***********************************************************************

game_over_font = 'Fonts/ghostclan.ttf'
confirmation_font = 'Fonts/BubblegumSans-Regular.ttf'
score_font = 'Fonts/DalelandsUncialBold-82zA.ttf'
final_score_font = 'Fonts/DroneflyRegular-K78LA.ttf'
help_page_font_1 = 'Fonts/ghostclan.ttf'
help_page_font_2 = 'Fonts/DalelandsUncialBold-82zA.ttf'
arial_font = pygame.font.SysFont("Arial", 30)

game_over_msg = Message(WIDTH//2, 230, 30, 'Game Over', game_over_font, WHITE, screen)
score_msg = Message(WIDTH-50, 28, 30, '0', final_score_font, BLUE, screen)
final_score_msg = Message(WIDTH//2, 280, 30, '0', final_score_font, BLUE, screen)
game_confirmation_msg = Message(WIDTH//2, HEIGHT//2-80, 35, 'Are you sure you want to exit ?', confirmation_font, BLUE, screen)
exit_help_page = BlinkingText(220, 490, 20, 'Click anywhere on the screen to exit this screen ', confirmation_font, BLUE, screen)


# SOUNDS **********************************************************************

player_bullet_fx = pygame.mixer.Sound('Sounds/laser_shot.mp3')
click_fx = pygame.mixer.Sound('Sounds/click.mp3')
collision_fx = pygame.mixer.Sound('Sounds/mini_exp.mp3')
blast_fx = pygame.mixer.Sound('Sounds/blast.wav')
fuel_fx = pygame.mixer.Sound('Sounds/fuel.wav')

pygame.mixer.music.load('Sounds/Defrini - Spookie.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)


# GROUPS & OBJECTS ************************************************************

earth_health = 100

bg = Background(screen)
earth = Earth(HEIGHT, WIDTH, earth_sprite, earth_health)

enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()

# FUNCTIONS *******************************************************************


def shoot_bullet():
	x, y = p.rect.center[0], p.rect.y

	if p.powerup > 0:
		for dx in range(-3, 4):
			b = Bullet(x, y, 4, dx)
			player_bullet_group.add(b)
		p.powerup -= 1
	else:
		b = Bullet(x-22, y, 6)
		player_bullet_group.add(b)
		b = Bullet(x+22, y, 6)
		player_bullet_group.add(b)
	player_bullet_fx.play()


def reset():
	enemy_group.empty()
	player_bullet_group.empty()
	enemy_bullet_group.empty()
	explosion_group.empty()
	fuel_group.empty()
	powerup_group.empty()


# VARIABLES *******************************************************************


level = 1
plane_destroy_count = 0
plane_frequency = 5000
start_time = pygame.time.get_ticks()

is_paused = False

moving_left = False
moving_right = False
moving_up = False
moving_down = False

choose_player_page = False
home_page = True
game_page = False
score_page = False
option_page = False
help_page = False
exit_decision_page = False

player_speed = 14

score = 0
sound_on = True

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False

		if event.type == pygame.KEYDOWN and game_page:
			if event.key == pygame.K_LEFT:
				moving_left = True
			if event.key == pygame.K_RIGHT:
				moving_right = True
			if event.key == pygame.K_DOWN:
				p.rect.y += player_speed
			if event.key == pygame.K_UP:
				p.rect.y -= player_speed
			if event.key == pygame.K_SPACE:
				shoot_bullet()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if help_page:
				help_page = False
				home_page = True
			if game_page:
				x, y = event.pos
				if p.rect.collidepoint((x, y)):
					shoot_bullet()
				elif x <= WIDTH // 2:
					moving_left = True
				elif x > WIDTH // 2:
					moving_right = True

		if event.type == pygame.KEYUP:
			moving_left = False
			moving_right = False

		if event.type == pygame.MOUSEBUTTONUP:
			moving_left = False
			moving_right = False

	if home_page:
		screen.blit(home_bg, (0, 0))
		screen.blit(logo_img, (50, 50))
		screen.blit(fighter_img, (WIDTH//2 - 36, HEIGHT//2 + 50))

		if start_button.draw(screen):
			choose_player_page = True
			home_page = False

		if help_button.draw(screen):
			help_page = True
			home_page = True

		if quit_button.draw(screen):
			exit_decision_page = True
			home_page = False

	if score_page:
		screen.fill(BLACK)
		screen.blit(logo_img_2, (50, 65))
		game_over_msg.update()
		final_score_msg.update(score)

		if home_btn.draw(screen):
			home_page = True
			game_page = False
			score_page = False
			reset()
			click_fx.play()

			plane_destroy_count = 0
			level = 1
			score = 0

		if replay_btn.draw(screen):
			score_page = False
			game_page = True
			reset()
			click_fx.play()

			plane_destroy_count = 0
			score = 0

		if sound_btn.draw(screen):
			sound_on = not sound_on

			if sound_on:
				sound_btn.update_image(sound_on_img)
				pygame.mixer.music.play(loops=-1)
			else:
				sound_btn.update_image(sound_off_img)
				pygame.mixer.music.stop()

	if choose_player_page:
		screen.fill(BLACK)
		msg_choose = Message(240, 30, 30, "Choose your player", confirmation_font, BLUE, screen)
		msg_choose.update()

		if player_4_btn.draw(screen):
			p = Player1(WIDTH / 2, HEIGHT - 100)
			p.reset(p.x, p.y, player_1)
		if player_1_btn.draw(screen):
			p = Player2(WIDTH / 2, HEIGHT - 100)
			p.reset(p.x, p.y, player_2)
		if player_2_btn.draw(screen):
			p = Player3(WIDTH / 2, HEIGHT - 100)
			p.reset(p.x, p.y, player_3)
		if player_3_btn.draw(screen):
			p = Player4(WIDTH / 2, HEIGHT - 100)
			p.reset(p.x, p.y, player_4)

		if go_btn.draw(screen):
			choose_player_page = False
			game_page = True

			click_fx.play()

	if option_page:
		screen.blit(logo_img, (50, 50))

		if home_btn_2.draw(screen):
			home_page = True
			game_page = False
			score_page = False
			option_page = False
			reset()
			click_fx.play()

			plane_destroy_count = 0
			level = 1
			score = 0

		if replay_btn_2.draw(screen):
			home_page = False
			score_page = False
			game_page = True
			option_page = False
			reset()
			click_fx.play()

			plane_destroy_count = 0
			score = 0

		if sound_btn_2.draw(screen):
			sound_on = not sound_on

			if sound_on:
				sound_btn.update_image(sound_on_img)
				pygame.mixer.music.play(loops=-1)
			else:
				sound_btn.update_image(sound_off_img)
				pygame.mixer.music.stop()

	if help_page:
		screen.fill(BLACK)

		if home_btn_3.draw(screen):
			home_page = True
			help_page = False
			score_page = False
			game_page = False
			click_fx.play()

			plane_destroy_count = 0
			level = 1
			score = 0

		msg_1 = Message(220, 20, 30, 'HOW TO PLAY THE GAME :', help_page_font_1, BLUE, screen)
		msg_2 = Message(190, 50, 13, 'If you are playing space war in smartphone , ', help_page_font_2, WHITE, screen)
		msg_3 = Message(220, 80, 13, 'then to move the player to the right side or left side ', help_page_font_2, WHITE, screen)
		msg_4 = Message(180, 110, 13, 'tap on right side or left side to move the player the ', help_page_font_2, WHITE, screen)
		msg_5 = Message(220, 140, 13, 'player right or left . Tap on upper side to move the ', help_page_font_2, WHITE, screen)
		msg_6 = Message(240, 170, 13, 'player upwards and tap on down side to move the player ', help_page_font_2, WHITE, screen)
		msg_7 = Message(210, 200, 13, 'downwards . Tap on the player to shoot bullets . ', help_page_font_2, WHITE, screen)
		msg_8 = Message(210, 230, 13, ' You have to kill the space obstacles and monsters . ', help_page_font_2, WHITE, screen)
		msg_9 = Message(220, 290, 13, 'If you are playing in computers , then use arrow keys', help_page_font_2, WHITE, screen)
		msg_10 = Message(210, 320, 13, 'to move the player and use mouse or space bar', help_page_font_2, WHITE, screen)
		msg_11 = Message(160, 350, 13, 'to shoot bullets and all other things . you can also navigate to up and down side', help_page_font_2, WHITE, screen)
		msg_12 = Message(211, 410, 13, 'On the top left corner of the game screen , there', help_page_font_2, WHITE, screen)
		msg_13 = Message(205, 440, 13, 'will be the player live , health and earth health .', help_page_font_2, WHITE, screen)
		msg_14 = Message(226, 470, 13, 'Click on the player indicator on top left to open menu .', help_page_font_2, WHITE, screen)
		msg_1.update()
		msg_2.update()
		msg_3.update()
		msg_4.update()
		msg_5.update()
		msg_6.update()
		msg_7.update()
		msg_8.update()
		msg_9.update()
		msg_10.update()
		msg_11.update()
		msg_12.update()
		msg_13.update()
		msg_14.update()
		exit_help_page.update()

	if exit_decision_page:
		screen.fill(BLACK)
		game_confirmation_msg.update()

		if yes_btn.draw(screen):
			running = False

		if no_btn.draw(screen):
			home_page = True
			exit_decision_page = False

	if game_page:

		current_time = pygame.time.get_ticks()
		delta_time = current_time - start_time
		if delta_time >= plane_frequency:
			if level == 1:
				type = 1
			elif level == 2:
				type = 2
			elif level == 3:
				type = 3
			elif level == 4:
				type = random.randint(4, 5)
			elif level == 5:
				type = random.randint(1, 7)

			x = random.randint(10, WIDTH - 100)
			e = Enemy(x, -150, type, earth_health)
			enemy_group.add(e)
			start_time = current_time

		if plane_destroy_count:
			if plane_destroy_count % 5 == 0 and level < 5:
				level += 1
				plane_destroy_count = 0

		p.fuel -= 0.04
		bg.update()

		p.update(moving_left, moving_right, explosion_group)
		p.draw(screen)

		player_bullet_group.update()
		player_bullet_group.draw(screen)
		enemy_bullet_group.update()
		enemy_bullet_group.draw(screen)
		explosion_group.update()
		explosion_group.draw(screen)
		fuel_group.update()
		fuel_group.draw(screen)
		powerup_group.update()
		powerup_group.draw(screen)
		earth.update(screen, enemy_group)

		enemy_group.update(enemy_bullet_group, explosion_group, game_page, score_page, earth_health)
		enemy_group.draw(screen)

		if up_arrow_btn.draw(screen):
			p.rect.y -= player_speed
		if down_arrow_btn.draw(screen):
			p.rect.y += player_speed

		if earth_health <= -10:
			game_page = False
			score_page = True

		if p.alive:
			player_hit = pygame.sprite.spritecollide(p, enemy_bullet_group, False)
			for bullet in player_hit:
				p.health -= bullet.damage
				
				x, y = bullet.rect.center
				explosion = Explosion(x, y, 1)
				explosion_group.add(explosion)

				bullet.kill()
				collision_fx.play()

			for bullet in player_bullet_group:
				planes_hit = pygame.sprite.spritecollide(bullet, enemy_group, False)
				for plane in planes_hit:
					plane.health -= bullet.damage
					if plane.health <= 0:
						x, y = plane.rect.center
						rand = random.random()
						if rand >= 0.9:
							power = Powerup(x, y)
							powerup_group.add(power)
						elif rand >= 0.3:
							fuel = Fuel(x, y)
							fuel_group.add(fuel)

						plane_destroy_count += 1
						blast_fx.play()

					x, y = bullet.rect.center
					explosion = Explosion(x, y, 1)
					explosion_group.add(explosion)

					bullet.kill()
					collision_fx.play()

			player_collide = pygame.sprite.spritecollide(p, enemy_group, True)
			if player_collide:
				x, y = p.rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)

				x, y = player_collide[0].rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)
				
				p.health = 0
				level = 1
				p.alive = False

				blast_fx.play()

			if pygame.sprite.spritecollide(p, fuel_group, True):
				p.fuel += 34
				if p.fuel >= 100:
					p.fuel = 100
				fuel_fx.play()

			if pygame.sprite.spritecollide(p, powerup_group, True):
				p.powerup += 2
				p.health += 13
				if p.health >= 100:
					p.health = 100
				fuel_fx.play()

			earth_collide = pygame.sprite.spritecollide(earth, enemy_group, True)
			if earth_collide:
				earth.health -= 10

				if earth.health <= -10:
					p.health = 0
					level = 1
					p.alive = False

		if not p.alive or p.fuel <= -15:
			if len(explosion_group) == 0:
				game_page = False
				score_page = True
				reset()

		score += 1
		score_msg.update(score)

		fuel_color = RED if p.fuel <= 40 else GREEN
		pygame.draw.rect(screen, fuel_color, (30, 20, p.fuel, 10), border_radius=4)
		pygame.draw.rect(screen, WHITE, (30, 20, 100, 10), 2, border_radius=4)
		pygame.draw.rect(screen, BLUE, (30, 32, earth_health, 10), border_radius=4)
		pygame.draw.rect(screen, WHITE, (30, 32, 100, 10), 2, border_radius=4)
		pygame.draw.rect(screen, BLUE, (30, 51, earth.health, 10), border_radius=4)
		pygame.draw.rect(screen, WHITE, (30, 51, 100, 10), 2, border_radius=4)
		screen.blit(earth_img, (10, 40))

		if p.alive and plane_img_button.draw(screen):
			home_page = False
			score_page = False
			game_page = False
			option_page = True

	pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 3, border_radius=1)
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()
