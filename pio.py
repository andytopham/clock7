#!/usr/bin/python
""" pio.py
	To control leds mounted on Raspberry PI/O board.
	
"""
# Install: apt-get install python-smbus

import logging
import datetime
import smbus
import time

LOGFILE = '/home/pi/master/clock7/log/pio.log'

class Pio():
	"""Class to control the bank of 8 leds"""
	def __init__(self):
		logging.info("Initialising leds")
		self.address = 0x20 			# i2C address of MCP23017
		self.registera = 0x12
		self.registerb = 0x13
#		self.led = [1,2,4,8,16,32,64,128]
#		self.led = [1,4,16,64,128,32,8,2]
		self.led = [['a',1],['a',4],['a',16],['a',64],['b',128],['b',32],['b',8],['b',2]]
		self.bus = smbus.SMBus(1)
		self.bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
		self.bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 
	
	def ledsoff(self, off = True):
		if off == True:
			state = 0
		else:
			state = 0xFF
		logging.info("Turn off leds")
		self.bus.write_byte_data(self.address,self.registera,state)
		self.bus.write_byte_data(self.address,self.registerb,state)
		
		
	def selftest(self,waittime,holdtime):
		logging.info("Running led selftest")
		print "Running LED selftest"
		self.ledsoff()
		register=self.registera
		value = 0
		for i in range(8):
			value = i
			self.do_write2(value, waittime)
		self.ledsoff(False)
		time.sleep(holdtime)		# all on time
		# now turn them all on
		self.ledsoff(True)
		
	def do_write(self, value, waittime):
		print 'Writing:', value
		self.ledsoff()
		if value < 4:
			register=self.registera
		else:
			register=self.registerb		
		self.bus.write_byte_data(self.address,register,self.led[value])
		time.sleep(waittime)
		
	def do_write2(self, value, waittime):
		print 'Writing:', value
		self.ledsoff()
		register, thisled = self.led[value]
		if register == 'a':
			thisregister = self.registera
		else:	# 'b'
			thisregister = self.registerb
		self.bus.write_byte_data(self.address, thisregister, thisled)
		time.sleep(waittime)
		self.ledsoff()
		
	def lighting(self):
		print 'Lighting'
		vals = [0, 255, 255, 255, 255, 127, 127, 255]
		while True:
			for i in range(8):
#				print 'Lighting value:',i, vals[i]
				self.bittest(vals[i])
				time.sleep(5)
	
	def counter(self):
		print 'Counter'
		for i in range(256):
			self.bittest(i)
			time.sleep(.01)
		self.ledsoff()
			
	def bittest(self, value):
		writevaluea = 0
		writevalueb = 0
		mask = 1
		for i in range(8):
			reg, thisled = self.led[i]
			if value & mask:
				if reg == 'a':
					writevaluea += thisled
				else:
					writevalueb += thisled
			mask = mask << 1
		self.bus.write_byte_data(self.address, self.registera, writevaluea)
		self.bus.write_byte_data(self.address, self.registerb, writevalueb)
		
	
	def updateleds(self):
		logging.info("Update leds")
		timenow=list(time.localtime())
		hour=timenow[3]
		minute=timenow[4]
		day=timenow[6]
		alarmhour,alarmminute = readalarmtime()
		print "Time now: %02d:%02d. Day:%01d. Alarm time:%02d:%02d " % (hour,minute,day,alarmhour,alarmminute)
		if day in range(5):
			#		print "Valid alarm day"
			if hour == alarmhour and minute == alarmminute:
				selftest(stepinterval,leaveledson)
			else:
				heartbeat()
	
if __name__ == "__main__":
	'''	leds main routine
		Sets up the logging and constants, before calling ...
	'''
#	logging.basicConfig(format='%(levelname)s:%(message)s',
	logging.basicConfig(
						filename = LOGFILE,
						filemode='w',
						level=logging.INFO)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running pio class as a standalone app")
	myLeds=Pio()
#	myLeds.selftest(.5,1)
#	myLeds.counter()
	myLeds.lighting()
	
