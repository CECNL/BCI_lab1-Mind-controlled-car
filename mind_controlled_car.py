import queue
from pylsl import StreamInlet, resolve_stream


"""Example program to show how to read a multi-channel time series from LSL."""


queue_len = 20
q = queue.Queue(maxsize = queue_len)



threshhold = 0.7
# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('name', 'OpenViBE Stream1')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])


while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample, timestamp = inlet.pull_sample()
    if(sample[0]>0):
        tmp = 1
    else:
        tmp = 0
        
    if q.qsize()<queue_len:
        q.put(tmp)
    else:
        _ = q.get()
        q.put(tmp)

    
    ratio = (sum(list(q.queue))/len(list(q.queue)))


    if ratio > threshhold and len(list(q.queue)) == queue_len:
        print("move forward",ratio)
        """ 
            you need to write some code to send commend to the car
        """
        
    elif ratio < threshhold:
        print("stop ",ratio)
        """ 
            you need to write some code to send commend to the car
        """
        
        
        
