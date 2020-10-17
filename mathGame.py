import pygame, sys, time
from pygame.locals import *



class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def redrawWindow():
    windowSurface.fill((WHITE))
    additionButton.draw(windowSurface, (BLUE))
    subtractionButton.draw(windowSurface, (BLUE))

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 800
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
      0, 32)

pygame.display.set_caption('Interactive Math Game')

# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
                                #l/r 
additionButton = button((GREEN), 50, 225, 250, 100, 'Addition')
subtractionButton = button((GREEN), 500, 225, 250, 100, 'Subtraction')
# Run the game loop.
while True:
    redrawWindow()
    pygame.display.update()
    #Check for the QUIT event.
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if additionButton.isOver(pos):
                print('clicked addition button')
            if subtractionButton.isOver(pos):
                print('clicked subtraction button')

        if event.type == pygame.MOUSEMOTION:
            if additionButton.isOver(pos):
                additionButton.color = (RED)
            else:
                additionButton.color = (GREEN)

            if subtractionButton.isOver(pos):
                subtractionButton.color = (RED)
            else:
                subtractionButton.color = (GREEN)
    #Draw the white background onto the surface.
    #windowSurface.fill(WHITE)




    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)