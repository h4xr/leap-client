import time
from procfs import Proc
from .structures import ProcData

class PerfData:
    '''
    PerfData, provides the information about the performance data of the system.
    '''

    def __init__(self):
        self.proc = Proc()
        self.proc_data = ProcData()
        self.sample_time = time.time()

    def getLoadAverages(self):
        data = {
            '1': self.proc.loadavg.average[1],
            '5': self.proc.loadavg.average[5],
            '15': self.proc.loadavg.average[15]
        }
        return data

    def getMemoryInfo(self):
        data = {
            'total': self.proc.meminfo.MemTotal,
            'free': self.proc.meminfo.MemFree,
            'available': self.proc.meminfo.MemAvailable
        }
        return data

    def getSwapInfo(self):
        data = {
            'total': self.proc.meminfo.SwapTotal,
            'free': self.proc.meminfo.SwapFree
        }
        return data

    def getCpuInfo(self):
        data = {
            'num': len(self.proc.cpuinfo.keys())
        }
        return data

    def getUptime(self):
        data = {
            'time': self.proc.uptime.uptime.total_seconds()
        }
        return data

    def getProcessData(self):
        data = {
            'proc_total': self.proc.stat.processes,
            'proc_running': self.proc.stat.procs_running,
            'softirq': self.proc.stat.softirq.total
        }
        return data

    def performSampling(self):
        self.proc_data.setLoadAvg(self.getLoadAverages())
        self.proc_data.setMemoryUsage(self.getMemoryInfo())
        self.proc_data.setSwapUsage(self.getSwapInfo())
        self.proc_data.setCpuCount(self.getCpuInfo())
        self.proc_data.setUptime(self.getUptime())
        self.proc_data.setProcessCount(self.getProcessData())
        self.sample_time = time.time()
        return True

    def getPerfData(self):
        return self.proc_data.getData()
