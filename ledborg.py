#!/usr/bin/python
# ledborg.py
# A simple controller for the ledborg hardware.

import time
import datetime
import logging
import wiringpi2 as wiringpi

wiringpi.wiringPiSetup()

LOGFILE = 'log/ledborg.log'

# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
OFF = [0,0,0]
RED = [1, 0, 0]
GREEN = [0, 1, 0]
BLUE = [0, 0, 1]
YELLOW = [1, 1, 0]
CYAN = [0, 1, 1]
MAGENTA = [1, 0, 1]
WHITE = [1, 1, 1]

class Ledborg():
	def __init__(self):
		wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
		wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
		wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)
  
	def setledborg(self, state):
		wiringpi.digitalWrite(PIN_RED, state[0])
		wiringpi.digitalWrite(PIN_GREEN, state[1])
		wiringpi.digitalWrite(PIN_BLUE, state[2])
		return(0)
		
	def sequenceleds(self, delay=0.5, holdtime=0.5):
		steps = 8		# for compatibility with other boards
		ontimesteps = 0.001
		ontime = 0.001
		offtime = 0.01
		for i in range(steps):
			cycles = delay / (ontime + offtime)
#			print 'cycles =',cycles
			for j in range(50):
				self.setledborg(WHITE)
				time.sleep(ontime)
				self.setledborg(OFF)
				time.sleep(offtime)
			ontime += ontimesteps
		self.setledborg(WHITE)			# max here
		time.sleep(holdtime)
		for i in range(steps):
			cycles = delay / (ontime + offtime)
#			print 'cycles =',cycles
			ontime -= ontimesteps
			for j in range(50):
				self.setledborg(WHITE)
				time.sleep(ontime)
				self.setledborg(OFF)
				time.sleep(offtime)
			
if __name__ == "__main__":
	'''Called if this file is called standalone. Then just runs a selftest. '''
	logging.basicConfig(filename=LOGFILE,
						filemode='w',
						level=logging.WARNING)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running gpio class as a standalone app")
	print 'ledborg test'
	MyLedborg = Ledborg()
	MyLedborg.sequenceleds()
	MyLedborg.setledborg(OFF)

	
