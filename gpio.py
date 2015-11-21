#!/usr/bin/python
# gpio.py
# Control leds connected to gpio pins, typically via a slice of pi board.

import RPi.GPIO as GPIO
import time
import datetime
import logging
LEDSTATEFILE = '/home/pi/clock7/ledstate.txt'
SLICE_OF_PI = True

class gpio:
	'''A class containing ways to handle the RPi gpio. '''
	def __init__(self):
		'''Initialise GPIO ports. '''
		self.logger = logging.getLogger(__name__)
		self.logger.info("Starting gpio class")
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.rpi_gpio_chk_function()	
		rev = GPIO.RPI_INFO['P1_REVISION']
		print 'RPi board revision:',str(rev)
		if rev == 1:
			if SLICE_OF_PI == True:
				self.pins = [17,18,21,22,23,24,25,4]	# wiring pi numbering
			else:
				self.pins = [4,17,21,18,22,23,24,25]
		else:
			if SLICE_OF_PI == True:	# This array is the Slice of Pi pins: GP0-7
				self.pins = [17,18,27,22,23,24,25,4]	# wiring pi numbering
			else:
				self.pins = [4,17,27,18,22,23,24,25]	# rev 2 pinout
		for i in range(len(self.pins)):
			GPIO.setup(self.pins[i], GPIO.OUT)

	def rpi_gpio_chk_function(self):
		# Now updated to use BCM mode
		retstr = ''
		pin = 10		# 19
		GPIO.setmode(GPIO.BCM)
		func = GPIO.gpio_function(pin)
		if func == GPIO.SPI:
			print 'SPI enabled'
			retstr += 'SPI '
		else:
			print 'Warning: SPI not enabled!'
		pin = 2		# 3
		func = GPIO.gpio_function(pin)
		if func == GPIO.I2C:
			print 'I2C enabled'
			retstr += 'I2C '
		else:
			print 'Warning: I2C not enabled!'
		pin = 14 		# 8
		func = GPIO.gpio_function(pin)
		if func == GPIO.SERIAL:
			print 'Serial enabled'
			retstr += 'Serial '
		else:
			print 'Warning: Serial not enabled!'
		pin = 18 		# 12
		func = GPIO.gpio_function(pin)
		if func == GPIO.HARD_PWM:
			print 'PWM enabled'
			retstr += 'PWM '
		else:
			print 'Warning: PWM not enabled!'
		return(retstr)
	
	def writeledstate(self, lednumber, ledstate):
		''' Save the state of an led in the state file. '''
		led = []
		try:
			file = open(LEDSTATEFILE,'r+')		# read and write
		except:
			file = open(LEDSTATEFILE,'w')		# if file does not exist
			file.write('0 0 0 0 0 0 0 0')
			file.close()
			file = open(LEDSTATEFILE,'r+')		# read and write	
		line = file.readline()
		led = line.split()
		led[lednumber] = ledstate
		file.seek(0)			# rewind file
		for i in range(8):
			file.write(str(led[i])+" ")
		file.close()
		return(0)
			
	def sequenceleds(self, delay=0.5, holdtime=0.5):
		'''The main led alarm sequence. Also, alternative test routine to be used with the clock3 slice of pi.'''
		self.logger.debug("def gpio sequenceleds")
		# Set all pins as outputs
		for i in range(len(self.pins)):
			GPIO.setup(self.pins[i], GPIO.OUT)
			GPIO.output(self.pins[i], GPIO.LOW)
		for i in range(len(self.pins)):
			time.sleep(delay)
			print "High:",self.pins[i]
			GPIO.output(self.pins[i], GPIO.HIGH)
			self.writeledstate(i,1)
		time.sleep(holdtime)
		for i in range(len(self.pins)):
			time.sleep(delay)
			print "Low:",self.pins[i]
			GPIO.output(self.pins[i], GPIO.LOW)
			self.writeledstate(i,0)
				
	def scan(self):
		# Continuously read the gpio input pins and print results.
		for i in range(len(self.pins)):
			GPIO.setup(self.pins[i],GPIO.IN)
			print self.pins[i]," ",
		print
		while True:
			for i in range(len(self.pins)):
				print GPIO.input(self.pins[i]),"  ",
			print
			time.sleep(1)
		
if __name__ == "__main__":
	'''Called if this file is called standalone. Then just runs a selftest. '''
	logging.basicConfig(filename='log/gpio.log',
						filemode='w',
						level=logging.WARNING)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running gpio class as a standalone app")
	myGpio = gpio()
	myGpio.sequenceleds()		# use this as a self test
