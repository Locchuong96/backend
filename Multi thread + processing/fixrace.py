# Example 6
# The basic functions to do this are .acquire() and .release().
# A thread will call my_lock.acquire() to get the lock.
# If the lock is already held, the calling thread will wait until it is released. 
# There’s an important point here. If one thread gets the lock but never gives it back, your program will be stuck. 
# You’ll read more about this later.

# Fortunately, Python’s Lock will also operate as a context manager, so you can use it in a with statement, and it gets released automatically when the with block exits for any reason.
# You can turn on full logging by setting the level to DEBUG by adding this statement after you congigure the logging output in __main__
# loggin will also log out the logging.debug line

import threading 
import time 
import concurrent.futures 
import logging 

#Create a class pretend as  fake datebase 
class FakeDatabase:
    
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        
    def locked_update(self,name):
        
        logging.info("Thread %s: starting update",name)
        logging.debug("Thread %s: about to lock",name)
        
        with self._lock:
            logging.debug("Thread %s has lock",name)
            local_copy =  self.value 
            local_copy +=1 
            time.sleep(0.1) 
            self.value = local_copy
            logging.debug("Thread %s about to release the lock",name)
            # release the lock after finishing this line
            
        logging.debug("Thread %s after release",name)
        logging.info("Thread %s: finishing update",name)
        
if __name__ == "__main__":
    
    format = "%(asctime)s : %(message)s"
    
    logging.basicConfig(format = format,level = logging.INFO,datefmt=  '%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    
    database = FakeDatabase()
    logging.info("Testing update, Starting value is %d.",database.value)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        for index in range(2):
            executor.submit(database.locked_update,index) # Tell the thread the run the function update .submit(function,*args,**kwargs)
        
    # printout the last value
    logging.info("Testing update,Ending value is %d.",database.value)
