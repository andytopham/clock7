#!/usr/bin/python
""" clock7.py
	andyt wake up light alarm clock using various hardware.
	Works with slice of pi (slice == True).
	Works with ledborg.
"""

import time
import os
import logging
import datetime
import alarmtime	# my module
slice = True
if slice == True:
	import gpio			# my module
else:
	import ledborg as gpio	# alternative led solution

LOGFILE = '/home/pi/clock7/log/clock7.log'
		
def clockstart(slice):	
	"""Main:clock7"""
	print "main:- Clock7.3 - piLiter clock code."
	if slice == True:
		myGpio=gpio.gpio()
	else:
		myGpio=gpio.Ledborg()
	myGpio.sequenceleds()
	myAlarmTime=alarmtime.AlarmTime()
	myAlarmTime.read()

	while True:
		time.sleep(30)				# check every 30 seconds
		if(myAlarmTime.check()):
#			Parameters below are: delay, holdtime
			myGpio.sequenceleds(30,2000)	# this is the alarm
	  
if __name__ == "__main__":
	'''	clock6 main routine
		Sets up the logging and constants, before calling ...
	'''
#	logging.basicConfig(format='%(levelname)s:%(message)s',
	logging.basicConfig(
						filename=LOGFILE,
						filemode='w',
						level=logging.INFO)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running clock7 class as a standalone app")
	clockstart(slice)
	