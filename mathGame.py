import pygame, sys, time
import pygame as py
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
	windowSurface.blit(background,(0,0))
	additionButton.draw(windowSurface, (BLUE))
	subtractionButton.draw(windowSurface, (BLUE))
	#added DC
	multiplicationButton.draw(windowSurface, (BLUE))
	exitButton.draw(windowSurface, (WHITE))


# Set up pygame.
pygame.init()

window_width = 800
window_height = 700

size = (window_width, window_height)
windowSurface = pygame.display.set_mode(size)

pygame.display.set_caption('Interactive Math Game')


# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
#added DC
PURPLE = (204, 153, 255)
LIGHT_GREEN = (102, 255, 102)
TEAL = (0, 255, 255)

background = py.image.load("bg.png") ## Load the image file
background = py.transform.scale(background,(window_width,window_height)) ## Make it the same size as the screen
							#l/r 
additionButton = button((PURPLE), 300, 200, 200, 100, 'Add')
subtractionButton = button((LIGHT_GREEN), 300, 310, 200, 100, 'Subtract')
#added DC
multiplicationButton = button((TEAL), 300, 420, 200, 100, 'Multiply')
exitButton = button((WHITE), 750, 0, 50, 50, 'X')

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
				print('clicked add button')
			if subtractionButton.isOver(pos):
				print('clicked subtract button')
				#added DC
			if multiplicationButton.isOver(pos):
				print('clicked multiply button')
			if exitButton.isOver(pos):
				pygame.quit()
				sys.exit()


		if event.type == pygame.MOUSEMOTION:
			if additionButton.isOver(pos):
				additionButton.color = (WHITE)
			else:
				additionButton.color = (PURPLE)

			if subtractionButton.isOver(pos):
				subtractionButton.color = (WHITE)
			else:
				subtractionButton.color = (LIGHT_GREEN)
				#added DC
			if multiplicationButton.isOver(pos):
				multiplicationButton.color = (WHITE)
			else:
				multiplicationButton.color = (TEAL)
			if exitButton.isOver(pos):
				exitButton.color = (RED)
			else:
				exitButton.color = (WHITE)
				
				

	# Draw the window onto the screen.
	pygame.display.update()
	time.sleep(0.02)