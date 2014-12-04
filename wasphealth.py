import pygame,math,sys,random

class WaspHealthBar():
    def __init__(self, wasp):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/Dead.png")] #1
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/1%.png")]   #2
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/5%.png")]   #3
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/10%.png")]  #4
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/15%.png")]  #5
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/20%.png")]  #6
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/25%.png")]  #7
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/30%.png")]  #8
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/35%.png")]  #9
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/40%.png")]  #10
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/45%.png")]  #11
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/50%.png")]  #12
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/55%.png")]  #13
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/60%.png")]  #14
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/65%.png")]  #15
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/70%.png")]  #16
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/75%.png")]  #17
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/80%.png")]  #18
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/85%.png")]  #19
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/90%.png")]  #20
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/95%.png")]  #21
        self.surfaces += [pygame.image.load("rsc/Zombies/Health/100%.png")]  #22
        
        
        
        self.maxFrame = len(self.surfaces)-1
       #self.surface = pygame.transform.scale(self.faces,(100,25))
        self.frame = self.maxFrame
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.zombie = wasp
        self.rect.center = [self.wasp.rect.center[0],self.wasp.rect.center[1]-20]
        #if pygame.mixer:
        #    self.healthSound = pygame.mixer.Sound("health.wav")
       
    def  __str__(self):
        return "I'm a Health Bar " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def helth_bare(self):
        pass
            
    def update(self):
        percentLife = float(self.wasp.life)/float(self.wasp.maxLife)
        if percentLife > .95:
            self.frame = 20
        elif percentLife > .90:
            self.frame = 19
        elif percentLife > .85:
            self.frame = 18
        elif percentLife > .80:
            self.frame = 17
        elif percentLife > .75:
            self.frame = 16
        elif percentLife > .70:
            self.frame = 15
        elif percentLife > .65:
            self.frame = 14
        elif percentLife > .60:
            self.frame = 13
        elif percentLife > .55:
            self.frame = 12
        elif percentLife > .50:
            self.frame = 11
        elif percentLife > .45:
            self.frame = 10
        elif percentLife > .40:
            self.frame = 9
        elif percentLife > .35:
            self.frame = 8
        elif percentLife > .30:
            self.frame = 7
        elif percentLife > .25:
            self.frame = 6
        elif percentLife > .20:
            self.frame = 5
        elif percentLife > .15:
            self.frame = 4
        elif percentLife > .10:
            self.frame = 3
        elif percentLife > .5:
            self.frame = 2
        elif percentLife > .1:
            self.frame = 1
        else:
            self.frame = 0
          #  self.living = False
        #self.surface = self.surfaces[self.frame]
        
        self.rect.center = [self.wasp.rect.center[0],self.wasp.rect.center[1]-20]