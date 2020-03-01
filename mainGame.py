import os, sys
import pygame
from pygame.locals import *
from Zero import *
from Carrier import *
from F4F import *

pygame.init()
SCREENRECT = pg.Rect(0, 0, 640, 480)
fullscreen = False
winstyle = 0

bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

background_image = pygame.image.load('background.png').convert()
background = pg.Surface(SCREENRECT.size)
for x in range(0, SCREENRECT.width, background_image.get_width()):
	background.blit(background_image, (x, 0))

screen.blit(background, (0,0))

pg.display.flip()

all = pg.sprite.RenderUpdates()
planes = pg.sprite.Group()
enemy_planes = pg.sprite.Group()
Zero.containers = all, planes
Carrier.containers = all
F4F.containers = all, enemy_planes

clock = pg.time.Clock()
for i in range(5):
	Zero(i * 20 + 500, 10* i + 200,enemy_planes)

for i in range(4):
	F4F(i * 20 + 100, 10* i + 300,planes)

Carrier(400,400)


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	print(all.sprites())
	for plane in all.sprites():
		print("hi")
	all.clear(screen, background)
	all.update()
	dirty = all.draw(screen)
	pygame.display.update(dirty)
	clock.tick(40)
