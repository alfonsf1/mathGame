import pygame, random, sys
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ORANGE = (245,99,15)
	
	
class Menu(object):
	state = -1
	def __init__(self,items,font_color=(15,160,245),select_color=(245,99,15),ttf_font=None,font_size=25):
		self.font_color = font_color
		self.select_color = select_color
		self.items = items
		self.font = pygame.font.Font(ttf_font,font_size)
		# Generate a list that will contain the rect for each item
		self.rect_list = self.get_rect_list(items)

	def get_rect_list(self,items):
		rect_list = []
		for index, item in enumerate(items):
			# determine the amount of space needed to render text
			size = self.font.size(item)
			# Get the width and height of the text
			width = size[0]
			height = size[1]

			posX = (SCREEN_WIDTH / 2) - (width /2)
			# t_h: total heigth of the text block
			t_h = len(items) * height
			posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
			# Create rects
			rect = pygame.Rect(posX,posY,width,height)
			# Add rect to the list
			rect_list.append(rect)

		return rect_list

	def collide_points(self):
		index = -1
		mouse_pos = pygame.mouse.get_pos()
		for i,rect in enumerate(self.rect_list):
			if rect.collidepoint(mouse_pos):
				index = i

		return index

	def update(self):
		# assign collide_points to state
		self.state = self.collide_points()
		
	def display_frame(self,screen):
		for index, item in enumerate(self.items):
			if self.state == index:
				label = self.font.render(item,True,self.select_color)
			else:
				label = self.font.render(item,True,self.font_color)
			
			width = label.get_width()
			height = label.get_height()
			
			posX = (SCREEN_WIDTH /2) - (width /2)
			# t_h: total height of text block
			t_h = len(self.items) * height
			posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
			
			
			screen.blit(label,(posX,posY))
			
			
			
			
	
			
			
class Game(object):
	def __init__(self):
		# Create a new font obeject
		self.font = pygame.font.Font(None,65)
		# Create font for the score msg
		self.score_font = pygame.font.Font("fonts/kids3.ttf",20)
		# Create a dictionary with keys: num1, num2, result
		# These variables will be used for creating the
		# arithmetic problem
		self.problem = {"num1":0,"num2":0,"result":0}
		# Create a variable that will hold the name of the operation
		self.operation = ""
		self.symbols = self.get_symbols()
		self.button_list = self.get_button_list()
		# Create boolean that will be true when clicked on the mouse button
		# This is because we have to wait some frames to be able to show
		# the rect green or red.
		self.reset_problem = False
		# Create menu
		items = ("Add","Subtract","Multiply")
		self.menu = Menu(items,ttf_font="fonts/kids3.ttf",font_size=80)
		# True: show menu
		self.show_menu = True
		# create the score counter
		self.score = 0
		# Count the number of problems
		self.count = 0
		# load background image
		self.background_image = pygame.image.load("images/bg.jpg").convert()

		
		pygame.display.update()
		# load sounds effects
		self.sound_1 = pygame.mixer.Sound("sounds/right_answer.wav")
		self.sound_2 = pygame.mixer.Sound("sounds/wrong_answer.wav")
		
		
	
		
		

	def get_button_list(self):
		""" Return a list with four buttons """
		button_list = []
		# assign one of the buttons with the right answer
		choice = random.randint(1,4)
		# define the width and height
		width = 100
		height = 100
		# t_w: total width
	#	t_w = width * 2 + 50
		posX = (SCREEN_WIDTH / 2)
		posY = 275
		if choice == 1:
			btn = Button(posX,posY,width,height,self.problem["result"])
			button_list.append(btn)
		else:
			btn = Button(posX,posY,width,height,random.randint(0,20))
			button_list.append(btn)

		posX = 180
		
		if choice == 2:
			btn = Button(posX,posY,width,height,self.problem["result"])
			button_list.append(btn)
		else:
			btn = Button(posX,posY,width,height,random.randint(0,20))
			button_list.append(btn)

		posX = 290
		

		
		if choice == 3:
			btn = Button(posX,posY,width,height,self.problem["result"])
			button_list.append(btn)
		else:
			btn = Button(posX,posY,width,height,random.randint(0,20))
			button_list.append(btn)

		posX = 510
		
			
		if choice == 4:
			btn = Button(posX,posY,width,height,self.problem["result"])
			button_list.append(btn)
		else:
			btn = Button(posX,posY,width,height,random.randint(0,20))
			button_list.append(btn)
			
	
					
		return button_list
	

	def get_symbols(self):
		""" Return a dictionary with all the operation symbols """
		symbols = {}
		sprite_sheet = pygame.image.load("images/symbols.png").convert()
		image = self.get_image(sprite_sheet,0,0,64,64)
		symbols["addition"] = image
		image = self.get_image(sprite_sheet,64,0,64,64)
		symbols["subtraction"] = image
		image = self.get_image(sprite_sheet,128,0,64,64)
		symbols["multiplication"] = image

		return symbols

	def get_image(self,sprite_sheet,x,y,width,height):
		""" This method will cut an image and return it """
		# Create a new blank image
		image = pygame.Surface([width,height]).convert()
		# Copy the sprite from the large sheet onto the smaller
		image.blit(sprite_sheet,(0,0),(x,y,width,height))
		# Return the image
		return image

	def addition(self):
		""" These will set num1,num2,result for addition """
		a = random.randint(0,20)
		b = random.randint(0,20)
		self.problem["num1"] = a
		self.problem["num2"] = b
		self.problem["result"] = a + b
		self.operation = "addition"

	def subtraction(self):
		""" These will set num1,num2,result for subtraction """
		a = random.randint(0,20)
		b = random.randint(0,20)
		if a > b:
			self.problem["num1"] = a
			self.problem["num2"] = b
			self.problem["result"] = a - b
		else:
			self.problem["num1"] = b
			self.problem["num2"] = a
			self.problem["result"] = b - a
		self.operation = "subtraction"
			

	def multiplication(self):
		""" These will set num1,num2,result for multiplication """
		a = random.randint(0,5)
		b = random.randint(0,5)
		self.problem["num1"] = a
		self.problem["num2"] = b
		self.problem["result"] = a * b
		self.operation = "multiplication"


	def check_result(self):
		""" Check the result """
		for button in self.button_list:
			if button.isPressed():
				if button.get_number() == self.problem["result"]:
					# set color to green when correct
					button.set_color(GREEN)
					# increase score
					self.score += 1
					# Play sound effect
					self.sound_1.play()
				else:
					# set color to red when incorrect
					button.set_color(RED)
					# play sound effect
					self.sound_2.play()
				# Set reset_problem True so it can go to the
				# next problem
				# we'll use reset_problem in display_frame to wait
				# a second
				self.reset_problem = True

	def set_problem(self):
		""" do another problem again """ 
		if self.operation == "addition":
			self.addition()
		elif self.operation == "subtraction":
			self.subtraction()
		elif self.operation == "multiplication":
			self.multiplication()
	
		self.button_list = self.get_button_list()
		
		

	def process_events(self):
		for event in pygame.event.get():  # User did something
			if event.type == pygame.QUIT: # If user clicked close
				return True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.show_menu:
					if self.menu.state == 0:
						self.operation = "addition"
						self.set_problem()
						self.show_menu = False
					elif self.menu.state == 1:
						self.operation = "subtraction"
						self.set_problem()
						self.show_menu = False
					elif self.menu.state == 2:
						self.operation = "multiplication"
						self.set_problem()
						self.show_menu = False
		
				
				# We'll go to check_result to check if the user
				# answer correctly the problem
				else:
					self.check_result()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.show_menu = True
					# set score to 0
					self.score = 0
					self.count = 0

		return False

	def run_logic(self):
		# Update menu
		
		self.menu.update()

		
	def display_message(self,screen,items):
		""" display every string that is inside of a tuple(args) """
		for index, message in enumerate(items):
			label = self.font.render(message,True,YELLOW)
			# Get the width and height of the label
			width = label.get_width()
			height = label.get_height()
			
			posX = (SCREEN_WIDTH /2) - (width /2)
			# t_h: total height of text block
			t_h = len(items) * height
			posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
			
			
			screen.blit(label,(posX,posY))
			  

	def display_frame(self,screen):
		# Draw the background image
		
		#screen.blit(self.background_image,(0,0))										#################################### 										
		self.background_image = pygame.image.load("images/bg.jpg").convert()			## added 10/26
		screen.blit(self.background_image,(0,0))
																						####################################
		# True: call pygame.time.wait()
		time_wait = False
		# --- Drawing code should go here
		if self.show_menu:
			self.menu.display_frame(screen)
		elif self.count == 10:
			# if the count gets to 20 that means that the game is over
			# and we are going to display how many answers were correct
			# and the score
			#msg_1 = "You answered " + str(self.score / 1) + " correctly"
			msg_1 = "Your score was " + str(self.score) + " out of 10"
			msg_2 = "GREAT JOB!!! Try Again..."
			self.display_message(screen,(msg_1,msg_2))
			self.show_menu = True
			# reset score and count to 0
			self.score = 0
			self.count = 0
			# set time_wait True to wait 3 seconds
			time_wait = True
		else:
			# Create labels for the each number
			label_1 = self.font.render(str(self.problem["num1"]),True,BLACK)
			label_2 = self.font.render(str(self.problem["num2"])+" = ?",True,BLACK)
			# t_w: total width
			t_w = label_1.get_width() + label_2.get_width() + 64 # 64: length of symbol
			posX = (SCREEN_WIDTH / 2) - (t_w / 2)
			screen.blit(label_1,(posX,150))                                                       ### HERE
			# print the symbol into the screen
			screen.blit(self.symbols[self.operation],(posX + label_1.get_width(),140))
			
			screen.blit(label_2,(posX + label_1.get_width() + 64,150))
			# Go to through every button and draw it
			for btn in self.button_list:
				btn.draw(screen)
			# display the score
			score_label = self.score_font.render("Score: "+str(self.score),True,BLACK)
			screen.blit(score_label,(10,10))
			
		# --- Go ahead and update the screen with what we've drawn
		
																				###########################################################################
		#pygame.font.init()														#added 10/26
		myfont = pygame.font.Font("fonts/kids3.ttf",80)
		myfont2 = pygame.font.Font("fonts/kids3.ttf",50)
		textsurface = myfont.render('MATH ADVENTURES', False, (YELLOW))
		textsurface2 = myfont2.render('X', False, (RED))
		screen.blit(textsurface, (110, 10))
		screen.blit(textsurface2, (760, 0))
																				###########################################################################
		pygame.display.flip()
		# --- This is for the game to wait a few seconds to be able to show
		# --- what we have drawn before it change to another frame
		if self.reset_problem:
			# wait 1 second
			pygame.time.wait(1000)
			self.set_problem()
			# Increase count by 1
			self.count += 1
			self.reset_problem = False
		elif time_wait:
			# wait three seconds
			pygame.time.wait(5000)

class Button(object):
	def __init__(self,x,y,width,height,number):
		self.rect = pygame.Rect(x,y,width,height)
		self.font = pygame.font.Font(None,60)
		self.text = self.font.render(str(number),True,BLACK)
		self.number = number
		self.background_color = WHITE

	def draw(self,screen):
		""" This method will draw the button to the screen """
		# First fill the screen with the background color
		pygame.draw.rect(screen,self.background_color,self.rect)
		# Draw the edges of the button
		pygame.draw.rect(screen,YELLOW,self.rect,3)
		# Get the width and height of the text surface
		width = self.text.get_width()
		height = self.text.get_height()
		# Calculate the posX and posY
		posX = self.rect.centerx - (width / 2)
		posY = self.rect.centery - (height / 2)
		# Draw the image into the screen
		screen.blit(self.text,(posX,posY))

	def isPressed(self):
		""" Return true if the mouse is on the button """
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			return True
		else:
			return False

	def set_color(self,color):
		""" Set the background color """
		self.background_color = color

	def get_number(self):
		""" Return the number of the button."""
		return self.number
		
		
		
		
		
		

def main():
	# Initialize all imported pygame modules
	pygame.init()
	# Initiate the game theme song
	pygame.mixer.init()
	# Loads the game theme song
	pygame.mixer.music.load('images/game_theme.ogg')
	# Plays endless loop theme song, if parameter is set to -1.
	pygame.mixer.music.play(-1)	
	# Set the width and height of the screen [width, height]
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	# Set the current window caption
	pygame.display.set_caption("Math Adventures")
	
	
	#Loop until the user clicks the close button.
	done = False
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	# Create game object
	game = Game()
	# -------- Main Program Loop -----------
	while not done:
				
		# --- Process events (keystrokes, mouse clicks, etc)
		done = game.process_events()
		# --- Game logic should go here
		game.run_logic()
		# --- Draw the current frame
		game.display_frame(screen)
		# --- Limit to 30 frames per second
		clock.tick(30)

	# Close the window and quit.
	# If you forget this line, the program will 'hang'
	# on exit if running from IDLE.
	pygame.quit()

if __name__ == '__main__':
	main()
