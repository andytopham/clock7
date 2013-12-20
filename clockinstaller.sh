#!/bin/sh
echo "clock installer"
echo
echo "apt-get update"
apt-get update
echo
echo "apt-get -y upgrade"
apt-get -y upgrade
echo "installing rpi-gpio"
apt-get install python-dev
apt-get install python-rpi.gpio
echo "installing web stuff"
apt-get -y install lighttpd
apt-get -y install php5-common
apt-get -y install php5-cgi
apt-get -y install php5
lighty-enable-mod fastcgi-php
service lighttpd force-reload
