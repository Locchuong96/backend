# Example 8
# producer and consumer example
import threading 
import time 
import logging 
import random
import concurrent.futures


SENTINEL = object()

def producer(pipeline):
    """ Pretenf we are getting the message from the network, and the message coming in the burst""" 
    for index in range(10):
        message = random.randint(1,101)
        logging.info("Producer got message %s",message)
        pipeline.set_message(message,"Producer") # send the message on the pipeline for the consumer
        
    # Send a sentinel message to tell consumer we are done 
    pipeline.set_message(SENTINEL,"Producer") # ater send 10 message, send a sentinel for stopping
    
def consumer(pipeline):
    """Pretend that we are saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message %s",message)
            
class Pipeline:
    """
    Class to allow single element pipeline between producer and consumer.
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire() # the consumer hold it own lock, the consumer go first
        
    def get_message(self,name):
        logging.debug("%s:about to acquire getlock",name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock",name)
        message = self.message
        logging.debug("%s:about to release setlock",name)
        self.producer_lock.release() # release producer's lock for insert next message
        logging.debug("%s:setlock released",name)
        return message
    
    def set_message(self,message,name):
        logging.debug("%s:about to acquire setlock",name)
        self.producer_lock.acquire()
        logging.debug("%s: have setlock",name)
        self.message = message 
        logging.debug("%s:about to release getlock",name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released",name)
            
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO,datefmt = "%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        executor.submit(producer,pipeline) # run the function producer with the arg is pipeline
        executor.submit(consumer,pipeline)
        
    
