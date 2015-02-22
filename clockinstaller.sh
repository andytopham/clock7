#!/bin/sh
echo "clock7 installer"
echo
echo "apt-get update"
apt-get update
echo
echo "apt-get -y upgrade"
apt-get -y upgrade
echo "installing rpi-gpio"
apt-get -y install python-dev
apt-get -y install python-rpi.gpio
echo "setup dirs"
mkdir log
echo "installing web stuff"
apt-get -y install lighttpd
apt-get -y install php5-common
apt-get -y install php5-cgi
apt-get -y install php5
lighty-enable-mod fastcgi-php
service lighttpd force-reload
echo "Now set correct webpage by..."
echo "Edit /etc/lighttpd/lighttpd.conf and change root page to ~"
echo "Then restart webserver by: sudo service lighttpd force-reload"
