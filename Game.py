import pygame, sys, random
from Butterfly import Butterfly
from Player import Player
from Wasp import Wasp
#from QueenWasp import QueenWasp

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height
bgColor = r,g,b = 0, 0, 0
bg =  pygame.image.load("rsc/Background/Bg.png")
bgRect = bg.get_rect()

#timer = Score([80, height - 25], "Time: ", 36)
#timerWait = 0
#timerWaitMax = 6

#Score = Score([80, height - 50], "Score: ", 36)


screen = pygame.display.set_mode(size)

player = Player([width/2, height/2])

butterflys = []
butterflys += [Butterfly("rsc/Butterfly/Butterfly2.png",[1,2], [100, 125])]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				player.go("up")
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				player.go("right")
			if event.key == pygame.K_s or event.key == pygame.K_DOWN:
				player.go("down")
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.go("left")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				player.go("stop up")
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				player.go("stop right")
			if event.key == pygame.K_s or event.key == pygame.K_DOWN:
				player.go("stop down")
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.go("stop left")
		
	if len(butterflys) < 10:
		if random.randint(0, .25*60) == 0:
			butterflys += [Butterfly("rsc/Butterfly/Butterfly.png",
					  [random.randint(0,10), random.randint(0,10)],
					  [random.randint(100, width-100), random.randint(100, height-100)]
					  )]
	#if timerWait < timerWaitMax:
	#	timerWait += 1
	#else:
	#	timerWait = 0
	#	timer.increaseScore(.1)
	player.update(width, height)
	#timer.update()
	print butterflys
	for butterfly in butterflys:
		butterfly.update(width, height)
	player.update(width, height)
	for butterfly in butterflys:
		butterfly.update(width, height)
		
	for bully in butterflys:
		for victem in butterflys:
			bully.collideButterfly(victem)
			bully.collidePlayer(player)
	
	for butterfly in butterflys:
		if not butterfly.living:
			butterflys.remove(butterfly)
	
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bg,bgRect)
	for butterfly in butterflys:
		screen.blit(butterfly.image, butterfly.rect)
	screen.blit(player.image, player.rect)
	#screen.blit(timer.image, timer.rect)
	#screen.blit(Score.image, Score.rect)
	pygame.display.flip()
	clock.tick(60)
