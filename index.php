<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- 	This is the web page for setting the alarm time for clock7.py.
		RPi webserver is lighttpd
		To restart webserver after any changes here... sudo service lighttpd force-reload.
		This expects the alarmtime file to contain daily alarm time, weekend alarm time and hold time.
		-->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="apple-mobile-web-app-capable" content="yes" />
	<link rel="shortcut icon" href="favicon.ico" />
	<link rel="desktop icon" href="sunrise.ico" />
	<title>Alarm Clock</title>
	<style type="text/css" media="screen">
		body { background: #e7e7e7; font-family: Verdana, sans-serif; font-size: xx-large; }	
	</style>
</head>

<body>
	<div id="page">
		<div id="header">
			<h1> Clock 7.4 </h1>
		</div>
		<div id="body">
			<!-- This next line has most of the work. -->
			<?php include 'page.php'; ?>
			<form method="post" action="index.php" style="font-size:xx-large" >
			  Weekday alarm: 
				<input type="text" name="newalarmtime" value="<?php echo $altime;?>" style="font-size:xx-large">
			  <br>Weekend alarm: 
				<input type="text" name="newwealarmtime" value="<?php echo $wetime;?>" style="font-size:xx-large">
			  <br>Hold time: 
				<input type="text" name="holdtime" value="<?php echo $holdtime;?>" style="font-size:xx-large">
				<br><center><input type="submit" value="Submit" style="font-size:xx-large">
				</center>
			</form>
			<br>
			<center> <img src="sunrise.jpg" alt="sunrise picture" > </center>
		</div>
	</div>
</body>
</html>
