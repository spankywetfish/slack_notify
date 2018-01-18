#!/usr/bin/python3

### BEGIN INIT INFO
# Provides:	slack--notify
# Required-Start:
# Required-Stop:
# Default-Start:	2 3 4 5
# Default-Stop:	0 1 6
# Short-Description:	Slack alert of system state change
# Description:	Slack alert of system state change
### END INIT INFO

import sys
import json
import urllib3
import socket
import certifi

hostname = socket.gethostname()

# Slack incoming web hook URL
# e.g. slack_url = 'https://hooks.slack.com/services/blah/long-blah/even-longer-blah'
slack_url = '####### PLACE YOUR URL HERE #######'

def SendToSlack(output_data):
	http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
	req = http.request("POST", slack_url, body=json.dumps(output_data), headers={'Content-Type': 'application/json'})
	return;

print (sys.argv[1])

if sys.argv[1] == "start" :
	output_data = {}
	output_data['text'] = 'Server Status Change'
	output_data['response_type'] = "ephemeral"
	output_data['attachments'] = [ {'text' : hostname + ' is coming up', 'color': 'good' } ]
	SendToSlack(output_data)

if sys.argv[1] == "stop" :
	output_data = {}
	output_data['text'] = 'Server Status Change'
	output_data['response_type'] = "ephemeral"
	output_data['attachments'] = [ {'text' : hostname + ' is going down', 'color': 'danger' } ]
	SendToSlack(output_data)

