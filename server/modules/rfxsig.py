#!/usr/bin/env python
# coding: utf8

import signal

class RFXSig(object):
    """
	basic signal managment

	SIGINT : Interrupt from keyboard
	SIGQUIT: Quit from keyboard
	SIGTERM: Termination signal
    """

    stop_signals = ['SIGINT','SIGQUIT','SIGTERM']
    uncatchable  = ['SIGKILL', 'SIGSTOP']


    def __init__(self, logger):
	self.stop = False
   	self.logger  = logger

	#{1: 'SIGHUP', 2: 'SIGINT', ... }
	self.SIGNALS = dict((getattr(signal, n), n) for n in dir(signal) if n.startswith('SIG') and '_' not in n )

	for (k,v) in self.SIGNALS.iteritems():
		# some signals cannot be caught
		if v in self.uncatchable :
			continue

		if v in self.stop_signals:
			signal.signal(k, self.stop_handler)
		else:
			signal.signal(k, self.default_handler)
		
    def default_handler(self, signum, frame):
	try:
		sig_name = self.SIGNALS[ signum ]
	except:
		sig_name = None
	self.logger.warning("ignoring received signal %s/%s." % (signum,sig_name))


    def stop_handler(self, signum, frame):
	self.stop = True

	try:
		sig_name = self.SIGNALS[ signum ]
	except:
		sig_name = None
	self.logger.info("received signal %s/%s, shutting down." % (signum,sig_name))

