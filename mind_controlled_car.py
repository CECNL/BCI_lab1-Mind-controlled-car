import queue
from pylsl import StreamInlet, resolve_stream
import serial
import time

#### port"COM5"  must be change to suitable port
ser = serial.Serial("COM4", 9600, timeout = 1)




"""Example program to show how to read a multi-channel time series from LSL."""


queue_len = 15
q = queue.Queue(maxsize = queue_len)



threshhold = 0.0
# first resolve DATA from openvibe
print("looking for an openvibe stream...")
streams = resolve_stream('name', 'OpenViBE Stream1')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])


while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    time.sleep(0.1)
    sample, timestamp = inlet.pull_chunk() 
    if timestamp:
#         print(sample[0][0])
        

        tmp = sample[0][0]

        if q.qsize()<queue_len:
            q.put(tmp)
        else:
            _ = q.get()
            q.put(tmp)


        ratio = (sum(list(q.queue))/len(list(q.queue)))


        if ratio > threshhold and len(list(q.queue)) == queue_len:
            print("move forward",ratio)
            ser.write(b'1')

        elif ratio < threshhold:
            print("stop ",ratio)
            ser.write(b'0')

        
        
        
