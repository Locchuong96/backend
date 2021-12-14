# Example 1
import logging 
import threading 
import time 

def thread_function(name):
    logging.info("Thread %s: starting",name)
    time.sleep(2)
    logging.info("Thread %s: finishing",name)
    
if __name__ == "__main__":
    format = "%(asctime)s %(message)s"
    logging.basicConfig(format = format, level = logging.INFO,datefmt = "%H:%M:%S")
    logging.info("Main      : before creating thread")
    x = threading.Thread(target = thread_function, args = (1,))
    logging.info("Main      : before running thread")
    x.start()
    logging.info("Main      : wait for thread to finish")
    # x.join() to tell one thread wait for another thread to finish, you call .join(), if you uncomment this line the main thread is wait for the thread x done, doesn't matter that thread is deamon or not
    
    logging.info("Main      : all done")