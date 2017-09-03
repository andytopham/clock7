#!/usr/bin/python
""" clock7.py
	andyt wake up light alarm clock using various hardware.
	Works with slice of pi (slice == True).
	Works with ledborg.
"""

import time
import os, sys
import logging
import datetime
import alarmtime	# my module
#board = 'slice'
board = 'blinkt'
if board == 'slice':
	import gpio			# my module
elif board == 'ledborg':
	import ledborg as gpio	# alternative led solution
elif board == 'uoled':
	import uoled
elif board == 'blinkt':
	import blinktcontrol
else:
	print "Error: board type not specified"
	sys.exit()
	
LOGFILE = '/home/pi/master/clock7/log/clock7.log'
		
def clockstart(board = 'blinkt'):	
	"""Main:clock7"""
	print "main:- Clock7.4 - alarm clock code."
	print 'Board selected:', board
	if board == 'slice':
		myGpio=gpio.gpio(board)
	elif board == 'ledborg':
		myGpio=gpio.Ledborg()
	elif board == 'blinkt':
		myGpio = blinktcontrol.Blinktcontrol()
	addr = '0'
#	addr = myGpio.get_ip_address()
	if addr is not '0':
		last_byte = addr.split('.')[3]
		print 'IP: ',addr,last_byte
		logging.info('IP address: '+addr)
		myGpio.writeleds(last_byte)
	else:
		logging.info('Zero IP address')
		myGpio.flash_error()
	myGpio.sequenceleds()
	myAlarmTime=alarmtime.AlarmTime()
	myAlarmTime.read()
	steptime = 30
	holdtime = 2000					# seconds
	holdtime = myAlarmTime.return_holdtime()
	print 'Entering main loop'
	while True:
		if(myAlarmTime.check()):
#			Parameters below are: delay, holdtime
			myGpio.sequenceleds(steptime,holdtime)	# this is the alarm
		time.sleep(30)				# check every 30 seconds
	  
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
	clockstart(board)
	