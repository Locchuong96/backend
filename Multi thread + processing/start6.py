# Example 6 concurrent.futures , multiprocessing

import concurrent.futures 
import time

start  = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print("Done sleeping...")
    return "Done sleeping..." # Return a string so you can wrap it out ex: func()

if __name__ == "__main__":    
    
    result = []
    
    secs = [5,4,3,2,1]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # results = [executor.submit(do_something,1) for _ in range(10)] # a list of submit function
        
        results = [executor.submit(do_something,sec) for sec in secs] # a list of submit function
        
    for f in concurrent.futures.as_completed(results):
        print(f.result())
        
    finish = time.perf_counter()

    print(f"Finished in {round((finish-start),2)} seconds (s)")