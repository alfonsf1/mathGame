import pygame, sys, time
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
      0, 32)

pygame.display.set_caption('Interactive Math Game')

# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Run the game loop.
while True:
    #Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Draw the white background onto the surface.
    windowSurface.fill(WHITE)




    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)