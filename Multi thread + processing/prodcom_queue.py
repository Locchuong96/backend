# Example 9
# producer and consumer example using quere
import threading 
import time 
import logging 
import random
import concurrent.futures
import queue

SENTINEL = object()

def producer(pipeline,event):
    """ Pretenf we are getting the message from the network, and the message coming in the burst""" 
    while not event.is_set(): # it now will loop until it see that the event was set on line 3, it also no longer puts the sentienl value into the pipeline
        message = random.randint(1,101)
        logging.info("Producer got message: %s",message)
        pipeline.set_message(message,"Producer")
    logging.info("Producer received EXIT event, exiting")
    
def consumer(pipeline,event):
    """Pretend that we are saving a number in the database."""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info("Consumer storing message: %s (queue size = %s)",
                     message,
                     pipeline.qsize())
            
# Pipeline is the subclass of queue.Queue class
class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize = 10) # it will limit the queue to that number of elements, causing .put() until there are fewer than maxsize, if you don't do that, it will grow to the limit of your computer's memory
        
    def get_message(self,name):
        logging.debug("%s: about to get from queue",name)
        value = self.get()
        logging.debug("%s: got %d from queue",name,value)
        return value
    
    def set_message(self,value,name):
        logging.debug("%s: about to add %d to queue",name,value)
        self.put(value)
        logging.debug("%s: added %d to queue",name,value)
            
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO,datefmt = "%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    pipeline = Pipeline()
    event = threading.Event()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        
        executor.submit(producer,pipeline,event) # run the function producer with the arg is pipeline
        executor.submit(consumer,pipeline,event)
        
        time.sleep(0.1)
        
        logging.info("Main:     about to set event")
        event.set()
        
    
