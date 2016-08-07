'''
File: client.py
Description: Sets the client up by reading the proper configuration variables
and API points
'''
import os
import time
from libweb.helpers import HttpRequest

hostname = os.environ['LEAP_HOSTNAME']
port = os.environ['LEAP_PORT']
sampling_interval = float(os.environ['LEAP_SAMPLING_RATE'])

http_client = HttpRequest(hostname, port)
