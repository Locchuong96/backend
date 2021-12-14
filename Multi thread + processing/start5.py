# Example 5 concurrent.futures , multiprocessing

import concurrent.futures 
import time

start  = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print("Done sleeping...")
    return "Done sleeping..." # Return a string so you can wrap it out ex: func()

if __name__ == "__main__":    
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something,1) # The submit method schedule the function to submit and return in the futures object
        f2 = executor.submit(do_something,1)
        print(f1.result()) # This wrapping will return a return  of do_something function
        print(f2.result())
        
    finish = time.perf_counter()

    print(f"Finished in {round((finish-start),2)} seconds (s)")