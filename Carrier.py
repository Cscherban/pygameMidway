import pygame as pg
import math
vec = pg.math.Vector2

class Carrier(pg.sprite.Sprite):
	def __init__(self, x ,y):
		pg.sprite.Sprite.__init__(self, self.containers)
		self.vel = vec(-.01,-.01)
		self.original = pg.image.load('boat.png').convert_alpha()
		self.image = self.original
		self.state = "circle"
		self.rect = self.image.get_rect().move(0,12)
		self.pos = vec(x,y)
		self.facing = -.74
		self.r_detect = 500
		self.r_engage = 40

	def update(self):
		self.pos += self.vel
		#angle = -90 + (180 / math.pi) * -math.atan2(self.vel.y, self.vel.x)
		#self.image = pg.transform.rotate(self.original, int(angle))
		self.rect = self.image.get_rect(center=self.pos)
		#if self.state == "Attack":
		#	print("hi")
		#detected_enemy = pg.sprite.spritecollide(self, self.containers[0], False, lambda x,y: math.hypot(x.pos.x - y.pos.x,x.pos.y - y.pos.y) < x.r_detect)
