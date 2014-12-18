import math,sys,pygame

class Gust():
    def __init__(self,player):
        self.facing = player.facing
        if self.facing == "up":
            self.speed = [0, -5]
        elif self.facing == "down":
            self.speed = [0, 5]
        elif self.facing == "right":
            self.speed = [5, 0]
        elif self.facing == "left":
            self.speed = [-5, 0]
        self.image = pygame.image.load("rsc/Projectiles/gust.png")
        self.rect = self.image.get_rect()
        self.damage = 10
        self.place(player.rect.center)
        self.radius = 30
        self.move()
      
    def move(self):
        self.rect = self.rect.move(self.speed)
    
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
        
    def place(self, pt):
        self.rect.center = pt
        
    def update(self, width, height):
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        
    
