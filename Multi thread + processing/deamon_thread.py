# Example 2
import logging 
import time 
import threading 

# Deamon thread, if the thread running as not as a deamon, then the __main__ wait until thread is done
# If the thread is running as a deamon, then if __main__ finish, terminate the thread immidiately

def thread_function(name):
    logging.info("Thread %s: starting",name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO,datefmt = "%H:%M:%S")
    logging.info("Main      :before creating thread")
    x =threading.Thread(target = thread_function,args = (1,),daemon = True)
    logging.info("Main      :before running thread")
    x.start()
    logging.info("Main      :wait for the thread to finish")
    logging.info("Main      :all done")