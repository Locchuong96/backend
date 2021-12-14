import multiprocessing 
import time 

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)....")
    time.sleep(seconds)
    print("Done Sleeping...")
        
processes = []
    
if __name__ == "__main__":
    multiprocessing.freeze_support()
    
    # We must create and join the the process in the __main__
    for _ in range(10):
        p = multiprocessing.Process(target = do_something,args = [1.5]) # the args must be serialize using pickle 
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()
        
    finish = time.perf_counter()
    print(f"Finished in {round (finish - start,2)} second(s)")
    