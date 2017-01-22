# RFXServer

RFXServer is a small project that aims to capture messages received by RFXtrx433 (USB) transreceiver and simply write them as JSON objects to a log file. From there, the log can be easily processed with your favorite analytics tool (Splunk, ELK, ...) and you can build "Advanced Home Analytics" ! (-:

This server is a generic approach and will write any message as a JSON object. I tried it with Oregon sensors, but it should work with anything else discussing with a RFXtrx transceiver.

# Logs

/var/log/rfxserver/app.log
* Where messages received over RFXtrx433 are written to as JSON.

/var/log/rfxserver/error.log
* Where rfxserver state messages are written to.

A log message will looks like the folllwing:

```
{"device": {"subtype": 1, "packettype": 82, "type_string": "THGN122/123, THGN132, THGR122/228/238/268", "id_string": "f7:01"}, "timestamp": "2016-12-05 09:16:42", "values": {"Battery numeric": 9, "Rssi numeric": 8, "Temperature": 23.2, "Humidity": 49, "Humidity status numeric": 1, "Humidity status": "comfort"}}
```


# Installation

```
$ git clone ...
$ mkdir /var/log/rfxserver
$ cp -r server /usr/local/bin/rfxserver
$ cp init.d/rfxserver.sh /etc/init.d/
$ chmod 0755 /etc/init.d/rfxserver.sh
$ chmod +x /usr/local/bin/rfxserver/rfxserver.py
$ systemctl daemon-reload
$ sudo update-rc.d rfxserver.sh defaults
```


# Thanks

* Original RFXtrx module written by [@woudt](https://github.com/woudt/pyRFXtrx)


