'''
File: structures.py
Module: libproc
Description: Defines the structures for proc filesystem. The structures are used
to communicate the system performance data with the graph service.
Date: 06/08/2016
'''
import os

class ProcData:
    '''
    ProcData is the structure used to record the data from the proc filesystem
    Methods provide functionality to access the structure and modify its
    properties.
    '''

    proc_data = {
        'loadavg': {
            '1': 0.0,
            '5': 0.0,
            '15': 0.0
        },
        'memory': {
            'total': 0.0,
            'free': 0.0,
            'available': 0.0
        },
        'swap': {
            'total': 0.0,
            'free': 0.0
        },
        'cpu': {
            'num': 0
        },
        'uptime': {
            'time': 0
        },
        'processes': {
            'proc_total': 0,
            'proc_running': 0,
            'softirq': 0
        },
        'hostname': {
            'name': ''
        }
    }

    def __init__(self):
        self.proc_data['hostname']['name'] = os.uname()[1]

    def setLoadAvg(self, data):
        if len(data)!=3:
            return False
        self.proc_data['loadavg'] = data
        return True

    def setMemoryUsage(self, data):
        if len(data)!=3:
            return False
        self.proc_data['memory'] = data
        return True

    def setSwapUsage(self, data):
        if len(data)!=2:
            return False
        self.proc_data['swap'] = data
        return True

    def setCpuCount(self, data):
        if len(data)!=1:
            return False
        self.proc_data['cpu'] = data
        return True

    def setUptime(self, data):
        if len(data)!=1:
            return False
        self.proc_data['uptime'] = data
        return True

    def setProcessCount(self, data):
        if len(data)!=3:
            return False
        self.proc_data['processes'] = data
        return True

    def getData(self):
        return self.proc_data
