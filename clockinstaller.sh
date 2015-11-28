#!/bin/sh
echo "clock7 installer"
#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi
echo "Doing updates"
apt-get update
apt-get -y upgrade
apt-get -y install python-dev
apt-get -y install python-rpi.gpio
echo "Setup dirs"
mkdir log
echo 'Enable alarmtime file for writing by web server'
chmod 666 alarmtime.txt
echo 'Allow to run at power up'
cp startclock.sh /etc/init.d
chmod 755 /etc/init.d/startclock.sh
update-rc.d startclock.sh defaults
echo "Installing web stuff"
apt-get -y install lighttpd
apt-get -y install php5-common
apt-get -y install php5-cgi
apt-get -y install php5
lighty-enable-mod fastcgi-php
lighty-enable-mod cgi
lighty-enable-mod userdir
service lighttpd force-reload
echo "Now set correct webpage by..."
echo "First check that lighty is running by logging onto this server."
echo "!! Read the output of this carefully !! It tells you what to do next."
echo "Then..."
echo "Edit /etc/lighttpd/lighttpd.conf and change server.document-root page to this directory."
echo "Then restart webserver by: sudo service lighttpd force-reload"
echo "Error log is in /var/log/lighttpd, but will need to chmod 777 first."

