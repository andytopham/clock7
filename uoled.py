#!/usr/bin/python
# uoled.py
# My routines for writing to the micro oled.
# This calls on info from guyc at py-gaugette on github and raspi.tv.
# GPIO docs are here...
# https://pypi.python.org/pypi/RPi.GPIO
# http://raspi.tv/2015/rpi-gpio-new-feature-gpio-rpi_info-replaces-gpio-rpi_revision
# ToDo
# Add horizontal scrolling with this...
# http://guy.carpenter.id.au/gaugette/2012/11/11/font-support-for-ssd1306/

import gaugette.ssd1306
#from gaugette.fonts import gaugette.font5x8
from gaugette.fonts import arial_16		# default, skinny
#from gaugette.fonts import curlz_22		# too fancy
#from gaugette.fonts import magneto_24		# very bold, ok
#from gaugette.fonts import stencil_24		# thick in bits, then skinny
from gaugette.fonts import tahoma_24		# very clear
from gaugette.fonts import tahoma_16		# very clear
#from gaugette.fonts import verdana_15		# too crunched
import time

# Setup which pins we are using to control the oled
RESET_PIN = 15
DC_PIN    = 16
# Using a 5x8 font
ROW_HEIGHT = 8
ROW_LENGTH = 20

class uoled:
	''' Class to control the micro oled based on the gaugette routines.
		The row numbering starts at 1.
		Calling writerow does not display anything. Also need to call display.
		'''
	def __init__(self):
		self.MySsd = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
		self.font = tahoma_24
		self.fontsize = 24		
		self.MySsd.begin()
		self.MySsd.clear_display()
	
	def scroll_text(self,rownumber,text):
		''' So far just scrolls one row.'''
#		print 'Scrolling row number ',rownumber
		x = 0
		y = ROW_HEIGHT * rownumber-1
		i = 0
		time.sleep(1)
		while i < len(text)-ROW_LENGTH:
			todraw = '{: <20}'.format(text[i:])
			self.MySsd.draw_text2(x,y,todraw,1)
			self.MySsd.display()
			i += 1
		time.sleep(1)
		return(0)
	
	def writerow(self,rownumber,string, fontselect):
		xpos = 0
		ypos = (rownumber-1) * self.fontsize
		if fontselect == False:								# so use the default font
			self.MySsd.draw_text2(xpos, ypos, string, 1)	# note the use of 'text2'
		else:
			self.MySsd.draw_text3(xpos, ypos, string, self.font)
		return(0)

	def draw_blob(self,x,y):
		self.MySsd.draw_pixel(x,y,True)
#		self.MySsd.draw_pixel(x+1,y,True)
#		self.MySsd.draw_pixel(x,y+1,True)
#		self.MySsd.draw_pixel(x+1,y+1,True)
		return(0)
		
	def draw_sprite(self,sprite):
		for o in sprite:
			for pt in o:
#				print o
				self.MySsd.draw_pixel(pt[0], pt[1], True)
		return(0)
		
	def delete_blob(self,x,y):
		self.MySsd.draw_pixel(x,y,False)
#		self.MySsd.draw_pixel(x+1,y,True)
#		self.MySsd.draw_pixel(x,y+1,True)
#		self.MySsd.draw_pixel(x+1,y+1,True)
		return(0)
		
	def display(self):
		self.MySsd.display()
		return(0)

	def show_time(self):
		while True:
			self.MySsd.clear_display()
			#			self.writerow(1, self.time_now, False)		# to clear old text	
			date_now = time.strftime("%b %d %Y", time.gmtime())
			time_now = time.strftime("%H:%M:%S", time.gmtime())
			self.writerow(1, time_now, True)	# chg to big font
			self.writerow(2, date_now, False)	# std small font
			self.display()
			time.sleep(1)
		return(0)

	def game(self):
		x = 0
		y = 0
		while True:
			x += 1
		return(0)
		
if __name__ == "__main__":
	print 'uoled.py: showing real time clock.'
	myDisplay = uoled()
	myDisplay.show_time()
	myDisplay.display()
	