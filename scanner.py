#!/bin/bash

import sys
import socket
from datetime import datetime

# define a target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
else:
	print('Invalid amout of arguments')
	print('Syntax: python3 scanner.py <ip>')

# add a banner
print('-' * 50)
print('Scanning target: ' + target)
print('Time started: ' + str(datetime.now()))
print('-' * 50)

try:
	for port in range(1, 80):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.1)
		result = s.connect_ex((target, port)) # returns an error indicator
		if result == 0:
			print('Port {} is open'.format(port))
		s.close()

except KeyboardInterrupt:
	print('\nExiting program')
	sys.exit()
except socket.gaierror:
	print('Hostname could not be resolved')
except socket.error:
	print('Cannot connect to the server')
