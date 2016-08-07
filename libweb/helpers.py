import time
import requests
import os

class HttpRequest:
    '''
    HttpRequest, wraps the code to make HTTP requests by the client for the server
    collecting the data. The data is encoded into the JSON format and sent to
    the server specified using the hostname and port number. The class checks the
    response originating from the server to validate the status code.
    '''

    def __init__(self, hostname="http://localhost", port=80):
        '''
        Used to initialize the object with the specified hostname and port
        Defaults to http://localhost as hostname and 80 as port
        '''
        self.port = port
        self.hostname = hostname+":"+self.port

    def post(self, api, data):
        '''
        Used to make a post request to the server and validate the response code
        '''
        r = requests.post(self.hostname+api, data=data)
        if r.status_code==200:
            return True
        return False

    def get(self, api):
        '''
        Make a HTTP GET request to the server
        '''
        r =requests.get(self.hostname+api)
        if r.status_code==200:
            return r
        return False

    def makeDataRequest(self, api, data):
        '''
        Make a POST data request
        '''

        request_data = {
            'application_key': os.environ['LEAP_APP_KEY'],
            'application_secret': os.environ['LEAP_APP_SECRET'],
            'request_time': time.time(),
            'data': data
        }

        return self.post(api, request_data)
