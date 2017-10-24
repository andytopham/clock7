#!/usr/bin/python
# blinktcontrol.py
# A simple controller for the Pimoroni blinkt hardware.

import time
import logging
import blinkt
LOGFILE = '/home/pi/master/clock7/log/blinkt.log'
ON = 255
OFF = 0
NUM_PIXELS = 8

class Blinktcontrol():
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.logger.info("Initialising blinktcontrol")
		blinkt.set_clear_on_exit()
  
	def setleds(self, state):
#		blinkt.set_all(state,state,state)	# params are r,g,b
		blinkt.set_pixel(0,state,state,state)	# params are r,g,b
		if state > 10:
			blinkt.set_pixel(1,state,state,state)	# params are r,g,b
		else:
			blinkt.set_pixel(1,0,0,0)		
		if state > 20:
			blinkt.set_pixel(2,state,state,state)	# params are r,g,b
		else:
			blinkt.set_pixel(2,0,0,0)		
		if state > 30:
			blinkt.set_pixel(3,state,state,state)	# params are r,g,b
		else:
			blinkt.set_pixel(3,0,0,0)		
		blinkt.show()
		return(0)
		
	def flash_error(self):
		self.setleds(1)
		time.sleep(1)
		self.setleds(0)
		return(0)
		
	def sequenceleds(self, delay=0.05, holdtime=0.5):
		self.logger.info("blinkt.sequenceleds")
		if delay > 4:
			delay = 4		# because we now have a lot of steps
		steps = 63
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

	
