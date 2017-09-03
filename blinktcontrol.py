#!/usr/bin/python
# blinktcontrol.py
# A simple controller for the Pimoroni blinkt hardware.

import time
#import datetime
import logging
import blinkt
#import wiringpi2 as wiringpi

#wiringpi.wiringPiSetup()

LOGFILE = 'log/blinkt.log'
ON = 255
OFF = 0
NUM_PIXELS = 8

class Blinktcontrol():
	def __init__(self):
		blinkt.set_clear_on_exit()
  
	def setleds(self, state):
		blinkt.set_all(state,state,state)	# params are r,g,b
		blinkt.show()
		return(0)
		
	def flash_error(self):
		a = 1
		
	def sequenceleds(self, delay=0.5, holdtime=0.5):
		steps = 8		# for compatibility with other boards
		ontimesteps = 0.001
		ontime = 0.001
		offtime = 0.01
		for i in range(steps):
			print i
			self.setleds(i)
			time.sleep(delay)
		time.sleep(holdtime)
		for i in range(steps,0, -1):
			print i
			self.setleds(i)
			time.sleep(delay)
		self.setleds(0)			# turn them off
			
if __name__ == "__main__":
	'''Called if this file is called standalone. Then just runs a selftest. '''
	logging.basicConfig(filename=LOGFILE,
						filemode='w',
						level=logging.WARNING)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running gpio class as a standalone app")
	print 'blinkt test'
	MyBlinkt = Blinktcontrol()
	MyBlinkt.sequenceleds()

	
