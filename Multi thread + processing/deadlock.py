# Example 7
# If a thread .acquire the Lock without .release() your function will stop in this thread forever
import threading 

l = threading.Lock()

print('before first acquire')

l.acquire()

# l.release()

print('before second acquire') # you never get this line if you don't release the lock 

l.acquire()

print("acquired lock twice")