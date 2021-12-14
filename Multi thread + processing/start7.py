# Example 7 , multiprocessing with map

import concurrent.futures 
import time 

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print("Done sleeping...")
    return "Done sleeping..." # Return a string so you can wrap it out ex: func()

start = time.perf_counter()

if __name__ == "__main__":
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = executor.map(do_something,secs) # map return wrap result of the function
        
    print(type(results))
    
    for result in results:
        print(result)
        
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    
    finish = time.perf_counter()
    
    print(f"Finished in {round((finish - start),2)}")
