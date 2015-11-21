<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- This is the web page for setting the alarm time for clock7.py -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="apple-mobile-web-app-capable" content="yes" />
	<link rel="shortcut icon" href="favicon.ico" />
	<link rel="desktop icon" href="sunrise.ico" />
	<title>Alarm Clock</title>
	<style type="text/css" media="screen">
		body { background: #e7e7e7; font-family: Verdana, sans-serif; font-size: xx-large; }
		
		<!--#page { background: #ffffff; margin: 50px; border: 2px solid #c0c0c0; padding: 10px; }
		#header { background: #4b6983; border: 2px solid #7590ae; text-align: center; padding: 10px; color: #ffffff; }
		#header h1 { color: #ffffff; }
		#body { padding: 10px; }
		span.tt { font-family: monospace; }
		span.bold { font-weight: bold; }
		a:link { text-decoration: none; font-weight: bold; color: #C00; background: #ffc; }
		a:visited { text-decoration: none; font-weight: bold; color: #999; background: #ffc; }
		a:active { text-decoration: none; font-weight: bold; color: #F00; background: #FC0; }
		a:hover { text-decoration: none; color: #C00; background: #FC0; }
		-->
	</style>
</head>

<body>
	<div id="page">
		<div id="header">
			<h1> Clock 7.3 </h1>
		</div>

		<div id="body">
		  <?php
			define('CLOCKDIR','/home/pi/clock7/');
			define('ALARMTIME',CLOCKDIR.'alarmtime.txt');
			define('LEDSTATE',CLOCKDIR.'ledstate.txt');
			$secondsWait = 20;
			header("Refresh:$secondsWait");		# this refreshes the page.
			echo "Time now: " . date("D H:i", time()) . "<br>";
			$lines = file(ALARMTIME);
			$altime = trim($lines[0]);	# trim removes the newline char.
			$wetime = trim($lines[1]);
#			echo "Weekday alarm:   ". $altime . "<br>";
#			echo "Weekend alarm:   ". $wetime . "<br>";

			$lines = file(LEDSTATE);
			echo "LED state:   ". $lines[0] ."<br>";
			
			if ($_POST){
				$newalarmtime = $altime;
				$newwealarmtime = $wetime;
				if ($_POST['newalarmtime']){
					$altime = validate($_POST['newalarmtime']);
					echo "New alarm time : " . $altime . "<br>";
					header("Refresh:0");		# this refreshes the page.
				}else{
					$newalarmtime = $altime;
				}
				if ($_POST['newwealarmtime']){
					$wetime = validate($_POST['newwealarmtime']);
					echo "New we alarm time : " . $wetime . "<br>";
					header("Refresh:0");		# this refreshes the page.
				}else{
					$newwealarmtime = $wetime;
				}
				$f=fopen(ALARMTIME,"w") or die("Could not open alarmtime.txt file for writing"); 
				fwrite($f, $altime."\n");
				fwrite($f, $wetime);
				fclose($f); 
			} 
			function validate($incoming){	# extra checks that also avoid hack entries
				$incoming = trim($incoming);
				$incoming = stripslashes($incoming);
				$incoming = htmlspecialchars($incoming);
				return $incoming;
			}
		  ?>
		   <form method="post" action="index.php" style="font-size:xx-large" >
			  Weekday alarm: 
				<input type="text" name="newalarmtime" value="<?php echo $altime;?>" style="font-size:xx-large">
			  <br>Weekend alarm: 
				<input type="text" name="newwealarmtime" value="<?php echo $wetime;?>" style="font-size:xx-large">
				<br><center><input type="submit" value="Submit" style="font-size:xx-large">
				</center>
			</form>
		  <br>
			<center>
				<img src="sunrise.jpg" alt="sunrise picture" > 
			</center>
		</div>
	</div>
</body>
</html>
