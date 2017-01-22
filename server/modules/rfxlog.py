#!/usr/bin/python
# coding: utf8

import os
import logging

from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler 

class RFXLog(object):

    def __init__(self, debug=False, logdir="/var/log/rfxserver"):
    	self.loglevel = logging.INFO
	if debug:
		self.loglevel = logging.DEBUG

	self._logpath( logdir )
	self._init_errLogger()
	self._init_appLogger()

    def _logpath(self, logdir):

	if not os.path.exists(logdir) :
		raise ValueError("directory %s does not exist." % logdir)

	self.appLogFile = os.path.join(logdir, "app.log")
	self.errLogFile = os.path.join(logdir, "error.log")

    def _init_errLogger(self):
	self.errLogger = logging.getLogger('errLogger')
	self.errLogger.propagate = False
	self.errLogger.setLevel(self.loglevel)
 
	formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

	handler = TimedRotatingFileHandler(self.errLogFile, when="midnight", interval=1, backupCount=31)
	handler.setFormatter(formatter)

	self.errLogger.addHandler(handler)


    def _init_appLogger(self):
	self.appLogger = logging.getLogger('appLogger')
	self.appLogger.propagate = False
	self.appLogger.setLevel(logging.INFO)
 
	formatter = logging.Formatter('%(message)s')

	handler = TimedRotatingFileHandler(self.appLogFile, when="midnight", interval=1, backupCount=31)
	handler.setFormatter(formatter)
	
	self.appLogger.addHandler(handler)


    def rfxevent(self, message):
	self.appLogger.info( message )

    def info(self, message):
	self.errLogger.info( message )

    def error(self, message):
	self.errLogger.error( message )

    def warn(self, message):
	self.errLogger.warning( message )

    def warning(self, message):
	self.errLogger.warning( message )

    def debug(self, message):
	self.errLogger.debug( message )


