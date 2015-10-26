#!/usr/bin/python
""" alarmtime.py

	"""
	
import time
import datetime
import logging

class AlarmTime():
	"""Class to manage the time for the alarm"""
	
	def __init__(self):
		logging.info("Initialising alarm time")
		a=0 # just to fix the formatting
		self.alarmhour=6
		self.alarmminute=20
		self.wealarmhour=7
		self.wealarmminute=00
		
	def read(self):
		logging.info("Reading alarm time")
		try:
			file=open('/home/pi/alarmtime.txt','r')
			line1=file.readline()
			line2=file.readline()
			file.close()
			a,b = line1.split(":")
			self.alarmhour=int(a)
			self.alarmminute = int(b)
			a,b = line2.split(":")
			self.wealarmhour=int(a)
			self.wealarmminute = int(b)
		except:
			logging.warning("Failed to open alarmtime file, using defaults.")
		logging.info("Weekday alarm time: %02d:%02d" % (self.alarmhour,self.alarmminute))
		logging.info("Weekend alarm time: %02d:%02d" % (self.wealarmhour,self.wealarmminute))
		print "Weekday alarm time: %02d:%02d" % (self.alarmhour,self.alarmminute)
		print "Weekend alarm time: %02d:%02d" % (self.wealarmhour,self.wealarmminute)
		return(0)
		
	def check(self):
		logging.info("Checking alarm")
		timenow=list(time.localtime())
		hour=timenow[3]
		minute=timenow[4] 
		day=timenow[6]
		if day < 5:				# weekday timings
			if ((hour == self.alarmhour) and (minute == self.alarmminute)):
				logging.warning("Alarm going off")
				print "Alarm going off"
				return(True)
			else:
				return(False)
		else:					# weekend timings
			if ((hour == self.wealarmhour) and (minute == self.wealarmminute)):
				logging.warning("Alarm going off")
				print "Alarm going off"
				return(True)
			else:
				return(False)
		

if __name__ == "__main__":
	'''	alarmtime main routine
		Sets up the logging and constants, before calling ...
	'''
#	logging.basicConfig(format='%(levelname)s:%(message)s',
	logging.basicConfig(
						filename='/home/pi/log/alarmtime.log',
						filemode='w',
						level=logging.INFO)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running alarmtime class as a standalone app")

	myAlarmTime = AlarmTime()
	while(True):
		myAlarmTime.check()
		time.sleep(2)
	
	