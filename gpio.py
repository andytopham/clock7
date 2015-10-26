#!/usr/bin/python
''' 
  Module to control the gpio switches.
  Imported by iradio.
  Will poll switches in a loop if called standalone.
  Slice of Pi pinout:
	Pin	Slice 	RPi		Use
	11	GP0		GPIO17	SW1
	12	GP1		GPIO18	SW2
	13	GP2		GPIO21 	-
	15	GP3		GPIO22	yellow led
	16	GP4		GPIO23	-
	18	GP5		GPIO24	red led
	22	GP6		GPIO25
	7	GP7		GPIO4

RPi.GPIO lib is required for this class. To install gpio lib:
	sudo apt-get update
	sudo apt-get dist-upgrade
	sudo apt-get install python-rpi.gpio python3-rpi.gpio
	Not the following...
	wget https://raspberry-gpio-python.googlecode.com/files/RPi.GPIO-0.5.2a.tar.gz
	tar zxf RPi.GPIO-0.5.2a.tar.gz
	cd RPi.GPIO-0.5.2a
	sudo python setup.py install
'''
import RPi.GPIO as GPIO
import time
import datetime
import logging
#import config

class gpio:
	'''A class containing ways to handle the RPi gpio. '''
	def __init__(self):
		'''Initialise GPIO ports. '''
		self.logger = logging.getLogger(__name__)
		self.logger.info("Starting gpio class")
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		#start with some constants
		self.NEXTSW = 17
		self.STOPSW = 18
		self.VOLUP = 21
		self.VOLDOWN = 22
		self.YELLOWLED = 23					# temporary hack from 22
		self.REDLED = 24
#		self.PRESSED = config.PRESSED			# True for small box, False for metal box
		#then initialise the variables
		self.next = 0
		self.stop = 0
		self.vol = 0
		
	def writeledstate(self, lednumber, ledstate):
		led = []
		file = open('/home/pi/ledstate.txt','r+')		# read and write
		line = file.readline()
		led = line.split()
#		for i in range(8):
#			print "led ",led[i]
#		print "writing: ",str(lednumber),str(ledstate)
		led[lednumber] = ledstate
		file.seek(0)			# rewind file
		for i in range(8):
			file.write(str(led[i])+" ")
		file.close()
		return(0)
			
	def sequenceleds(self, delay=.5, holdtime=.5):
		'''Alternative test routine to be used with the clock3 slice of pi.'''
		self.logger.debug("def gpio sequenceleds")
		# This array is the Slice of Pi pins: GP0-7
#		a = [17,18,21,22,23,24,25,4]
#		a = [4,17,21,18,22,23,24,25]
		a = [4,17,27,18,22,23,24,25]	# rev 2 pinout
		# Set all pins as outputs
		for i in range(len(a)):
			GPIO.setup(a[i], GPIO.OUT)
			GPIO.output(a[i], GPIO.LOW)
		for i in range(len(a)):
			time.sleep(delay)
			print "High:",a[i]
			GPIO.output(a[i], GPIO.HIGH)
			self.writeledstate(i,1)
		time.sleep(holdtime)
		for i in range(len(a)):
			time.sleep(delay)
			print "Low:",a[i]
			GPIO.output(a[i], GPIO.LOW)
			self.writeledstate(i,0)
				
	def scan(self):
		a = [17,18,21,22,23,24,25,4]
		for i in range(len(a)):
			GPIO.setup(a[i],GPIO.IN)
			print a[i]," ",
		print
		while True:
			for i in range(len(a)):
	#			print a[i],GPIO.input(a[i])
				print GPIO.input(a[i]),"  ",
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
	myGpio.setup()
#	myGpio.scan()
#	myGpio.checkforstuckswitches()
#	myGpio.test()
	myGpio.sequenceleds()
