import pygame, math

class Butterfly():
	def __init__(self, image, speed = [0,0], pos = [0,0]):
		self.surface = pygame.image.load("rsc/Butterfly/Butterfly.png")
        self.surface = pygame.transform.scale(self.surface,(15,25))
        self.decras = 100
        self.rect = self.surface.get_rect()
        self.maxSpeed = 2
        xDir = random.randint(-1,1)
        yDir = random.randint(-1,1)
        self.speed = [self.maxSpeed*xDir,self.maxSpeed*yDir]    
        self.place(pos)
        self.damage = 1
        self.life = 20
        self.maxLife = 20
        self.radius = 10
        self.detectionRadius = 80
        self.didHit = False
        self.living = True
		
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
		
		
		
		
		
		
		
		
		
		
		
		
		

