#!/usr/bin/env python
# coding: utf8
import json
import datetime

from RFXtrx.pyserial import PySerialTransport
from modules.rfxlog import RFXLog
from modules.rfxsig import RFXSig


##########
# CONFIG #
##########

# interface to connect to the RFXtrx433
interface = "/dev/ttyUSB0"

#############
# FUNCTIONS #
#############

def connect(logger, interface):

    try:
	transport = PySerialTransport(interface, debug=False)
	transport.reset()
    except Exception, e:
	logger.error(e)
	raise e

    return transport

########
# MAIN #
########
logger = RFXLog()
signal = RFXSig(logger=logger)


logger.info("connecting to %s" % interface)
transport = connect(logger, interface)

while not signal.stop:
    try:
	evt = transport.receive_blocking()
	res = evt.to_json()

	res['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	logger.rfxevent( json.dumps(res) )

    except Exception, e:
	# triggered on shutting down
	logger.error("received an error in receive_blocking() -- %s" % e)

	if not signal.stop :
		logger.info("reconnecting to %s" % interface)
		transport = connect(logger, interface)

logger.info("end of life.")

