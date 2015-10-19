#!/usr/bin/python
""" clock7.py
	andyt clock using the piliter hardware.
"""
import time
#import sys
#import getopt
import os
#import subprocess
import logging
import datetime
#import re
import alarmtime	# my module
import gpio			# my module
		
def clockstart():	
	##The start of the real code ##
	"""Main:clock7"""
	"""Print info about the environment and initialise all hardware."""
	print "main:- Clock7.1 - piLiter clock code."
	logging.info("Setting time")
	os.environ['TZ'] = 'Europe/London'
	time.tzset
	myGpio=gpio.gpio()
	myGpio.sequenceleds()
	myAlarmTime=alarmtime.AlarmTime()
	myAlarmTime.read()

	while True:
		time.sleep(30)
		if(myAlarmTime.check()):
#			Parameters below are: delay, holdtime
			myGpio.sequenceleds(30,2000)	# this is the alarm
	  
if __name__ == "__main__":
	'''	clock6 main routine
		Sets up the logging and constants, before calling ...
	'''
#	logging.basicConfig(format='%(levelname)s:%(message)s',
	logging.basicConfig(
						filename='/home/pi/log/clock.log',
						filemode='w',
						level=logging.INFO)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running clock7 class as a standalone app")
	clockstart()
	