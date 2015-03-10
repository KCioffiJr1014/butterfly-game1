import pygame, math
from Gust import Gust
from spray import Spray
from health import *


class Player():
    def __init__(self, pos):
        self.upImages = [pygame.image.load("rsc/Player/MU.png"),
                         pygame.image.load("rsc/Player/MU2.png")]
        self.downImages = [pygame.image.load("rsc/Player/MD.png"),
                           pygame.image.load("rsc/Player/MD2.png")]
        self.leftImages = [pygame.image.load("rsc/Player/ML.png"),
                           pygame.image.load("rsc/Player/ML2.png")]
        self.rightImages = [pygame.image.load("rsc/Player/MR.png"),
                            pygame.image.load("rsc/Player/MR2.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.maxSpeed = 7
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.gusting = False
        self.gustCount = 0
        self.maxGustCount = 10
        self.gustCoolDown = 0
        self.gustCoolDownMax = 50
        self.gustdelay = 5
        self.spraying = False
        self.sprayCount = 0
        self.maxSprayCount = 10
        self.sprayCoolDown = 0
        self.sprayCoolDownMax = 50
        self.spraydelay = 5
        self.radius = 20
        self.didBounceX = False
        self.didBounceY = False
        self.health = 250
        self.maxHealth = 250
        self.nodamage = 0
        self.living = True
        self.place(pos)
        self.damage = 40
        
    def place(self, pos):
        self.rect.center = pos
    
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        self.animate()
        self.facingChanged = False
        if self.gustCoolDown > 0:
            self.gustCoolDown -=1
        if self.sprayCoolDown > 0:
            self.sprayCoolDown -=1
        
   
   
    def modifyHealth (self, amount):
        self.health += amount
        if self.health <= 0:
            self.health = 0
            self.living = False
        elif self.health >= self.maxHealth:
            self.health = self.maxHealth
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        
    def attack(self, atk):
        if atk == "gust" and self.gustCoolDown == 0:
            self.gusting = True
            self.gustCoolDown = self.gustCoolDownMax
            return [Gust(self)]
        if atk == "spray" and self.sprayCoolDown == 0:
            self.spraying = True
            self.sprayCoolDown = self.sprayCoolDownMax
            return [Spray(self)]
        return []

    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
                #print "hit xWall"
                
    def enemyCollide(self, other, effect):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom):
                    self.hurt = True
                    if self.nodamage == 0:
                        self.modifyHealth(-other.damage)
                        effect.update(self.health, self.maxHealth) 
                        print self.health
                    self.nodamage += 1
                    if self.nodamage == 25:
                        self.nodamage = 0
                        
    def stingerCollide(self, other, effect):
        if (self.rect.right > stinger.rect.left 
            and self.rect.left < stinger.rect.right):
                if (self.rect.bottom > stinger.rect.top and 
                    self.rect.top < stinger.rect.bottom):
                    self.hurt = True
                    if self.nodamage == 0:
                        self.modifyHealth(-other.damage)
                        effect.update(self.health, self.maxHealth) 
                        print self.health
                    self.nodamage += 1
                    if self.nodamage == 25:
                        self.nodamage = 0
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.facingChanged = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0
            
    
    '''def collideWasp(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom):
                    self.hurt = True
                    if self.nodamage == 0:
                        self.modifyHealth(-other.damage)
                        effect.update(self.health, self.maxHealth) 
                        print self.health
                    self.nodamage += 1
                    if self.nodamage == 25:
                        self.nodamage = 0'''
    
    
    
    
    def collideQueenWasp(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
                        
                        
        
        
        
        
        
        
        
        
        
        
        
        
        

