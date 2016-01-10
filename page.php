<?php
/* page.php
 The php to go with the clock7 webpage.
*/

// ToDo: split this php into a separate file, then editor can behave correctly.
define('CLOCKDIR','/home/pi/master/clock7/');
define('ALARMTIME',CLOCKDIR.'alarmtime.txt');
define('LEDSTATE',CLOCKDIR.'ledstate.txt');
$secondsWait = 20;
header("Refresh:$secondsWait");		# this refreshes the page.
echo "Time now: " . date("D H:i", time()) . "<br>";
$lines = file(ALARMTIME);
$altime = trim($lines[0]);	# trim removes the newline char.
$wetime = trim($lines[1]);
$holdtime = trim($lines[2]);
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
	fwrite($f, $altime."\n");		# must be double quotes!
	fwrite($f, $wetime."\n");
	fwrite($f, $holdtime);
	fclose($f); 
} 

function validate($incoming){	# extra checks that also avoid hack entries
	$incoming = trim($incoming);
	$incoming = stripslashes($incoming);
	$incoming = htmlspecialchars($incoming);
	return $incoming;
}
?>

