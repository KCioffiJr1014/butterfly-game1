from Wasp import *
from Button import *
from Player import *
import pygame, sys, random
pygame.init()
width = 800
height = 600


size = width, height
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
bgImage = pygame.image.load("rsc/Startscreen/startscreen.png").convert()
bgRect = bgImage.get_rect()

startButton = Button([width/2, height-300], 
                                     "rsc/Startscreen/Start Base.png", 
                                     "rsc/Startscreen/Start Clicked.png")
                                     
startCharacter = pygame.image.load("rsc/Startscreen/Start Screen.png",
                                "rsc/Startscreen/Start Screen.png")


clock = pygame.time.Clock()
bgColor = r,g,b = 100, 255, 80
running = False

while True:
        while not running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        running = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                startButton.click(event.pos)
                        if event.type == pygame.MOUSEBUTTONUP:
                                if startButton.release(event.pos):
                                        running = True
                                        
                bgColor = r,g,b
                screen.fill(bgColor)
                screen.blit(bgImage, bgRect)
                screen.blit(startButton.image, startButton.rect)
                pygame.display.flip()
                clock.tick(60)
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        bgColor = r,g,b
        screen.fill(bgColor)
        pygame.display.flip()
        clock.tick(60)
