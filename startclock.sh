#! /bin/sh
# /etc/init.d/startclock.sh
# The script to start clock7 at power up.

# Some things that run always
# the next line is needed to allow the ip address to be settled
sleep 20
python /home/pi/master/clock7/clock7.py &

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "This could be starting clock7, but does nothing at present "
    echo "Could do more here"
    ;;
  stop)
    echo "This could be stopping clock7 but does nothing at present"
    echo "Could do more here"
    ;;
  *)
    echo "Usage: /etc/init.d/startclock7.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
