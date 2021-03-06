#!/usr/bin/python
# uoled_emulator.py

import os
import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
ROWHEIGHT = 20

class Uoled_Emulator():

	def __init__(self):
		x = 20
		y = 300
		os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
		pygame.init()
		pygame.display.set_mode((220, 80))
		pygame.display.set_caption('uoled emulator')
		self.screen = pygame.display.get_surface()
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill(BLACK)

	def writerow(self, rownumber, string):
		ypos = ROWHEIGHT / 2 + (rownumber - 1) * ROWHEIGHT
		font = pygame.font.Font(None, 24)
		text = font.render(string, 1, WHITE)
		textpos = text.get_rect(centery = ypos)
		self.background.blit(text, textpos)
		self.screen.blit(self.background, (0, 0))
		
	def draw_blob(self,x,y):
		surface.set_at((x,y), WHITE)
#		self.MySsd.draw_pixel(x,y,True)
		return(0)
		
	def delete_blob(self,x,y):
		surface.set_at((x,y), BLACK)
#		self.MySsd.draw_pixel(x,y,False)
		return(0)
		
	def display(self):
		pygame.display.flip()
		return(0)
		
	def draw_sprite(self,sprite):
		for o in sprite:
			for pt in o:
#				print o
				self.MySsd.draw_pixel(pt[0], pt[1], True)
		return(0)
