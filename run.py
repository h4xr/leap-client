from libproc.helpers import PerfData
import threading
import client

data = PerfData()

def sample():
    threading.Timer(client.sampling_interval, sample).start()
    data.performSampling()
    print data.getPerfData()
    client.http_client.makeDataRequest(api='/api/report/', data=data.getPerfData())

threading.Timer(client.sampling_interval, sample).start()
