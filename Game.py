import pygame, sys, random, time
from Butterfly import Butterfly
from Player import Player
from Wasp import Wasp
from Screen import Screen
from Menu import Button
from health import HealthBar
from spray import Spray
from Stinger import Stinger
from QueenWasp import QueenWasp

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600
fullscreen = 0
altFlag = False
size = width, height
screen = pygame.display.set_mode(size)


player = Player([375,300])

healthbar = HealthBar([width - 75, 125])  #DEFAULT: 100 MODED: 200

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
                    sys.exit()
                
        
        
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        screen.blit(startButton2.image, startButton2.rect)
        screen.blit(startButton3.image, startButton3.rect)
        pygame.display.flip()
        

	player = Player([375,300])
    #75 for both
    healthbar = HealthBar([width - 75, 125])  #DEFAULT: 100 MODED: 200
    #600


    butterflys = []
    maxButterfly = 5
    butterflys += [Butterfly("rsc/Butterfly/Butterfly.png", [1, 2], [100, 125])]

    wasps = []
    maxWasp = 3
    wasps += [Wasp("rsc/Wasp/Wasp.png", [1, 2], [100, 125])]
    
    queenWasps = []
    maxqueenWasps = 1
    queenWasps += [QueenWasp("rsc/Wasp/QueenWasp.png", [1, 2], [100, 125])]
    
    stingers = []
    maxStingers = 1
    
    

    projectiles = []

    while running and player.living:
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
                    projectiles += player.attack("gust")
                elif (event.key == pygame.K_e or event.key == pygame.K_k):
                    projectiles += player.attack("spray")
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
                elif (event.key == pygame.K_k ):
                    player.attack("stop spray")
                elif (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = False

        if len(butterflys) < maxButterfly:
            if random.randint(0, 1 * 60) == 0:
                butterflys += [Butterfly("rsc/Butterfly/Butterfly2.png",
                                         [random.randint(0, 10), random.randint(0, 10)],
                                         [random.randint(100, width - 400), random.randint(100, height - 400)]
                )]

        if len(wasps) < maxWasp:
            if random.randint(0, 5 * 60) == 0:
                wasps += [Wasp("rsc/Wasp/Wasp.png",
                               [random.randint(0, 10), random.randint(0, 10)],
                               [random.randint(400, width - 100), random.randint(400, height - 100)]
                )]
        
        if len(queenWasps) < maxqueenWasps:
            if random.randint(0, 5 * 60) == 0:
                queenWasps += [QueenWasp("rsc/Wasp/QueenWasp.png",
                               [random.randint(0, 10), random.randint(0, 10)],
                               [random.randint(400, width - 100), random.randint(400, height - 100)]
                )]
                
        if len(stingers) < maxStingers:
            for wasp in queenWasps:
                if random.randint(0, 1 * 60) == 0:
                    stingers += [Stinger(wasp)]
                
        player.update(width, height)
        for butterfly in butterflys:
            butterfly.update(width, height)
        for wasp in wasps:
            wasp.update(width, height, player)
        for queenWasp in queenWasps:
            queenWasp.update(width, height, player)
        for projectile in projectiles:
            projectile.update(width, height)

        for bully in butterflys:
            for victem in butterflys:
                bully.collideButterfly(victem)
                bully.collidePlayer(player)
        for bully in wasps:
            for victem in wasps:
                bully.collideWasp(victem)
                player.enemyCollide(wasp,healthbar)
            bully.collidePlayer(player)
            for projectile in projectiles:
                bully.collideGust(projectile)
                if projectile.collideGust(bully):
                    projectiles.remove(projectile)
                bully.collideSpray(projectile)
                if projectile.collideSpray(bully):
                    projectiles.remove(projectile)
                

        for butterfly in butterflys:
            if not butterfly.living:
                butterflys.remove(butterfly)
        for wasp in wasps:
            if not wasp.living:
                wasps.remove(wasp)
        for projectile in projectiles:
            if not projectile.living:
                projectiles.remove(projectile)
        if player.health <= 0:
            player.living = False

        bgColor = r, g, b
        screen.fill(bgColor)
        screen.blit(bg, bgRect)
        screen.blit(healthbar.surface, healthbar.rect)
        for butterfly in butterflys:
            screen.blit(butterfly.image, butterfly.rect)
        for wasp in wasps:
            screen.blit(wasp.image, wasp.rect)
        screen.blit(player.image, player.rect)
        for queenWasp in queenWasps:
            screen.blit(queenWasp.image, wasp.rect)
        screen.blit(player.image, player.rect)
        
        while player.living == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                print "dead me"
        
        for projectile in projectiles:
            screen.blit(projectile.image, projectile.rect)
        pygame.display.flip()
        #print "draw:", time.time() - st
        clock.tick(60)


    endButton = Button([width/5, height/2], 
                    "rsc/deathscreen/tryagain.png",
                    "rsc/deathscreen/tryagainhighlighted.png")
                                     
    endButton2 = Button([width/3, height/2],
                    "rsc/deathscreen/quit.png",
                    "rsc/deathscreen/quithighlighted.png")
                                     
    endCharacter = pygame.image.load("rsc/deathscreen/deathscreen.png",
                                "rsc/deathscreen/deathscreen.png")
    
    while running and not player.living:
        for event in pygame.event.get():
            if event.type == pygame.quit: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                endButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if endButton.release(event.pos):
                    running = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                endButton2.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if endButton2.release(event.pos):
                    running = False
                    sys.exit()
        
        screen.blit(endButton.image, endButton.rect)
        screen.blit(endButton2.image, endButton2.rect)
        

