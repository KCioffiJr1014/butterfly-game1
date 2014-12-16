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
        
    def place(self, pt):
        self.rect.center = pt
        
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        self.animate()
        
    
