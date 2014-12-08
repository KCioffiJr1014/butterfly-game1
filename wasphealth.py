import pygame,math,sys,random

class WaspHealthBar():
    def __init__(self, wasp):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/Health/0%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/5%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/10%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/15%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/20%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/25%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/30%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/35%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/40%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/45%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/55%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/60%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/65%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/70%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/75%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/80%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/85%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/90%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/95%.png")]
        self.surfaces += [pygame.image.load("rsc/Health/100%.png")]
        self.wasp = wasp
        
        self.maxFrame = len(self.surfaces)-1
       #self.surface = pygame.transform.scale(self.faces,(100,25))
        self.frame = self.maxFrame
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.wasp = wasp
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
            self.frame = 19
            print percentLife
        elif percentLife > .90:
            self.frame = 18
            print percentLife
        elif percentLife > .85:
            self.frame = 17
            print percentLife
        elif percentLife > .80:
            self.frame = 16
            print percentLife
        elif percentLife > .75:
            self.frame = 15
            print percentLife
        elif percentLife > .70:
            self.frame = 14
            print percentLife
        elif percentLife > .65:
            self.frame = 13
            print percentLife
        elif percentLife > .60:
            self.frame = 12
            print percentLife
        elif percentLife > .50:
            self.frame = 11
            print percentLife
        elif percentLife > .45:
            self.frame = 10
            print percentLife
        elif percentLife > .40:
            self.frame = 9
            print percentLife
        elif percentLife > .35:
            self.frame = 8
            print percentLife
        elif percentLife > .30:
            self.frame = 7
            print percentLife
        elif percentLife > .25:
            self.frame = 6
            print percentLife
        elif percentLife > .20:
            self.frame = 5
            print percentLife
        elif percentLife > .15:
            self.frame = 4
            print percentLife
        elif percentLife > .10:
            self.frame = 3
            print percentLife
        elif percentLife > .5:
            self.frame = 2
            print percentLife
        elif percentLife > .1:
            self.frame = 1
            print percentLife
        else:
            self.frame = 0
            print percentLife
          #  self.living = False
        #self.surface = self.surfaces[self.frame]
        
        self.rect.center = [self.wasp.rect.center[0],self.wasp.rect.center[1]-20]
