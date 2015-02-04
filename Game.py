import pygame, sys, random, time
from Butterfly import Butterfly
from Player import Player
from Wasp import Wasp
from Screen import Screen
from Menu import Button
from health import HealthBar

# from QueenWasp import QueenWasp

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600
fullscreen = 0
altFlag = False
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r, g, b = 0, 0, 0
bg = pygame.image.load("rsc/Background/BG2.png")
bgRect = bg.get_rect()
bgImage = pygame.image.load("rsc/Startscreen/startscreen.png")
bgRect = bgImage.get_rect()

startButton = Button([width/6, height/1.7], 
                    "rsc/Startscreen/start.png",
                    "rsc/Startscreen/starthighlighted.png")
                                     
startButton2 = Button([width/2, height/1.7],
                    "rsc/Startscreen/options.png",
                    "rsc/Startscreen/optionshighlighted.png")
                                    
startButton3 = Button([width/1.2, height/1.7],
                    "rsc/Startscreen/quit.png",
                    "rsc/Startscreen/quit.png")
                                     
startCharacter = pygame.image.load("rsc/Startscreen/startscreen.png",
                                "rsc/Startscreen/startscreen.png")

running = False

while True:
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.quit: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    running = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton2.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton2.release(event.pos):
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton3.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton3.release(event.pos):
                    running = False
                    sys.quit()
                
        
        
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        screen.blit(startButton2.image, startButton2.rect)
        screen.blit(startButton3.image, startButton3.rect)
        #screen.blit(startCharacter.image, startCharacter.rect)
        pygame.display.flip()
        
    


    #timer = Score([80, height - 25], "Time: ", 36)
    #timerWait = 0
    #timerWaitMax = 6

    #Score = Score([80, height - 50], "Score: ", 36)
    #if Butterfly = self.living = True:
    #Score = Score + 100



    player = Player([375,300])
    #player = Player([width / 4, height / 2])
    #75 for both
    healthbar = HealthBar([width - 75, 125])  #DEFAULT: 100 MODED: 200
    #600

    butterflys = []
    butterflys += [Butterfly("rsc/Butterfly/Butterfly.png", [1, 2], [100, 125])]

    wasps = []
    wasps += [Wasp("rsc/Wasp/Wasp.png", [1, 2], [100, 125])]

    projectiles = []

    while running:
        st = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
                elif (event.key == pygame.K_e or event.key == pygame.K_j):
                    projectiles += [player.attack("gust")]
                elif (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = True
                elif (event.key == pygame.K_RETURN) and altFlag:
                    if fullscreen == 0:
                        fullscreen = pygame.FULLSCREEN
                    else:
                        fullscreen = 0
                    screen = pygame.display.set_mode((width, height), fullscreen)
                    pygame.display.flip()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
                elif (event.key == pygame.K_j ):
                    player.attack("stop gust")
                elif (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = False

    
    
        #print "controls:", time.time() - st
        if len(butterflys) < 10:
            if random.randint(0, 1 * 60) == 0:
                butterflys += [Butterfly("rsc/Butterfly/Butterfly2.png",
                                         [random.randint(0, 10), random.randint(0, 10)],
                                         [random.randint(100, width - 100), random.randint(100, height - 100)]
                )]

        if len(wasps) < 10:
            if random.randint(0, 5 * 60) == 0:
                wasps += [Wasp("rsc/Wasp/Wasp.png",
                               [random.randint(0, 10), random.randint(0, 10)],
                               [random.randint(100, width - 100), random.randint(100, height - 100)]
                )]
                #if timerWait < timerWaitMax:
                #   timerWait += 1
                #else:
                #   timerWait = o
                #  timer.increaseScore(.1)
        player.update(width, height)
        #timer.update()
        #print "spawn:", time.time() - st
        player.update(width, height)
        for butterfly in butterflys:
            butterfly.update(width, height)
        for wasp in wasps:
            wasp.update(width, height, player)
        for projectile in projectiles:
            projectile.update(width, height)

        #print "update:", time.time() - st
        for bully in butterflys:
            for victem in butterflys:
                bully.collideButterfly(victem)
                bully.collidePlayer(player)
        for bully in wasps:
            for victem in wasps:
                bully.collideWasp(victem)
            bully.collidePlayer(player)
            for projectile in projectiles:
                bully.collide_attack(projectile)
                if projectile.collideGust(bully):
                    projectiles.remove(projectile)
                

        #print "collide:", time.time() - st
        for butterfly in butterflys:
            if not butterfly.living:
                butterflys.remove(butterfly)
        for wasp in wasps:
            if not wasp.living:
                wasps.remove(wasp)

        if player.health <= 0:
            player.living = False

        #print "die:", time.time() - st
        bgColor = r, g, b
        screen.fill(bgColor)
        screen.blit(bg, bgRect)
        screen.blit(healthbar.surface, healthbar.rect)
        for butterfly in butterflys:
            screen.blit(butterfly.image, butterfly.rect)
            player.collideWasp(healthbar)
        for wasp in wasps:
            screen.blit(wasp.image, wasp.rect)
        #for wasphealthbar in wasphealthbar:
         #   screen.blit(wasphealthbar.image, wasphealthbar.rect)
        screen.blit(player.image, player.rect)
        #screen.blit(timer.image, timer.rect)
        #screen.blit(Score.image, Score.rect)
        for projectile in projectiles:
            screen.blit(projectile.image, projectile.rect)
        
       
        for projectile in projectiles:
            if not projectile.living:
                projectiles.remove(projectile) 
        pygame.display.flip()
        #print "draw:", time.time() - st
        clock.tick(60)















