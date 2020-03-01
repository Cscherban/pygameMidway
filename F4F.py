import pygame as pg
import math
import random
vec = pg.math.Vector2

class F4F(pg.sprite.Sprite):
	def __init__(self, x ,y,enemy_group):
		pg.sprite.Sprite.__init__(self, self.containers)
		self.vel = vec(10,10)
		self.original = pg.image.load('f4f.png').convert_alpha()
		self.image = self.original
		self.state = "circle"
		self.rect = self.image.get_rect().move(0,12)
		self.pos = vec(x,y)
		print(self.rect)
		self.facing = -.74
		self.r_detect = 500
		self.r_engage = 10
		self.target = None
		self.speed = 1
		self.damage = 15
		self.hp = 100
		self.enemy_group = enemy_group

	def update(self):
		if (self.hp <= 0):
			self.kill()
		self.pos += self.vel
		angle = 0
		if self.state == "circle":
			self.vel = self.vel.rotate(1)
			angle = (180 / math.pi) * -math.atan2(self.vel.y, self.vel.x)
			detected = pg.sprite.spritecollide(self, self.enemy_group, False, lambda x,y: math.hypot(x.pos.x - y.pos.x,x.pos.y - y.pos.y) < x.r_detect)
			if (len(detected) > 0):
				self.state = "Engage"
				self.target = random.choice(detected)
				print("found enemy")

		elif self.state == "Engage":
			print(self.vel)
			target_pos = self.target.pos
			angle = (180 / math.pi) * -math.atan2(target_pos.y - self.pos.y, target_pos.x - self.pos.x)
			self.vel = vec(self.speed,0).rotate(360 - angle)
			print(angle)
			dist = math.hypot(target_pos.x - self.pos.x,target_pos.y - self.pos.y)
			if(dist < self.r_engage):
				self.target.hp -= self.damage
			if(self.target.hp <= 0):
				self.state = "circle"
				self.target == None

		self.image = pg.transform.rotate(self.original, int(-90 + angle))
		self.rect = self.image.get_rect(center=self.pos)
