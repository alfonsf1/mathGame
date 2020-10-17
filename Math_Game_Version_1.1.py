import pygame, sys, time
from pygame.locals import *

	
PURPLE = (204, 153, 255)
LIGHT_GREEN = (102, 255, 102)
TEAL = (0, 255, 255)

pygame.init()

window_width=800
window_height=500

animation_increment=10
clock_tick_rate=20

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Interactive Math Game')

dead = False

clock = pygame.time.Clock()
background_image = pygame.image.load("4.jpg").convert()

while(dead==False):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				dead = True
				
		screen.blit(background_image, [0, 0])
	
		pygame.display.flip()
		clock.tick(clock_tick_rate)



game1 =pygmae.Rect(0,0,200,150)
pygame.draw.rect(screen, [255, 100, 0], game1)


