#!/bin/sh -e

### BEGIN INIT INFO
# Provides:        rfxserver
# Required-Start:  $syslog
# Required-Stop:   $syslog
# Default-Start:   2 3 4 5
# Default-Stop: 
# Short-Description: Start the rfxserver python script to collect RFXTRX433 data
### END INIT INFO

PATH=/sbin:/bin:/usr/sbin:/usr/bin

. /lib/lsb/init-functions

DAEMON=/usr/local/bin/rfxserver/rfxserver.py
PIDFILE=/var/run/rfxserver.pid

test -x $DAEMON || exit 5


case $1 in
	start)
		log_daemon_msg "Starting RFXServer"
  		start-stop-daemon --background --start --quiet --oknodo --pidfile $PIDFILE --make-pidfile --startas $DAEMON 
		log_end_msg $?
  		;;
	stop)
		log_daemon_msg "Stopping RFXServer"
  		start-stop-daemon --stop --quiet --oknodo --pidfile $PIDFILE --signal TERM --retry 5
		log_end_msg $?
		rm -f $PIDFILE
  		;;
	restart)
		$0 stop && sleep 2 && $0 start
  		;;
	status)
		status_of_proc $DAEMON "RFXServer"
		;;
	*)
		echo "Usage: $0 {start|stop|restart|status}"
		exit 2
		;;
esac

