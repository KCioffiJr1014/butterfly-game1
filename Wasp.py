import pygame, math
from wasphealth import WaspHealthBar

class Wasp():
    def __init__(self, image, speed = [0,0], pos = [0,0]):
        self.image = pygame.image.load("rsc/Wasp/Wasp.png")
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[0]
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True
        self.healthbar = WaspHealthBar(self)
        self.life = True 
        self.maxLife = True
        self.health = 20
        self.maxHealth = 25
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        
    def move(self):
        self.rect = self.rect.move(self.speed)

    def chase(self,player):
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
            #print "trying to hit Wall"
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
                            
                            
    def collidePlayer(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
