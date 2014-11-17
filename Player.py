import pygame, math

class Player():
	def __init__(self, image, speed = [0,0], pos = [0,0]):
	
		
	def place(self, pos):
		self.rect.center = pos
		
	def update(self, width, height):
		
		
	def move(self):
		self.rect = self.rect.move(self.speed)

	def collideWall(self, width, height):
		
		
	def collideBall(self, other):
		
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[1]
		x2 = pt[0]
		y2 = pt[1]
		return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
		
		
		
		
		
		
		
		
		
		
		
		
		

