# Example 5
# Race condition will ocur when two or more threads access shared piece of the data of resource
# it will lead to more error logic and so hard to debug
import time 
import logging
import threading 
import concurrent.futures

#Create a class pretend as  fake datebase 
class FakeDatabase:
    def __init__(self):
        self.value = 0
        
    def update(self,name):
        logging.info("Thread %s: starting update",name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update",name)

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format = format,level = logging.INFO,datefmt=  '%H:%M:%S')
    
    database = FakeDatabase()
    logging.info("Testing update, Starting value is %d.",database.value)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        for index in range(2):
            executor.submit(database.update,index) # Tell the thread the run the function update .submit(function,*args,**kwargs)
        
    # printout the last value
    logging.info("Testing update,Ending value is %d.",database.value)
        
        
        