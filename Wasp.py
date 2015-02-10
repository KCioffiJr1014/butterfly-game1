import pygame, math
from wasphealth import WaspHealthBar
from Gust import Gust

class Wasp():
    def __init__(self, image, speed = [0,0], pos = [0,0]):
        self.image = pygame.image.load("rsc/Wasp/Wasp.png")
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[0]
        self.speed = [self.speedx, self.speedy]
        self.maxSpeed = 20
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True
        self.healthbar = WaspHealthBar(self)
        self.life = True 
        self.maxLife = True
        self.damage = 1
        self.health = 20
        self.didHit = False
        self.maxHealth = 25
        self.detectionRadius = 80
        
    def place(self, pos):
        self.rect.center = pos
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        
    def update(self, width, height, player):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move(player)
        self.collideWall(width, height)
        self.image.blit(self.healthbar.image, self.healthbar.rect)
        
    def move(self, player):
        if player != None:
            self.detect(player)
        self.rect = self.rect.move(self.speed)

    def detect(self,player):
        if self.distToPoint(player.rect.center) < self.detectionRadius:
            pX = player.rect.center[0]
            pY = player.rect.center[1]
            zX = self.rect.center[0]
            zY = self.rect.center[1]
           
            if pX > zX:
                self.speed[0] = self.maxSpeed
            elif pX < zX:
                self.speed[0] = -self.maxSpeed
            else:
                self.speed[0] = 0
       
            if pY > zY:
                self.speed[1] = self.maxSpeed
            elif pY < zY:
                self.speed[1] = -self.maxSpeed
            else:
                self.speed[1] = 0
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
               self.speedx = -self.speedx
               self.didBounceX = True
               #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
               self.speedy = -self.speedy
               self.didBounceY = True
               #print "hit xWall"
        
    def collideWasp(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
                            #print "hit wasp"
                        if not self.didHit:
                            self.speed[0] = self.speed[0] * -1
                            self.speed[1] = self.speed[1] * -1
                            self.move(None)
                            self.move(None)
                            self.didHit = True
                        return True
            return False
    
    def collideGust(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = False
                            
    def collidePlayer(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        pass
                        #self.living = False

    def collideGust(self, attack):
        if (self.rect.right > attack.rect.left and self.rect.left < attack.rect.right):
            if (self.rect.bottom > attack.rect.top and self.rect.top < attack.rect.bottom):
                if (self.distToPoint(attack.rect.center) < self.radius + attack.radius):
<<<<<<< HEAD
                    #self.life -= attack.damage
                    #self.healthbar.update()
                    #print "Hit", self.life
                    #if self.life <= 0:
=======
                    print "Hit", self.health
                    self.health -= attack.damage
                    self.healthbar.update()
                    print "Hit Done", self.health
                    if self.health <= 0:
>>>>>>> origin/master
                        self.living = False
                                            
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
    '''def Hurt():
		hurt = 0
		if collidePlayer == True:
			hurt += 1
    '''     
            
		
        
