
import pygame,math,sys,random

class WaspHealthBar():
    def __init__(self, wasp):
        self.images = []
        self.images += [pygame.image.load("rsc/Health/0%.png")]
        self.images += [pygame.image.load("rsc/Health/5%.png")]
        self.images += [pygame.image.load("rsc/Health/10%.png")]
        self.images += [pygame.image.load("rsc/Health/15%.png")]
        self.images += [pygame.image.load("rsc/Health/20%.png")]
        self.images += [pygame.image.load("rsc/Health/25%.png")]
        self.images += [pygame.image.load("rsc/Health/30%.png")]
        self.images += [pygame.image.load("rsc/Health/35%.png")]
        self.images += [pygame.image.load("rsc/Health/40%.png")]
        self.images += [pygame.image.load("rsc/Health/45%.png")]
        self.images += [pygame.image.load("rsc/Health/55%.png")]
        self.images += [pygame.image.load("rsc/Health/60%.png")]
        self.images += [pygame.image.load("rsc/Health/65%.png")]
        self.images += [pygame.image.load("rsc/Health/70%.png")]
        self.images += [pygame.image.load("rsc/Health/75%.png")]
        self.images += [pygame.image.load("rsc/Health/80%.png")]
        self.images += [pygame.image.load("rsc/Health/85%.png")]
        self.images += [pygame.image.load("rsc/Health/90%.png")]
        self.images += [pygame.image.load("rsc/Health/95%.png")]
        self.images += [pygame.image.load("rsc/Health/100%.png")]
        self.wasp = wasp
        newimages =[]
        self.maxFrame = len(self.images)-1
        for image in self.images:
            newimages += [pygame.transform.scale(image,(100,25))]
        self.images = newimages
        self.frame = self.maxFrame
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.wasp = wasp
        #self.rect.center = [self.wasp.rect.center[0],self.wasp.rect.center[1]]
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
            print "wh:",percentLife
        elif percentLife > .90:
            self.frame = 18
            print "wh:",percentLife
        elif percentLife > .85:
            self.frame = 17
            print "wh:",percentLife
        elif percentLife > .80:
            self.frame = 16
            print "wh:",percentLife
        elif percentLife > .75:
            self.frame = 15
            print "wh:",percentLife
        elif percentLife > .70:
            self.frame = 14
            print "wh:",percentLife
        elif percentLife > .65:
            self.frame = 13
            print "wh:",percentLife
        elif percentLife > .60:
            self.frame = 12
            print "wh:",percentLife
        elif percentLife > .50:
            self.frame = 11
            print "wh:",percentLife
        elif percentLife > .45:
            self.frame = 10
            print "wh:",percentLife
        elif percentLife > .40:
            self.frame = 9
            print "wh:",percentLife
        elif percentLife > .35:
            self.frame = 8
            print "wh:",percentLife
        elif percentLife > .30:
            self.frame = 7
            print "wh:",percentLife
        elif percentLife > .25:
            self.frame = 6
            print "wh:",percentLife
        elif percentLife > .20:
            self.frame = 5
            print "wh:",percentLife
        elif percentLife > .15:
            self.frame = 4
            print "wh:",percentLife
        elif percentLife > .10:
            self.frame = 3
            print "wh:",percentLife
        elif percentLife > .5:
            self.frame = 2
            print percentLife
        elif percentLife > .1:
            self.frame = 1
            print "wh:",percentLife
        else:
            self.frame = 0
            print "wh:",percentLife
          #  self.living = False
        #self.image = self.images[self.frame]
        self.image = self.images[self.frame]
